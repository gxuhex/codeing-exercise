/*********************c0610.c********************/
# include <unistd.h>

int main (void)
{
    char * pbook = "The Laws of Boole's Thought.\n";
    write (STDOUT_FILENO, pbook, strlen (pbook));
}
