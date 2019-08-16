/**************c0709.c**************/
# include <stdio.h>

void fdemo (void)
{
    printf ("The return type of the function %s is void.\n",
              __func__);
}

int main (void)
{
    (void) 500;
    (void) printf ("hello world.\n");
    fdemo ();
}
