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

/*�����ڿ�ʼ��Ϊ��ʡƪ������Լֽ�ţ�main����һ�ɲ��ٰ���ĩβ��return 0;��䣬
����ȷ�����Cʵ��֧��C99���ޣ������в�֧�ֵ��ˣ���*/

int main (void)
{
    unsigned long long int x, y, z;

    x = cusum (10);
    y = cusum (100);
    z = cusum (1000);
}	//�˺���û��return��䣬����ִ�е��˻�����ʱ����ִͬ����return 0;
