#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <math.h>

static int divInt(int a, int b)
{
    int res = a / b;

    return res - (a % b < 0);
}

int main(void)
{

    FILE *fp = fopen("input.in", "r");
    if (fp == NULL)
    {
        exit(EXIT_FAILURE);
    }
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    int number = 50;
    int p1 = 0;
    int p2 = 0;
    while ((read = getline(&line, &len, fp)) != -1)
    {
        int prevNum = number;
        int inputNum = atoi((line + 1));
        if (line[0] == 'L')
        {
            number -= inputNum;
            p2 += divInt((prevNum - 1), 100) - divInt((number - 1), 100);
        }
        else if (line[0] == 'R')
        {
            number += inputNum;
            p2 += divInt(number, 100) - divInt(prevNum, 100);
        }
        if (number%100 == 0)
        {
            p1 += 1;
        }
    }
    fclose(fp);
    if (line)
    {
        free(line);
    }
    printf("%d, %d", p1, p2);
    return 0;
}