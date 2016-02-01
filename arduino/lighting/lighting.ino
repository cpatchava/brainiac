#include <Lighting.h>
#include "XBee.h"
#include "queue.h"
#include <SoftwareSerial.h>

XBee xbee;
Queue RxQ;
Lighting lighting;
const int pin1 = 10;
const int pin2 = 11;
const int pin3 = 12;
const int pin4 = 13;

void setup(void)
{
    Serial.begin(9600);
    
    pinMode(pin1, OUTPUT);
    pinMode(pin2, OUTPUT);
    pinMode(pin3, OUTPUT);
    pinMode(pin4, OUTPUT);
}

void loop(void)
{
    delay(5);
    int queueLen = 0;
    int delPos = 0;
   
    while (Serial.available() > 0){
        unsigned char in = (unsigned char)Serial.read();
        if (!RxQ.Enqueue(in)){
            break;
        }
    }

    queueLen = RxQ.Size();
    for (int i=0;i<queueLen;i++){
        if (RxQ.Peek(i) == 0x7E){
            unsigned char checkBuff[Q_SIZE];
            unsigned char msgBuff[Q_SIZE];
            unsigned char address[8];
            int checkLen = 0;
            int msgLen = 0;
            int frameLen =0;

            checkLen = RxQ.Copy(checkBuff, i);
            msgLen = xbee.Receive(checkBuff, checkLen, msgBuff);
            if (msgLen > 0){
                unsigned char outMsg[Q_SIZE];
                unsigned char outFrame[Q_SIZE];
                int frameLen = 0;
                int x =0;
                while(x<8){
                  address[x] = msgBuff[x+4];
                  x++;
                }
                int just_msg = checkLen - 17;
                // 10 is length of "you sent: "
                //memcpy(outMsg, "you sent: ", 10);
                memcpy(outMsg, &msgBuff[15], just_msg);
                //Serial.write(outMsg, just_msg);
                //Serial.println();
                int idx = (int)outMsg[0];
                idx = idx-48;
                int act = outMsg[1];
                act = act-48;
                lighting.update(idx, act);
                act = lighting.status_switch(idx);
                
                  switch(idx){
                    case 0:
                      if(act == 1){
                        digitalWrite(pin1, HIGH);
                      }
                      else{
                        digitalWrite(pin1, LOW);
                      }
                      break;
                    case 1:
                      if(act == 1){
                        digitalWrite(pin2, HIGH);
                      }
                      else{
                        digitalWrite(pin2, LOW);
                      }
                      break;
                    case 2:
                      if(act == 1){
                        digitalWrite(pin3, HIGH);
                      }
                      else{
                        digitalWrite(pin3, LOW);
                      }
                      break;
                    case 3:
                      if(act == 1){
                        digitalWrite(pin4, HIGH);
                      }
                      else{
                        digitalWrite(pin4, LOW);
                      }
                      break;
                    default:
                      break;  
                  }
                  
                
                
                frameLen = xbee.Send(outMsg, just_msg, outFrame, address, 0);
                delay(1000);
                Serial.write(outFrame, frameLen);
                delay(500);
                i += msgLen;
                delPos = i; 
                delay(500);
            }else{
                if (i>0){
                    delPos = i-1;
                }
            }
        }
    }

    RxQ.Clear(delPos);
}


