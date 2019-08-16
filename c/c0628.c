/***********************c0628.c*********************/
# define __USE_MINGW_ANSI_STDIO 1
# include <stdio.h>

int main (void)
{
    unsigned long long n, t, sum = 0;

    printf ("A number less or equal 1,000,000,000:");

    fscanf (stdin, "%llu", & n), t = n;
    while (n) sum += n --;

    printf ("1+2+3+...+%llu=%llu\n", t, sum);
}
