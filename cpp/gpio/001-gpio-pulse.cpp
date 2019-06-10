#include<iostream>
#include<unistd.h>
#include "GPIO.h"

using namespace exploringRPI;
using namespace std;

int main() {
    GPIO outGPIO(17), inGPIO(27);       // Pin 11 and 13
    for (int i=0; i<10; i++) {          // Pulse the pin 10 times
        outGPIO.setValue(HIGH);         // Set pin ON/HIGH
        usleep(500000);                 // Sleep for 0.5 seconds
        outGPIO.setValue(LOW);          // Set pin OFF/LOW
        usleep(500000);                 // Sleep again
    }

    /* */
    inGPIO.setDirection(INPUT);         // input example
    cout << "Input state: " << inGPIO.getValue() << endl;

    outGPIO.streamOpen();               // fast write example
    for (int i=0; i<1000000; i++) {     // 1 million writes
        outGPIO.streamWrite(HIGH);      // high
        outGPIO.streamWrite(LOW);       // immediately low, repeat
    }
    outGPIO.streamClose();              // close the stream
    return 0;
}
