/**********************c0612.c*********************/
# include <windows.h>
# include <strsafe.h>

typedef struct employee
{
    char name [20];
    char gender;
    char age;
    unsigned int score;
} stgEMP;

int main (void)
{
    HANDLE hf = CreateFile ("myfile3.dat", \
                            GENERIC_READ | GENERIC_WRITE, \
                            0, NULL, CREATE_ALWAYS, \
                            FILE_ATTRIBUTE_NORMAL, NULL);

    if (hf == INVALID_HANDLE_VALUE) return -1;

    stgEMP emp;
    StringCchCopy (emp.name, sizeof emp.name, "HuoFengrong");
    emp.gender = 'F';
    emp.age = 79;
    emp.score = 56666;

    WriteFile (hf, & emp, sizeof emp, & (DWORD) {0}, 0);

    CloseHandle (hf);
}
