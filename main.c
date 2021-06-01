#include <stdio.h>
#include <conio.h>

int main(){
    int n,num01, num02, result;

    char option;
    do{
    printf("\nZgjidhni operator:\n");
    printf("Shtyp #1 per +\n");
    printf("Shtyp #2 per -\n");
    printf("Shtyp #3 per *\n");
    printf("Shtyp #4 per /\n");

    scanf("%d",&n);

    printf("Vendosni nje numer:\n");

    scanf("%d",&num01);

    printf("Vendosni numrin e dyte:\n");

    scanf("%d",&num02);

    switch(n) {
        case 1:
            result = num01 + num02;
            printf("mbledhje = %d\n", result);
            break;
        case 2:
            result = num01 - num02;
            printf("zbritje = %d\n", result);
            break;
        case 3:
            result = num01 * num02;
            printf("shumezim = %d\n", result);
            break;
        case 4:
            result = num01 / num02;
            printf("pjestim = %d\n", result);
            break;
        default:
            printf("Wrong input");
        }
        printf("Deshironi te vazhdoni y/n?\n");
        option = getche();
    }while(option == 'y');

    return 0;
}
