/*******************c0410.c******************/
int max (int a, int b)
{
    return a >= b ? a : b;
}

int main (void)
{
    int res, (* pf) (int, int) = max;
    void (* px) (void) = (void (*) (void)) pf;

    res = (int (*) (int, int)) px == pf ? 1 : 0;
    res = ((int (*) (int, int)) px) (1, 2);
}
