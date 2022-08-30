#include <stdio.h>

int n;
int direction[6 + 2][2 + 2];
int cnt[4];

int main() {
    
    int s = 1;
    int b = 1;

    scanf("%d", &n);
    for (int i = 0; i < 6; i++) {
        scanf("%d %d", &direction[i][0], &direction[i][1]);
        cnt[direction[i][0]]++;
    }

    for (int i = 0; i < 6; i++) {

        if (cnt[direction[i][0]] == 1) {
            b *= direction[i][1]; 
            continue;
        }

        int n = (i + 1) % 6;
        int nn = (i + 2) % 6;
        if (direction[i][0] == direction[nn][0]) s *= direction[n][1];
    }

    printf("%d", (b - s) * n);

    return 0;
}

