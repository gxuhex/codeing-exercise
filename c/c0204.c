/****************c0204.c****************/
unsigned long long int cusum ();		//D1

main ()									//D2
{
    unsigned long long int x, y, z;

    x = cusum (10);
    y = cusum (100);
    z = cusum (1000, 1200);				//S1

    return 0;
}

unsigned long long int cusum (r)		//D3
unsigned long long int r;				//D4
{
    unsigned long long int n, sum;

    n = 1;
    sum = 0;

    while (n <= r)
    {
        sum = sum + n;
        n = n + 1;
    }

    return sum;
}
