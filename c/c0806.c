/**********************c0806.c********************/
# include <stdio.h>
# include <limits.h>
# include <math.h>

int main (void)
{
    printf (":");

    long int m;
    scanf ("%ld", & m);

    if (m <= 1)
    {
        printf ("%ld is a invalid number.\n" \
                  "Must be a natural number more than 1 " \
                  "less than %ld.\n", m, LONG_MAX);
        return 0;
    }

    for (unsigned long x = 2; x <= sqrt (m); x ++)
        if (m % x == 0)
        {
            printf ("%ld is not a prime.\n", m);
            return 0;
        }

    printf ("%ld is a prime.\n", m);
}
