int main (void)
{
    unsigned long long int n, sum;

    n = 1;
    sum = 0;

    while (n <= 100)
    {
        sum = sum + n;
    	    n = n + 1;
    }

    return 0;
}
