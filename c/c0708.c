/*********************c0708.c******************/
# include <stdio.h>

# define DEBUG 1

# if DEBUG
# define prn_code(exp) printf ("%d\n", exp)
# else
# define prn_code(exp) (void) (exp);
# endif

int main (void)
{
    int ret = printf ("Let us then begin with it.\n");
    prn_code(ret);

    ret = printf ("岂有此理！你怎么不早说！\n");
    prn_code(ret);
}
