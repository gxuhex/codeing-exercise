/********************c0805.c*******************/
# include <stdio.h>
# include <complex.h>

int main (void)
{
    double _Complex d = 3.0 + 2.0i;

    d += 5.0 + 1.0i;
    printf ("%.1f%+.1fi\n", creal (d), cimag (d));

    d = csqrt (d);
    printf ("%.1f%+.1fi\n", creal (d), cimag (d));

    d = csin (d);
    printf ("%.1f%+.1fi\n", creal (d), cimag (d));
}
