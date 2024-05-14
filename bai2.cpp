#include <stdio.h>
#include <math.h>
#include <stdbool.h>
 // Your code here!
// Hàm kiểm tra số chính phương
bool LaSoChinhPhuong(int x) {
    int sqrt_x = (int)sqrt(x);
    return (sqrt_x * sqrt_x == x);
}

// Hàm đếm và in ra các số chính phương nhỏ hơn n
void DemSoChinhPhuong(int n) {
    int count = 0;
    printf("Cac so chinh phuong nho hon %d la:\n", n);
    for (int i = 1; i < n; i++) {
        if (LaSoChinhPhuong(i)) {
            printf("%d ", i);
            count++;
        }
    }
    printf("\nTong so chinh phuong nho hon %d la: %d\n", n, count);
}

int main() {
    int n;
    printf("Nhap vao mot so nguyen duong n: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Vui long nhap mot so nguyen lon hon 0.\n");
        return 1;
    }

    DemSoChinhPhuong(n);

    return 0;
}