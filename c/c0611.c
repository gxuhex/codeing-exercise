/*******************c0611.c*******************/
# include <unistd.h>

# define PROMPT "->"

int main (void)
{
    char buf [1];

    write (STDOUT_FILENO, PROMPT, strlen (PROMPT));

    while (read (STDIN_FILENO, buf, sizeof buf) > 0)
        write (STDOUT_FILENO, buf, sizeof buf);
}
