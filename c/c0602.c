/******************c0602.c********************/
int write_string (char * s)
{
    int l = 0, r;

    for (char * p = s; * p ++ != '\0'; l ++) ;

    __asm__ (
                "mov eax, 0x4 \n\t"
                "mov ebx, 0x1 \n\t"
                "int 0x80 \n\t"
                : "=a" (r)
                : "c" (s), "d" (l)
              );

    return r;
}

char * ull_to_string (unsigned long long int n, char * s)
{
    int x = 0;
    char buf [20], * p = s;

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

    while (r) sum += r --;

    return sum;
}

int main (void)
{
    write_string ("1+2+3+...+1000=");

    char a [20];

    write_string (ull_to_string (cusum (1000), a));
    write_string ("\n");
}
