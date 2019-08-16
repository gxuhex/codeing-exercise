/*************c0605.c************/
int preld (int * const cpc, const int ci)
{
    return * cpc + ci;
}

int main (void)
{
    int c = 1, d = preld (& c, c);
}
