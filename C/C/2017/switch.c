// switch for yes or no

#include <stdio.h>
#include <cs50.h>
int main(void)
{
    char c = get_char("Tell:"); 
    switch (c)
    {
        case 'y':
        case 'Y':
            printf("Yes\n");
            break;
        case 'n':
        case 'N':
            printf("No\n");
            break;
    }
}