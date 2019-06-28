#include <stdio.h>
#include <cs50.h>

int main()
{
    char c = get_char("Answer: ");

    if (c == 'Y'|| c == 'y')
    {
        printf("yes\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("No\n");
    }

}