/*********************c0618.c********************/
# include <windows.h>

# define ERRPAR "Usage: sndplay file-name.\n"
# define STARTP "Playing......\n"
# define ENDPLY "Finished.\n"

int main (int argc, char * * argv)
{
    HANDLE stdo = GetStdHandle (STD_OUTPUT_HANDLE);
    DWORD bwritten [1];

    if (argc < 2)
    {
        WriteFile (stdo, ERRPAR, lstrlen (ERRPAR), bwritten, NULL);
        return -1;
    }

    WriteFile (stdo, STARTP, lstrlen (STARTP), bwritten, NULL);
    PlaySound (argv [1], NULL, SND_FILENAME | SND_SYNC);
    WriteFile (stdo, ENDPLY, lstrlen (ENDPLY), bwritten, NULL);
}
