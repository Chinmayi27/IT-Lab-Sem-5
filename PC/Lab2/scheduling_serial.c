#include <omp.h>
#include <stdio.h>
int main(){
    int i;
    
    int n=100000;
    int a[n], b[n];

    double start_time = omp_get_wtime();

    for(i=0; i<n;i++)
    {
        a[i]+=1;
    }
    
        
    printf("serial scheduling time = %lfs\n",omp_get_wtime()-start_time);
}

