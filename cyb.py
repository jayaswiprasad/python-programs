#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    char str[1001];
    int l,i,j;
    scanf("%s",str);
    l=strlen(str);
    for(i=0;i<l;i++)
    {
        for(j=i+1;j<l;j++)
        {
            if(str[i]>str[j])
            {
                char temp=str[i];
                str[i]=str[j];
                str[j]=temp;
            }
        }
    }
    int k,flag=0;
    for(k=0;k<l;k++)
    {
        if(str[k]!=str[k+1])
        {
            flag=1;
            printf("%c",str[k]);
        }
        else
        {
            flag=0;
        }
    }
    if(flag==0)
    {
        printf("%c",str[l-1]);
    }
    return 0;

}
