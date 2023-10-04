#include<stdio.h>
void main()
{
    int n,c=0;
    scanf("%d",&n);
    /*if(n==1 || n<0)
    {
        printf("not power of 2");
    }
    else if(n&n-1)//for power of 4 the condition is n&n-2 remaining is same
    {
        printf("not power of 2");
    }
    else
    {
        printf("power of 2");
    }*/
    while(n)
    {
    	c++;
    	n=n&(n-1);//power of 4 n=n&(n-2)
	}
	if(c==1)
	  printf("true");
	else
	  printf("false");
}
