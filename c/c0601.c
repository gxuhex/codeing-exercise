/*************c0601.c**************/
int main (void)
{
    int r;

    __asm__ (
                "mov eax, 0x4 \n\t"
                "mov ebx, 0x1 \n\t"
                "mov edx, 0xd \n\t"
                "int 0x80 \n\t"
                : "=a" (r)
                : "c" ("hello world.\n")
              );

    return r;
}
