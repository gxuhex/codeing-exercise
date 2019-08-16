/*****************c0607.c****************/
# include <stdarg.h>

typedef long long int VARF (unsigned int, ...);

int main (void)
{
    long long int x, y, z, m, n;

    VARF sum_ints;
    x = sum_ints (2, 100, 200);
    y = sum_ints (0);
    z = sum_ints (5, 10, -10, 30, 600, -300);
}

long long int sum_ints (unsigned int count, ...)
{
    long long int sum = 0;

    va_list ap;
    va_start(ap, count);
    while (count --) sum += va_arg(ap, int);
    va_end(ap);

    return sum;
}
