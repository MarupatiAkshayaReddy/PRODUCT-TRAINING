/*find the 1 missing number in an 'n' array*/
#include<stdio.h>
int main()
{
	int n,c=0;
	scanf("%d",&n);
	int a[n],i,j=0;
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	j=j^i;
	for(i=0;i<n-1;i++)
	j=j^a[i];
	printf("%d",j);
}
