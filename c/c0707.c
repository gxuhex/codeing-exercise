/************************c0707.c*********************/
# include <stdio.h>
# include <wchar.h>
# include <locale.h>

int main (void)
{
    setlocale (LC_ALL, "chinese");
    wchar_t wa [] = L"�ҵ�������lizhongc.com";
    printf ("��%ls���еĵ�2���ַ��ǡ�%lc��\n", wa, wa [1]);
}
