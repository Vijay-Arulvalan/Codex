#include <stdio.h>
#include <cs50.h>

int main()
{
    int j = get_int("X: ");
    int k = get_int("Y: ");
    printf(" %i plus %i is %i\n",j,k, j + k );
    printf(" %i minus %i is %i\n",j,k, j - k );
    printf(" %i multiply %i is %i\n",j,k, j * k );
    printf(" %i division %i is %i\n",j,k, j / k );
    printf(" remainder of %i divided by %i is %i\n",j,k, j % k );
}