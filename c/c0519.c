/**********************c0519.c**********************/
int f_add (int x, int y)
{
    return x + y;
}

int f_sub (int x, int y)
{
    return x - y;
}

int f_mul (int x, int y)
{
    return x * y;
}

int f_div (int x, int y)
{
    return x / y;
}

int f_mod (int x, int y)
{
    return x % y;
}

int f_max (int x, int y)
{
    return x > y ? x : y;
}

int f_min (int x, int y)
{
    return x < y ? x : y;
}

int f_avg (int x, int y)
{
    return (x + y) / 2;
}

int main (void)
{
    int (* af []) (int, int) = {f_add, f_sub, f_mul, f_div,\
                                    	  f_mod, f_max, f_min, f_avg},\
                  r [sizeof af / sizeof (int (*) (int, int))];

    for (unsigned n = 0; n < sizeof r / sizeof (int); n ++)
        r [n] = af [n] (8, 6);
}
