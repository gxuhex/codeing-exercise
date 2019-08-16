/***********c0409.c**********/
int main (void)
{
    int m = 0;
    unsigned long long int ull;

    ull = (unsigned long long) & m;
    * (int *) ull = 10086;
}
