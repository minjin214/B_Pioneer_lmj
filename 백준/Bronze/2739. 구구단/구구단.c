#include <stdio.h>
int main(void)
{
    int N;
    int j=0;
    scanf("%d",&N);
    while (j<9)
    {
        j++;
        printf("%d * %d = %d\n",N,j,N*j);
    }
    return 0;
}