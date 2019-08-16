/******************c0706.c****************/
# include <stdio.h>
# include <locale.h>
# include <time.h>

int main (void)
{
    setlocale (LC_ALL, "Chinese");
    setlocale (LC_NUMERIC, "German");

    printf ("圆周率：%.2f\n", 3.14);

    char tms [100];
    time_t tm = time (NULL);
    strftime (tms, 100, "%Z %c %A %p", localtime (& tm));
    printf ("本地时间：%s\n", tms);
}
