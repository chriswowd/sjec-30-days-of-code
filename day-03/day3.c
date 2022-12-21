#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n,num;
    scanf("%d \n",&n);
    int a[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    float avg=0;
    int sum;
    for(int i=0;i<n;i++)
    {
        sum+=a[i];
    }
    avg=sum/n;
    for(int i=0;i<n;i++)
    {
        if(a[i]>avg)
        printf("%d ",a[i]);
    }
}