/**********************c0631.c*********************/
# include <stdio.h>
# include <stdlib.h>

typedef struct ss {
    char name [20];
    char gender [7];		//F/M Лђеп Female/Male
    unsigned int age;
    char grade [10];		//freshman/sophomore/junior/senior
    float score;
    struct ss * next;
} SSTUD, * PSSTUD;

void destroy_stud_info (PSSTUD pps)
{
    PSSTUD tmp;
    while (pps != NULL)
        tmp = pps, pps = pps -> next, free (tmp);
}

PSSTUD get_stud_info (void)
{
    FILE * pf = fopen ("students.dat", "r");
    if (pf == NULL)
    {
        printf ("File open failed.\n");
        return NULL;
    }

    PSSTUD pstd = malloc (sizeof (SSTUD));
    if (pstd == NULL)
    {
        printf ("Memory allocated failed.\n");
        return NULL;
    }

    if (fscanf (pf, "%s%s%u%s%f", pstd -> name, pstd -> gender,\
                  & pstd -> age, pstd -> grade, & pstd -> score)\
                  == EOF)
    {
        printf ("Empty file.please append some records.\n");
        free (pstd);
        return NULL;
    }

    pstd -> next = NULL;

    PSSTUD temp = pstd;
    do {
        if (temp -> next != NULL) temp = temp -> next;
        if ((temp -> next = malloc (sizeof (SSTUD))) == NULL)
        {
            printf ("Memory allocated failed.\n");
            destroy_stud_info (pstd);
            return NULL;
        }
        temp -> next -> next = NULL;
    } while (fscanf (pf, "%s%s%u%s%f", temp -> next -> name,\
               temp -> next -> gender, & temp -> next -> age,\
               temp -> next -> grade, & temp -> next -> score) != EOF);

    free (temp -> next);
    temp -> next = NULL;
    fclose (pf);

    return pstd;
}

void print_stud_info (PSSTUD pps)
{
    printf ("%-20s%5s%5s%15s%10s\n",\
             "NAME", "GENDR", "AGE", "GRADE", "SCORE");
    printf ("------------"\
             "-------------------------------------------\n");

    int total = 0;
    float sum = 0.0f;

    while (pps != NULL)
    {
        total ++;
        sum += pps -> score;
        printf ("%-20s%5s%5u%15s%10.2f\n", pps -> name, pps ->\
                  gender, pps -> age, pps -> grade, pps -> score);
        pps = pps -> next;
    }

    printf ("-------------"\
             "------------------------------------------\n");
    printf ("%-20s%35u\n", "Total:", total);
    printf ("-------------"\
             "------------------------------------------\n");
    printf ("%-20s%35.2f\n", "Sum:", sum);
    printf ("-------------"\
             "------------------------------------------\n");
    printf ("%-20s%35.2f\n", "Average:", sum / total);
}

int main (void)
{
    PSSTUD pstd = get_stud_info ();

    if (pstd != NULL)
    {
        print_stud_info (pstd);
        destroy_stud_info (pstd);
    }
    else
        printf ("No students information to print.\n");
}
