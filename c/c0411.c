/************c0411.c**********/
int main (void)
{
    unsigned long long x, y, z;
    x = _Alignof (char);
    y = _Alignof (char *);
    z = _Alignof (int (*) (void));
}
