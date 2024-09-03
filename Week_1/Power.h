#ifndef POWER_H
#define POWER_H

#include <iostream>

/*
* Another example of a recursive function;
* as you are aware, placing the base number
* to a power, n, can take a self referential 
* definition!

* base ^ n = base * base * base * .... * base 
* for as many n times as necessary.
*/

double power(double base, int n);


#endif