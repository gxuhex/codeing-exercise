/**********************c0626.c*********************/
# define __USE_MINGW_ANSI_STDIO 1
# include <stdio.h>

int main (void)
{
    fprintf (stdout, "%+11.5lld%-11.2Lf%011f\n", \
                                385LL, -6.25777L, -3.25);
    fprintf (stdout, "-----------+++++++++++-----------\n");
}
