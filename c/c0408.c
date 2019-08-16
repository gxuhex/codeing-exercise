/**********c0408.c*********/
int main (void)
{
    signed char cx = 1, cy = 2;
    signed long int sl = 0;
    unsigned long int ul = 0;

    sl += cx + cy;
    sl += cx * 3L;
    ul += sl <= ul;

    unsigned char uc = -1;
    cy = - uc ++;
}
