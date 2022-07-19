#include <stdio.h>

int main() {
    int H = 0, M = 10;
    scanf("%d %d", &H, &M);
    printf("%d %d\n", H, (M-45)%60);
}