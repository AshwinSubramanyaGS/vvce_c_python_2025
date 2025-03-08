#include <stdio.h>
int main()
{
    int n=98;
    char ch;
    //scanf("%c%d",&ch,&n);
    switch(n){
        case 98: printf("We are in case 99\n");
                break;
        case 'c': printf("We are in case \'c\'\n");
                break;
        case '@': printf("We are in case @\n");
                break;
        case '&': printf("We are in case &\n");
                break;
        case ':': printf("We are in case :\n");
                break;
    }


    return 0;
}