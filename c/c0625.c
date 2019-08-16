/*********************c0625.c********************/
# include <stdio.h>

int main (void)
{
    float fa [] = {.7, 9., 3e2, 2.2e+0, 0x3.5fp2};

    for (int x = 0; x < sizeof fa / sizeof (float); x ++)
        fprintf (stdout, "fa[%d]=%f\n", x, fa [x]);
}
