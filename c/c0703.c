/**************************c0703.c*************************/
# include <windows.h>

int main (void)
{
    char * mstr = "�ҵ�������lizhongc.com\n";
    MessageBoxA (NULL, mstr, "��ʾ", MB_OK | MB_ICONINFORMATION);

    wchar_t * wstr = L"�����ƶ��绰cell-phone\n";
    MessageBoxW (NULL, wstr, L"��ʾ", MB_OK | MB_ICONINFORMATION);
}
