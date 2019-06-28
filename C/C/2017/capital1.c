#include <cs50.h>
#include <stdio.h>
#include <string.h>// strlen(s)
#include <ctype.h>// toupper and tolower
int main(void)
{
    string s = get_string("Before: ");
    printf ("After: \n");
    for (int i=0, n = strlen(s); i < n; i++)
    {
        printf("%c\n", toupper (s[i]));
    }
}