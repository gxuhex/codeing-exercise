/**************c0516.c*************/
int fsum (int (* pints) [5])
{
    int sum = 0;

    for (unsigned x = 0; x < sizeof * pints / sizeof (int); x ++)
        sum += (* pints) [x];

    return sum;
}

int main (void)
{
    int a [] = {3, 10, -5, 6, 22}, r;
    r = fsum (& a);
}
