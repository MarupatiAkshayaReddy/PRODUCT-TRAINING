/*smallest number greater than 'n' with exactly 1 bit diff in binary form*/
#include<stdio.h>
int main()
{
	int n;
	scanf("%d",&n);
	printf("%d",n|n+1);
}
