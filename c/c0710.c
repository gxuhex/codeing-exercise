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

    wchar_t a [] = L"��Ϊ������http://www.huawei.com/";
    wprintf (L"��%lc����һ��%ls��ĸ��\n", a [8],
               iswupper (a [8]) ? L"��д" : L"Сд");
    wprintf (L"��%ls������%zu���ַ���\n", a, wcslen (a));
}
