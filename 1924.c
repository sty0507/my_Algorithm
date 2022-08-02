#include <stdio.h>
int month(int m){
	switch(m){
		case 1:
			return 31;
		case 2:
			return 28;
		case 3:
			return 31;
		case 4:
			return 30;
		case 5:
			return 31;
		case 6:
			return 30;
		case 7:
			return 31;
		case 8:
			return 31;
		case 9:
			return 30;
		case 10:
			return 31;
		case 11:
			return 30;
		case 12:
			return 31;
	}
}
int day(int dd){
	if(dd <= 7){
		return dd;
	}
	else day(dd-7);
}
int main(){
	int m, d, i;
	char *w[7] = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};
	int total_day = 0;
	scanf("%d %d", &m, &d);
	if(m == 1){
		printf("%s", w[day(d)-1]);
		return 0;
	}
	for(i= 1; i < m; i++){
		total_day += month(i);
	}
	total_day += d;
	printf("%s", w[day(total_day)-1]);
	return 0;
}

