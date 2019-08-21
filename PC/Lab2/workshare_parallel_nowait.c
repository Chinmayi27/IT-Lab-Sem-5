#include <omp.h>
#include <stdio.h>
int main(){
    int i, j;
    int n=100000;
    int a=0, b=0, d=0, c=0;

    //omp_set_num_threads(2);
    double start_time = omp_get_wtime();
    #pragma omp parallel num_threads(2) shared(n, a, b, d, c), private(i, j)
    {

        #pragma parallel for nowait reduction(+:a)
        for(i=0; i<n;i++)
        {
            a+=1;
        }
     
        #pragma parallel for nowait reduction(+:b)
        for(j=0; j<n;j++)
        {
            b+=1;
        }
    } 
    
    
    printf("parallel time with nowait= %lfsec",omp_get_wtime()-start_time);
}