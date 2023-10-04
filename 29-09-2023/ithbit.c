/*check the ith bit is set or not
  set means ith bit from right is 1 or not
  
  1011--->11  ith bit 3
  0100-->1<<2
  0---->0
  
  1111---->15
  1000--->1<<3
  8---->8
  */
  
#include<stdio.h>
int main()
{
	int n,pos;
	scanf("%d",&n);
	scanf("%d",&pos);
	
	//printf("%d",n&(1<<(pos-1)));
	if(n&(1<<(pos-1)))
	  printf("yes");
	else
	  printf("no");
}
