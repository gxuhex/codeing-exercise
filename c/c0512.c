/*************c0512.c**************/
int main (void)
{
    int a [] = {5, [7] = 7, [11] = 8}, b [sizeof a / sizeof (int)];

    for (int x = 0; x < sizeof a / sizeof (int); x ++)
        * (b + x) = * (a + x);

    char c = * ("Are you sure?" + 2);
}
