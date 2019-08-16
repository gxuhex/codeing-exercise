/************************c0707.c*********************/
# include <stdio.h>
# include <wchar.h>
# include <locale.h>

int main (void)
{
    setlocale (LC_ALL, "chinese");
    wchar_t wa [] = L"我的域名是lizhongc.com";
    printf ("“%ls”中的第2个字符是“%lc”\n", wa, wa [1]);
}
