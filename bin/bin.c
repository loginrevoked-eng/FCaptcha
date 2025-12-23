#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    system("calc");
    if(argc>2){
        printf("the detonate timer is %s",argv[1]);
    }
    printf("Programs name is %s\n",argv[1]);
    system("cmd");
    return 0;
}
