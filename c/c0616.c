/***********************c0616.c**********************/
# include <windows.h>

# define MSG0 "Playing......\n"
# define MSG1 "Finished.\n"

int main (void)
{
    WriteFile (GetStdHandle (STD_OUTPUT_HANDLE), MSG0, \
                 lstrlen (MSG0), (DWORD []) {0}, NULL);

    PlaySound ("zmtx.wav", NULL, SND_FILENAME | SND_SYNC);

    WriteFile (GetStdHandle (STD_OUTPUT_HANDLE), MSG1, \
                 lstrlen (MSG1), (DWORD []) {0}, NULL);
}
