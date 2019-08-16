/*********************c0619.c******************/
# include <stdio.h>

int main (void)
{
    FILE * hfile = fopen ("myfile5.txt", "w");
    if (hfile == NULL) return -1;

    char * ps = "By\nthe\nriver\nof\nBabylon\n";

    do
        if (* ps == '\0') break;
    while (fputc (* ps ++, hfile) != EOF);

    fclose (hfile);
}
