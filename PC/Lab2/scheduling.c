#include <omp.h>
#include <stdio.h>
int main(){
    int i;
    
    int n=100000;
    int a[n];

    double start_time = omp_get_wtime();
    #pragma omp parallel
    {
        #pragma omp for nowait schedule(static,100)
        for(i=0; i<n;i++)
        {
            a[i]+=1;
        }
     }
        
    printf("static scheduling time = %lfs\n",omp_get_wtime()-start_time);
}

