#include <stdio.h>
#include <cs50.h>

void cough (void);

int main(void)
{
    cough(3);
}

void cough (int n)
{
    for(int i=0; i<3; i++)
    {
         printf ("cough\n");
    }

}