/************************c0701.c*************************/
# include <unistd.h>
# include <string.h>

int main (void)
{
    char * cstr0 = "蜂窝移动电话cell-phone\n";
    write (STDOUT_FILENO, cstr0, strlen (cstr0));

    char * cstr1 = u8"我的域名是lizhongc.com\n";
    write (STDOUT_FILENO, cstr1, strlen (cstr1));
}
