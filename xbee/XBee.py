import serial
from collections import deque


class XBee():
	rxbuff = bytearray()
	rxmessages = deque()

	def	__init__(self, serialport, baudrate=9600):
		#set self.serial to be the serial port and baudrate set by main
		self.serial = serial.Serial(port=serialport, baudrate=baudrate)

	def Receive(self):
		"""
			Reads data from serial port and checks buffer
			Returns next message in the queue
		"""
		#get the buffer data from serial port and put it to remaining
		remaining = self.serial.inWaiting()
		#loop to keep probing until empty
		while remaining:
			chunk = self.serial.read(remaining)
			remaining -= len(chunk)
			self.rxbuff.extend(chunk)
		
		msgs = self.rxbuff.split(bytes(b'\x7E'))
		for msg in msgs[:-1]:
			self.Validate(msg)

		self.rxbuff = (bytearray() if self.validate(msgs[-1]) else msgs[-1])

		if self.rxmessages:
			return self.rxmessages.popleft()
		else:
			return None

	def Validate(self, msg):
		"""
			Parses a byte and makes sure that they are properly formatted

			Input is a message meant to be trasnmitted by XBee
			
			Output, T o F, message valid or not
		"""
		#according to the docs we need 9 bytes min length
		if(len(msg) - msg.count(bytes(b'0x7D'))) < 9:
			return False
		
		#unescaping data before validating content
		frame = self.Unescape(msg)

		LSB = frame[1]
		#gotta have atleast equal length to LSB
	
		if LSB > (len(frame[2:])-1):
			return False

		#validate checksum
		if(sum(frame[2:3+LSB]) & 0xFF) != 0xFF:
			return False

		print("Rx: " + self.format(bytearray(b'\x7E') + msg))
		self.rxmessages.append(frame)
		return True

	def SendStr(self, msg, addr=0xFFFF, options=0x01, frameid=0x00):
		"""
		This is where we actually will send our data
		Input:
			msg: The message that is expected to be sent
			addr: The 16 bit address of the destination XBee
				(default:0xFFFF which is to broadcast)
			options: Optional byte to specify transmission options
				(default 0x01: disable awk)
			frameid: Optional frameid, only use if Tx status is desired
		Returns:
			Number of bytes sent
		"""
		
		return self.Send(msg.encode('utf-8'), addr, options, frameid)

	def Self(self, msg, addr=0xFFFF, options=0x01, frameid=0x00):
		"""
		Inputs:
			msg: A message, in bytes to be sent to XBee
			addr: the 16 bit address of the destination XBee
				(default is set to broadcast)
			options: Optional byte to specify transmission options
				(default 0x01: disable ACK)
			frameid: optional, only used if status is desired
		Returns:
			Number of bytes sent
		"""	

