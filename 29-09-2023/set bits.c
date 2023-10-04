#include<stdio.h>
int main()
{
	int n;
	int r,c=0;
	scanf("%d",&n);
	/*if(n>0)
	{
		while(n>0)
		{
			r=n%2;
			if(r==1)
			  c++;
			n=n/2;
		}
	}
	else
	{
		while(n<0)
		{
			r=n%2;
			if(r==1)
			  c++;
			n=n/2;
		}
	}*/
/*	while(n)
	{
		c++;
		n=n&(n-1);
	}*/
	while(n>0)
	{
		if(n&1)
		  c++;
		n=n>>1;
	}
	printf("%d",c);
}
