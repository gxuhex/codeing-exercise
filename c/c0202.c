/*******************c0202.c******************/
unsigned long long int cusum (unsigned long long int r)
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

/*从现在开始，为节省篇幅、节约纸张，main函数一律不再包含末尾的return 0;语句，
但请确保你的C实现支持C99（噢，很少有不支持的了）。*/

int main (void)
{
    unsigned long long int x, y, z;

    x = cusum (10);
    y = cusum (100);
    z = cusum (1000);
}	//此函数没有return语句，程序执行到此花括号时，如同执行了return 0;
