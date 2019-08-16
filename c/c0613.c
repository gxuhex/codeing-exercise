/**********************c0613.c*********************/
# include <windows.h>

int main (void)
{
    HANDLE hstdo = CreateFile ("CONOUT$", GENERIC_WRITE, 0, \
                                     NULL, OPEN_ALWAYS,\
                                     FILE_ATTRIBUTE_NORMAL, NULL);
    char buf [] = "Hello world.\n";
    WriteFile (hstdo, buf, lstrlen (buf), (DWORD []) {0}, NULL);
}
