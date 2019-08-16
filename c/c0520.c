/*********************c0520.c********************/
char * ull_to_string (unsigned long long int n, char * s)
{
    int x = 0;
    char buf [22], * p = s;

    do
        buf [x ++] = n % 10 + '0';
    while (n /= 10);

    do
        * p ++ = buf [-- x];
    while (x);

    * p = '\0';

    return s;
}

unsigned long long int cusum (unsigned long long r)
{
    unsigned long long int sum = 0;

    for (unsigned long long int x = 1; x <= r; x ++)
        sum += x;

    return sum;
}

int main (void)
{
    char a [22], * ps = ull_to_string (cusum (1000), a);
}
