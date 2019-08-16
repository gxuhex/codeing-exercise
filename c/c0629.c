/**********************c0629.c*********************/
# include <stdio.h>

int main (void)
{
    char a [100], c;
    int d;
    unsigned int i, o, u, x;

    fscanf (stdin, "GBT%s%d%c%i-%o,%u,,%x",\
                      a, & d, & c, & i, & o, & u, & x);
    printf ("a=%s\nd=%d\nc=%c\ni=%i\no=%o\nu=%u\nx=%x\n",\
                                    a, d, c, i, o, u, x);
}
