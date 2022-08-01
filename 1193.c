#include <stdio.h>
int main() {
	int n;
	scanf("%d", &n);
	int k = 1;
	while (1)
	{		
		if ((k-1)*(k)/2 < n && n <= (k)*(k+1)/2)
		{
			break;
		}
		k++;
	}

	if (k % 2 == 1) // È¦¼öÀÏ ¶§
	{
		int a = k*(k + 1) / 2;
		printf("%d", a-n + 1);
		printf("/");
		printf("%d", k -(a -n));
	}
	else //Â¦¼ö ÀÏ ¶§
	{
		int a = k * (k + 1) / 2;
		printf("%d",k-(a-n));
		printf("/");
		printf("%d",a-n + 1);
	}
	return 0;
}
