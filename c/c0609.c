/*********************c0609.c********************/
# include <unistd.h>
# include <fcntl.h>
# include <sys/stat.h>

struct employee
{
    char name [20];
    char gender;
    char age;
    unsigned int score;
};

int main (void)
{
    int fd;
    fd = open ("myfile2.dat", O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
    if (fd == -1) return -1;

    struct employee emp = {"WangXiaobo", 'F', 26, 5000};
    write (fd, & emp, sizeof emp);

    close (fd);
}
