#include<stdio.h>
int main()
{
	int n;
	scanf("%d",&n);
	if(n&1)//based on boolean values it is working or we can also write in if(n&1==1) also
	   printf("odd");
	else
	   printf("even");
}
