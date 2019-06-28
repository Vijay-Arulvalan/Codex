#include <cs50.h>
#include <stdio.h>
int main(int argc, string argv[])
{
    if(argc == 2) //argc is argument count, argv is argument vector
    {
        printf("Hello, %s\n", argv[1]);
    }
    else
    {
        printf("Hello, world\n");
    }
}