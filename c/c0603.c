/******************c0603.c*******************/
int write_string (char *);
char * ull_to_string (unsigned long long int, char *);
unsigned long long int cusum (unsigned long long);

int main (void)
{
    write_string ("1+2+3+...+1000=");

    char a [20];

    write_string (ull_to_string (cusum (1000), a));
    write_string ("\n");
}
