#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        long int n,j=0,k=0,m,i; 
        scanf("%ld",&n);
        for(i=1;i<=n;i++)
        {
            j=j+i;
            k=k+(i*i);
        }
        m=j*j;
        printf("%ld \n",m-k);
    }
    return 0;
}