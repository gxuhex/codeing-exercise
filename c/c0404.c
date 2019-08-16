/***********c0404.c***********/
char * swaprp (char * a, char * b)
{
    char temp = * a;
    * a = * b;
    * b = temp;

    return * a > * b ? a : b;
}

int main (void)
{
    char m = 102, n = 103, * pc;

    pc = swaprp (& m, & n);
}
