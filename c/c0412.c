/***************c0412.c**************/
int main (void)
{
    int i, * pi = & i, * * ppi = & pi;
    * * ppi = 10086;					//S1
    * * ppi = * * ppi + 1;			//S2

    int j;
    pi = & j;						//S3
    * * ppi = 10010;					//S4

    int * pj = & j;
    ppi = & pj;						//S5
    ++ * * ppi;						//S6
}
