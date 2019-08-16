/**********************c0608.c*********************/
# include <unistd.h>
# include <fcntl.h>
# include <sys/stat.h>

int main (void)
{
    int fd;
    fd = open ("myfile1.dat", O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);

    if (fd == -1) return -1;

    char name [] = "LiuChangjiang", gender = 'M', age = 36;
    unsigned int score = 2200;

    write (fd, name, strlen (name));
    write (fd, & gender, sizeof gender);
    write (fd, & age, sizeof age);
    write (fd, & score, sizeof score);

    close (fd);
}
