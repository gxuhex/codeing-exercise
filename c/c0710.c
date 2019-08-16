/********************c0710.c*******************/
# define __USE_MINGW_ANSI_STDIO 1

# include <locale.h>
# include <wctype.h>
# include <wchar.h>
# include <stdio.h>

int main (void)
{
# if defined (PWINDOWS)
    setlocale (LC_ALL, "Chinese");
# elif defined (PLINUX)
    setlocale (LC_ALL, "zh_CN.UTF-8");
# else
    printf ("PWINDOWS or PLINUX is not defined.\n");
    return 0;
# endif

    wchar_t a [] = L"华为官网：http://www.huawei.com/";
    wprintf (L"‘%lc’是一个%ls字母。\n", a [8],
               iswupper (a [8]) ? L"大写" : L"小写");
    wprintf (L"“%ls”包含%zu个字符。\n", a, wcslen (a));
}
