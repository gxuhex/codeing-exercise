/*********************c0617.c********************/
# include <windows.h>

int main (int argc, char * * argv)
{
    HANDLE stdo = GetStdHandle (STD_OUTPUT_HANDLE);
    DWORD bwritten [1];

    for (int n = 0; n < argc; n ++)
    {
        WriteFile (stdo, argv [n],\
                   lstrlen (argv [n]), bwritten, NULL);
        WriteFile (stdo, "\n", 1, bwritten, NULL);
    }
}
