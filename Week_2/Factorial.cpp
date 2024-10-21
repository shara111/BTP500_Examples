#include "./Factorial.h"

// Note: recursion is one of those times where we can break the
// one entry, one exit principle.
int factorial(int num){
    // This is what we call a base case.
    // A base case is the "default behaviour" of a function
    // This has to happen at some point to break out of the "loop"
    if(num <= 1){
        return 1;
    }
    // This is the recursive step. The step that calls the function
    // internally is where it becomes recursive.
    else{
        return num * (factorial(num - 1)); 
    }
}

int main(){
    printf("The factorial of 10 is: %d\n", factorial(10));
    return 0;
}

