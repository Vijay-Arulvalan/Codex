#include <stdio.h>
#include <cs50.h>

int main()
{
    float j = get_float("X: ");
    float k = get_float("Y: ");
    printf(" %f plus %f is %f\n",j,k, j + k );
    printf(" %f minus %f is %f\n",j,k, j - k );
    printf(" %f multiply %f is %f\n",j,k, j * k );
    printf(" %f division %f is %f\n",j,k, j / k );
}