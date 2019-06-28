#include <cs50.h>
#include <stdio.h>

int main (void)
{
    string x = get_string ("name: ");
    string y = get_string ("age: ");
    printf ("hello, %s\n" ,x);
    printf ("You are %s\n",y);
}
