/*****************c0606.c*****************/
long long int sum_ints (unsigned int count, ...)
{
    int * var_start = (int *) & count + 1;
    long long int sum = 0;

    while (count --) sum += * var_start ++;

    return sum;
}

int main (void)
{
    long long int x, y, z;

    x = sum_ints (2, 100, 200);
    y = sum_ints (0);
    z = sum_ints (5, 10, -10, 30, 600, -300);
}
