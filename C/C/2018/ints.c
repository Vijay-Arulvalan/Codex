#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int ("X:");
    int y = get_int ("y:");
    printf ("x + y is %i\n",x + y);
    printf ("x - y is %i\n",x - y);
    printf ("x * y is %i\n",x % y);
    printf ("x / y is %i\n",x / y);
    printf ("x mod of y is %i\n",x % y);
}