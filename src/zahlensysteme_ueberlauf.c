#include <stdio.h>
#include <limits.h>

int main()
{
    int max_int = INT_MAX; // Maximum value for an int
    printf("Max int value: %d\n", max_int);

    int overflow = max_int + 1; // This will cause an overflow
    printf("After overflow: %d\n", overflow);

    return 0;
}