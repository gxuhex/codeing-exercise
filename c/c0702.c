/****************************c0702.c***************************/
# include <windows.h>

int main (void)
{
    char * cstr0 = "蜂窝移动电话cell-phone\n";
    WriteFile (GetStdHandle (STD_OUTPUT_HANDLE), cstr0,
               lstrlen (cstr0), (DWORD []) {0}, NULL);

    char * cstr1 = u8"我的域名是lizhongc.com\n";
    WriteFile (GetStdHandle (STD_OUTPUT_HANDLE), cstr1,
               lstrlen (cstr1), (DWORD []) {0}, NULL);
}
