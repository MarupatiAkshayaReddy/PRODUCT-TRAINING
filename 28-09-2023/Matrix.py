#include<stdio.h>
int main()
{
	int n,i,j,hc1=0,vc1=0,ld1=0,rd1=0;
	int hc0=0,vc0=0,ld0=0,rd0=0,flag;
	printf("enter n value:");
    scanf("%d",&n);
    int m[n][n];
    for(i=0;i<n;i++)
    {
    	for(j=0;j<n;j++)
    	{
    		scanf("%d",&m[i][j]);
		}
	}
	printf("\n");
	for(i=0;i<n;i++)
    {
    	for(j=0;j<n;j++)
    	{
    		printf("%d\t",m[i][j]);
		}
		printf("\n");
	}
	
	for(i=0;i<n;i++)
	{
		flag=0;
		for(j=0;j<n;j++)
		{
			if(m[i][j]==1)
			    flag++;
		}
		if(flag==n)
		    hc1++;
	}
	
	for(i=0;i<n;i++)
	{
		flag=0;
		for(j=0;j<n;j++)
		{
			if(m[j][i]==1)
			    flag++;
		}
		if(flag==n)
		   vc1++;
	}
	
	flag=0;
	for(i=0,j=n-1;(i<n && j>=0);i++,j--)
	{
			if(m[i][j]==1)
			{
			    flag++;
			}
	}
	if(flag==n)
	  rd1++;
	  
	flag=0;
	for(i=0,j=0;(i<n && j<n);i++,j++)
	{
			if(m[i][j]==1)
			{
				flag++;
			}
	}
	if(flag==n)
	  ld1++;
	
	
	for(i=0;i<n;i++)
	{
		flag=0;
		for(j=0;j<n;j++)
		{
			if(m[i][j]==0)
			    flag++;
		}
		if(flag==n)
		    hc0++;
	}
	
	for(i=0;i<n;i++)
	{
		flag=0;
		for(j=0;j<n;j++)
		{
			if(m[j][i]==0)
			    flag++;
		}
		if(flag==n)
		   vc0++;
	}
	
	flag=0;
	for(i=0,j=n-1;(i<n && j>=0);i++,j--)
	{
			if(m[i][j]==0)
			{
			    flag++;
			}
	}
	if(flag==n)
	  rd0++;
	  
	flag=0;
	for(i=0,j=0;(i<n && j<n);i++,j++)
	{
			if(m[i][j]==0)
			{
				flag++;
			}
	}
	if(flag==n)
	  ld0++;
		
	printf("1`s horizontal count=%d\n",hc1);
	printf("1`s vertical count=%d\n",vc1);
	printf("1`s left diagonal count=%d\n",ld1);
	printf("1`s right diagonal count=%d\n",rd1);
	
	printf("0`s horizontal count=%d\n",hc0);
	printf("0`s vertical count=%d\n",vc0);
	printf("0`s left diagonal count=%d\n",ld0);
	printf("0`s right diagonal count=%d",rd0);
	
}
