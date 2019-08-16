/******************c0621.c*****************/
# include <stdio.h>

int main (void)
{
    FILE * hfile = fopen ("myfile5.txt", "r");
    if (hfile == NULL) return -1;

    char buf [BUFSIZ];

    while (fgets (buf, BUFSIZ, hfile) != NULL)
        fputs (buf, stdout);

    fclose (hfile);
}
