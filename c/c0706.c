/******************c0706.c****************/
# include <stdio.h>
# include <locale.h>
# include <time.h>

int main (void)
{
    setlocale (LC_ALL, "Chinese");
    setlocale (LC_NUMERIC, "German");

    printf ("Բ���ʣ�%.2f\n", 3.14);

    char tms [100];
    time_t tm = time (NULL);
    strftime (tms, 100, "%Z %c %A %p", localtime (& tm));
    printf ("����ʱ�䣺%s\n", tms);
}
