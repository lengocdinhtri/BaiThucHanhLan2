#include <stdio.h>
int main(void){
    // Your code here!
    printf("Cac so nguyen co 2 chu so va la boi cua 7 la:\n");
    for (int i = 10; i <= 99; i++) {
        if (i % 7 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}