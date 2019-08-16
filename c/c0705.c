/***************************c0705.c*************************/
# include <windows.h>

int main (void)
{
    wchar_t * wstr = L"这个“𠰰”字你认识吗？";
    MessageBoxW (NULL, wstr, L"演示", MB_OK | MB_ICONINFORMATION);

    wstr = L"这个“\xd843\xdc30”字你认识吗？";
    MessageBoxW (NULL, wstr, L"演示", MB_OK | MB_ICONINFORMATION);
}
