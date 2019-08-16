/**********************c0630.c*********************/
# define __USE_MINGW_ANSI_STDIO 1
# include <stdio.h>

int main (void)
{
    char a [6];
    int b;
    long long int c;

    fscanf (stdin, "%5s%3d%6lld", a, & b, & c);
    fprintf (stdout, "%s,%d,%lld.\n", a, b, c);
}
