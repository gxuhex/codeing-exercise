/*******************c0704.c******************/
# include <stdio.h>

int main (void)
{
    float f = 123.5f;

    for (size_t m = 0; m < sizeof (float); m ++)
        printf ("%02X ", ((unsigned char *) & f) [m]);

    printf ("\n");
}
