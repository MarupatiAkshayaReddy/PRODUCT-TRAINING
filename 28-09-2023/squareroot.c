#include<stdio.h>
int main()
{
	int i;
	for(i=1;i<=10;i++)
	{
		if(i*i>=40 && i*i<=100)
		{
			printf("%d\n",i);
		}
	}
}
