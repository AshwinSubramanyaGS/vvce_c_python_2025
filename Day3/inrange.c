#include<stdio.h>

int main(){
    char *s="!@#$%^&*()-+";
    for(int i=0;s[i]!='\0';i++)
    {
        printf("\n%c - %d",s[i],s[i]);
    }
    return 0;
}