/*****************c0301.c******************/
unsigned long long int cusum (unsigned long long int r)
{
    unsigned long long int n = 1, sum = 0;

    while (n <= r)
    {
        sum = sum + n;
        n = n + 1;
    }

    return sum;
}

int main (void)
{
    unsigned long long int res = cusum (1000);
}
