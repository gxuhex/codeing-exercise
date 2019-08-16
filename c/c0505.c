/***************c0505.c***************/
unsigned int var_arr (int n)
{
    signed char va [n];

    return sizeof va;						//S1
}

int main (void)
{
    unsigned int n = 30, siz = sizeof 0;	//D1

    signed char c = 0;
    siz = sizeof (c = 1);					//S2

    siz = sizeof (int [30]);				//S3
    siz = var_arr (n);						//S4
    siz = sizeof (int [++ n]);				//S5

    siz = sizeof sizeof c;					//S6
}
