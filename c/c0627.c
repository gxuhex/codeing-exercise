/*************************c0627.c************************/
# include <stdio.h>
# include <limits.h>

int main (void)
{
    if (sizeof (unsigned long) != sizeof (float))
        return printf ("unsigned long is not suitable here.\n");

    float f = 123.5f;

    # define N sizeof (float) * CHAR_BIT

    for (int x = 0; x < N; x ++)
        printf ("%lu", * (unsigned long *) & f << x >> N - 1);

    printf ("\n");
}
