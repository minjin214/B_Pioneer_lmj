#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void)
{
    int A,B;
    long int a,b,c;
    long int x,y,z;
    scanf("%d",&A);
    scanf("%d",&B);

    a = B%10;
    b = (B/10)%10;
    c = B/100;

    x = A*a;
    y = A*b;
    z = A*c;
    printf("%ld\n%ld\n%ld\n%ld",x,y,z,z*100+y*10+x);

    return 0;

}