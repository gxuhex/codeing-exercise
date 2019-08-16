/*************c0504.c************/
int main (void)
{
    int a [] = {1, 2, [199] = 8, [99] = 7}, b [] = {1, 2, 3};

    unsigned int siza = 0, sizb = 0, numa = 0, numb = 0;
    siza = sizeof a;						//S1
    sizb = sizeof b;						//S2
    numa = sizeof a / sizeof (int);		//S3
    numb = sizeof b / sizeof (int);		//S4
}
