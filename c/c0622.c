/***************c0622.c**************/
# include <stdio.h>

int main (void)
{
    setvbuf (stdin, NULL, _IONBF, 0);

    int c;

    while ((c = fgetc (stdin)) != EOF)
        fputc (c, stdout);
}
