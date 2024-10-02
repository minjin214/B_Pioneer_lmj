#include <stdio.h>
int main(void)
{
    int N;
    int i=0,j=0;

    scanf("%d",&N);
    while(i<N)
    {
        ++i;
        while(j<i)
        {
            printf("*");
            ++j;
        }
        j=0;
        printf("\n");
    }
    return 0;
}