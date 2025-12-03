#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int divInt(int a, int b)
{
    int res = a / b;
    return res - (a % b < 0);
}
/*
static int  getFactorPairs(int n){
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            // i is a factor, so n/i is the other factor in the pair
            int other_factor = n / i;

            
        }
    }
}*/

char *str_repeat(const char *str, int n) {
    if (n <= 0) return NULL;

    size_t len = strlen(str);
    // Allocate memory: (length * repeats) + 1 for null terminator
    char *dest = malloc((len * n) + 1); 
    
    if (dest == NULL) return NULL; // Allocation failed

    // Copy the string n times
    for (int i = 0; i < n; i++) {
        // memcpy is faster than strcat because it doesn't scan for \0
        memcpy(dest + (i * len), str, len);
    }

    // Manually add the null terminator at the end
    dest[len * n] = '\0';

    return dest;
}

int main(void)
{

    FILE *fp = fopen("input.in", "r");
    if (fp == NULL)
    {
        exit(EXIT_FAILURE);
    }
    divInt(6, 7);
    char *line = NULL;
    size_t totalLineLen = 0;
    ssize_t read;
    long p1 = 0;
    long p2 = 0;
    while ((read = getline(&line, &totalLineLen, fp)) != -1)
    {  
        char * ptrIdRange = strtok(line, ",");
        while(ptrIdRange != NULL){
            long low, high;

            // Returns the number of items successfully matched (should be 2 here)
            if (sscanf(ptrIdRange, "%ld-%ld", &low, &high) == 2) {
                for(long id =low; id<=high; id++){
                    char ptrIdStr[25];
                    snprintf(ptrIdStr, sizeof(ptrIdStr), "%ld", id);
                    size_t length = strlen(ptrIdStr);
                    char halfId[length/2+1];
                    strncpy(halfId, ptrIdStr, length/2);
                    halfId[length/2]='\0';
                    char *repeatedHalf = str_repeat(halfId, 2);
                    if(length%2==0){
                        if((strcmp(ptrIdStr, repeatedHalf)==0)){
                            p1 += id;
                        }
                    }
                    free(repeatedHalf);
                    for (long i=1;i*i<=length;i++){
                        if(length%i==0){
                            long a =  i;
                            long b = length/i;
                            char ptrIdPartA[a+1];
                            char ptrIdPartB[b+1];
                            strncpy(ptrIdPartA, ptrIdStr, a);
                            ptrIdPartA[a] = '\0';
                            strncpy(ptrIdPartB, ptrIdStr, b);
                            ptrIdPartB[b] = '\0';
                            char * ptrRepeatedA = str_repeat(ptrIdPartA, b);
                            char * ptrRepeatedB = str_repeat(ptrIdPartB, a);
                            
                            if((b > 1 && strcmp(ptrIdStr, ptrRepeatedA)==0) || (a > 1 && strcmp(ptrIdStr, ptrRepeatedB)==0)){
                                p2 += id;
                                //printf("%s\n", ptrIdStr);
                                free(ptrRepeatedA);
                                free(ptrRepeatedB);
                                break;
                            }
                            free(ptrRepeatedA);
                            free(ptrRepeatedB);
                        }
                    }
                }
            }
            ptrIdRange = strtok(NULL, ",");
        }        
    }
    fclose(fp);
    if (line)
    {
        free(line);
    }
    printf("%ld, %ld", p1, p2);
    return 0;
}