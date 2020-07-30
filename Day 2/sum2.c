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
  int sum = 0;
  for(int i = 1; i<=n; i++)
    for(int j = 1; j<=i; j++)
        sum++;
      return sum;
}
