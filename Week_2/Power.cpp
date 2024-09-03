#include "Power.h"

/*
* This problem can be done without recursion, making it
* much more efficient. Can you figure it out?
*/

double power(double base, int n){
	double val;

    // Base cases
    if (n == 0){
        val = 1;
    }
    else if (n == 1){
        val = base;
    }
    // Recursive steps 
    else if(n < 0){
        val = 1 / power(base, (-1) * n);
    }
    else{
        val = base * (base, n - 1);
    }

	return val;
}