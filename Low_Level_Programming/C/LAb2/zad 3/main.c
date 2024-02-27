#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,i,sum,parz,ilocz;
    float sr;
    a=0;
    i=0;
    parz=0;
    sum=0;
    ilocz=1;
    printf("Program wczytujacy z klawiatury liczby calkowite az do pojawienia sie pierwszej liczby < 0.\n Program powinien obliczac i wypisywac srednia arytmetyczna wczytanych liczb > 0,\n iloczyn wczytanych liczb spoza przedzialu [5, 10] oraz ilosc wczytanych liczb parzystych.\n");

    while(a>=0){
        i=i+1;
        printf("\nPodaj liczbe calkowita: ");
        scanf("%d",&a);

        if(a>=0){
            sum=sum+a;
            printf("Suma wszystkich liczb to %d\n",sum);
            sr=(float)sum/i;
            printf ("Srednia wszystkich liczb to %f\n",sr);

            if(a<5||a>10){
                ilocz=ilocz*a;
                printf("iloczyn liczb spoza przedzialu [5,10] wynosi %d\n",ilocz);
            }

            if (a%2==0){
                parz=parz+1;
                printf("iloac liczb parzystych: %d\n",parz);
            }

        }
    }

    system("pause");
    return 0;
}
