#include <cs50.h>
#include <stdio.h>
int main(void)
{
    char c = get_char("Answer: ");

    if (c == 'y' || c == 'Y')
    {
        printf("Yes, you are in\n");
    }
    else if (c == 'n' || c == 'N')
    {
        printf("No, you are out\n");
    }
    else
    {
        printf("sorry,bye");
    }
}