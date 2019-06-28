#include <stdio.h>
#include <cs50.h>

int main(void)
{
    double x = get_double ("x:");
    double y = get_double ("y:");
    printf ("x div y is %.50f\n", x / y);
}