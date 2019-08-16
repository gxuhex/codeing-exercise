/*************c0518.c************/
int main (void)
{
    int a, b, * arrpi [2];

    arrpi [0] = & a;				//S1
    arrpi [1] = & b;				//S2
    * arrpi [0] = 10010;		//S3
    * arrpi [1] = 10086;		//S4

    char c, d, * arrps [2];

    arrps [0] = "Search";		//S5
    arrps [1] = "Project";		//S6
    c = * arrps [0];				//S7
    d = * arrps [1];				//S8
}
