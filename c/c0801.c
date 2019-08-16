/***************c0801.c**************/
# include <stdio.h>

enum Op {ADD, SUB, MUL, DIV, MOD, MAX};

int compu (int x, int y, enum Op op)
{
    if (op == ADD) return x + y;
    if (op == SUB) return x - y;
    if (op == MUL) return x * y;
    if (op == DIV) return x / y;
    if (op == MOD) return x % y;
    if (op == MAX) return x > y ? x : y;

    printf ("Illegal operator.\n");
    return 0;
}

int main (void)
{
    enum Op opr = MUL;
    printf ("%d\n", compu (2, 5, opr));

    printf ("%d\n", compu (3, 6, MOD));
    printf ("%d\n", compu (6, 7, 19));
}
