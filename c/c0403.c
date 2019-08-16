/*****************c0403.c***************/
void swap_ab (int * a, int * b)
{
    int temp = * b;

    * b = * a;
    * a = temp;
}

int main (void)
{
    int m = 10086, n = 10010;

    swap_ab (& m, & n);

    void (* pf) (int *, int *) = swap_ab;
    pf (& m, & n);
}
