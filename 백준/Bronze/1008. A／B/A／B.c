#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void)
{
    double A, B;
    scanf("%lf %lf",&A,&B);
    printf("%0.9lf\n", A/B);
    return 0;
}