import http.requests.*;

import processing.serial.*; //import serial communication classes

import cc.arduino.*; //import Arduino classes

Arduino arduino;
int buttonPin = 2;
int oldstate;
int currentstate;

int currentChoice = 1; // entre 1 et numberOfChoice.
int numberOfChoice = 3;

int potentioMax = 1023;
int potentioMin = 0;

//declare an Arduino object


void setup() {
  size(800, 600);
  arduino = new Arduino(this, Arduino.list()[0], 57600); //instanciate own Arduino object // COM port number and baudrate
  arduino.pinMode(buttonPin, Arduino.INPUT);
  oldstate = 0;
  
}

void draw() {
  float value = map(arduino.analogRead(0),potentioMin,potentioMax,0,1);
  currentChoice = findSelection(value);
 // println(value+","+currentChoice);
  
  currentstate = arduino.digitalRead(buttonPin);
  if(currentstate == 0 && oldstate == 1)
  {
    click();
    debugPrint();
  }
  oldstate = currentstate;

}

void click() {
  GetRequest req;
  switch(currentChoice){
    case 1:
     // req = new GetRequest("http://192.168.97.222:8082/");
      req = new GetRequest("http://localhost:8082/");
      req.send();
      break;
    case 2:
      //req = new GetRequest("http://192.168.97.222:8082/buy/raptor");
      req = new GetRequest("http://localhost:8082/buy/raptor");
      req.send();
      break;
    case 3:
     // req = new GetRequest("http://192.168.97.222:8082/buy/autobus");
      req = new GetRequest("http://localhost:8082/buy/autobus");
      req.send();
      break;
    default:
      break;
     
  }
  println(currentChoice);
}

int findSelection(float value){
  int i = 0;
  if(value == 1){
    return numberOfChoice;
  }
  while(value >= (float)i/numberOfChoice){
    i++;
  }
  return i;
}

void debugPrint() {
  println("click");
}
  
