/*********************c0604.c*******************/
# include "iotool.h"

# define CHAR_BUF_LEN 20
# define MAX_SUM_NUM 1000
# define FIXED_SUFFIX(x) "1+2+3+...+" #x "="
# define PRN_FIXED_SUFFIX(x) FIXED_SUFFIX(x)

int main (void)
{
    write_string (PRN_FIXED_SUFFIX(MAX_SUM_NUM));

    char a [CHAR_BUF_LEN];
    write_string (ull_to_string (cusum (MAX_SUM_NUM), a));
    write_string ("\n");
}
