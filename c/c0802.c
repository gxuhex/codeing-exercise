/***********c0802.c***********/
# include <stdio.h>

# define prn(s) printf ("Type int is simular with %s.\n", s);

int main (void)
{
    switch (sizeof (int))
    {
        case sizeof (short int):
            prn ("short int");
            break;
        case sizeof (long int):
            prn ("long int");
            break;
        default:
            prn ("other type");
    }
}
