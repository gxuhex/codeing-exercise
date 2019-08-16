/**************************c0703.c*************************/
# include <windows.h>

int main (void)
{
    char * mstr = "我的域名是lizhongc.com\n";
    MessageBoxA (NULL, mstr, "演示", MB_OK | MB_ICONINFORMATION);

    wchar_t * wstr = L"蜂窝移动电话cell-phone\n";
    MessageBoxW (NULL, wstr, L"演示", MB_OK | MB_ICONINFORMATION);
}
