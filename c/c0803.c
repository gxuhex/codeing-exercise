/****************c0803.c***************/
# include <stdio.h>

int main (void)
{
    union u {
        unsigned char a [sizeof (float)];
        float f;
    } ud = {.f = 123.5f};

    for (size_t m = 0; m < sizeof (float); m ++)
        printf ("%0.2X  ", ud . a [m]);

    printf ("\n");
}
