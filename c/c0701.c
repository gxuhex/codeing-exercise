/************************c0701.c*************************/
# include <unistd.h>
# include <string.h>

int main (void)
{
    char * cstr0 = "�����ƶ��绰cell-phone\n";
    write (STDOUT_FILENO, cstr0, strlen (cstr0));

    char * cstr1 = u8"�ҵ�������lizhongc.com\n";
    write (STDOUT_FILENO, cstr1, strlen (cstr1));
}
