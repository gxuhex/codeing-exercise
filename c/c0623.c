/********************c0623.c******************/
# include <stdio.h>

typedef struct employee
{
    char name [20];
    char gender;
    char age;
    unsigned int score;
} stgEMP;

int main (void)
{
    FILE * hfile = fopen ("myfile6.dat", "wb");

    if (hfile == NULL) return -1;

    stgEMP empa [] = {
        {"LiShuangyuan", 'F', 12, 600},
        {.age = 20, 1500, .name = "LiJianan", 'F'},
        [5] = {"WangXiaobo", 'F', 35, 20000},
        [6].name = "LiZhiping", 'M', 15, 800,
    };

    fwrite (empa, sizeof (stgEMP),\
              sizeof empa / sizeof (stgEMP), hfile);

    fclose (hfile);
}
