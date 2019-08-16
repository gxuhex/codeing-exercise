/************************c0615.c**********************/
# include <windows.h>

# define PROMPT "->"

int main (void)
{
    HANDLE stdi = GetStdHandle (STD_INPUT_HANDLE);
    HANDLE stdo = GetStdHandle (STD_OUTPUT_HANDLE);
    char buf [1];
    DWORD nbread, nbwrite;

    WriteFile (stdo, PROMPT, lstrlen (PROMPT), & nbwrite, NULL);

    while (ReadFile (stdi, buf, sizeof buf, & nbread, NULL) &&
                        (nbread != 0))
        WriteFile (stdo, buf, nbread, & nbwrite, NULL);
}
