/**********************c0614.c**********************/
# include <windows.h>

# define PSTR "Jace,Jack,Jackie,Jackson,Jacob,Jacque.\n"

int main (void)
{
    WriteFile (GetStdHandle (STD_OUTPUT_HANDLE), PSTR, \
                 lstrlen (PSTR), (DWORD []) {0}, NULL);
}
