/****************************c0702.c***************************/
# include <windows.h>

int main (void)
{
    char * cstr0 = "�����ƶ��绰cell-phone\n";
    WriteFile (GetStdHandle (STD_OUTPUT_HANDLE), cstr0,
               lstrlen (cstr0), (DWORD []) {0}, NULL);

    char * cstr1 = u8"�ҵ�������lizhongc.com\n";
    WriteFile (GetStdHandle (STD_OUTPUT_HANDLE), cstr1,
               lstrlen (cstr1), (DWORD []) {0}, NULL);
}
