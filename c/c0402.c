/**********c0402.c********/
int main (void)
{
    int x, * p = & x, * q;

    q = & x;
    * p = 1;
    x = * p + * q;
}
