#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int n,i;
    double a3,a2,a1,ai,sum;
    a3=2; //-1 czyli 0
    a2=1.5; //-2 czyli -1
    a1=1; //-3 czyli -2
    sum=0;
    printf("Ehej!\n");
    scanf("%d",&n);

    for(i=1;i<=n;i++){
        ai=a3*sqrt(a2+a1);
        sum=sum+ai;
        a3=a2;
        a2=a1;
        a1=ai;
    }

    printf("suma wynosi %f\n",sum);
    return 0;
}
