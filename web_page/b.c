#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
    int a,n;
    char c[40],//ca[]={-126,-96};//printf("%s",ca);
    ca[0]=-125;ca[1]=-65;
    /*char cc[330];
    cc[0]=-126;
    cc[1]=-96;
    for(n=0;n<160;n+=2){
        cc[n+2]=cc[n];
        cc[n+3]=cc[n+1]+1;
    }
    cc[n+2]='\0';
    printf("%s",cc);*/
    srand((unsigned)time(NULL));
    scanf("%s",c);//printf("%d %d %d %d",c[0],c[1],c[2],c[3]);
    for(n=0;c[n] != '\0';n+=1);//printf("%d\n",n);
    a=rand()%(n/2+1)*2;
    //printf("%d %d",ca[0],ca[1]);
    ca[1]=ca[1]+rand()%82;
    //printf(" %d %s\n",ca[1],ca);
    for(;a<=n;n-=2){
        c[n+2]=c[n];
        c[n+3]=c[n+1];
    }
    c[n+2]=ca[0];
    c[n+3]=ca[1];
    printf("%s\n",c);
}