#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float x = get_float ("x:");
    float y = get_float ("y:");
    printf ("x div y is %.50f\n", x / y); //.50 in between the placeholder is to get 7 decimal points in output//
}