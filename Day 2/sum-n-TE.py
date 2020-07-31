/*Sum of n natural numbers*/

#include<stdio.h>
int main()
{

int n1,sum;
printf("Enter number: ");
scanf("%d", &n1);
sum = fun1(n1);
printf("sum = %d\n",sum);

}

int fun1(int n)
{
  return n*(n+1)/2;
}
