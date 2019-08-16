/*****************c0517.c************/
_Bool fstrcmp (char (* para) [], char (* parb) [])
{
    char * p = * para, * q = * parb;

    while (* p != '\0' && * q != '\0')
        if (* p ++ != * q ++) return 0;

    return * p == * q;				//S1
}

int main (void)
{
    char a [] = "The Wizard of Oz";
    _Bool b = fstrcmp (& a, & "Goodbye Mr Hollywood");

    char (* pc) [] = & a;
    b = fstrcmp (pc, & a);
}
