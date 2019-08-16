/****************c0804.c***************/
# include <stdio.h>

void main (void)
{
    union u {int i; char c [21];};
    printf ("%zu, %zu\n", sizeof (union u), _Alignof (union u));
}
