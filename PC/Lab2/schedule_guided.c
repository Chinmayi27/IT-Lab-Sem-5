#include <omp.h>
#include <stdio.h>
int main(){
    int i;
    
    int n=100000;
    int a[n];

   // for(i=0;i<n;i++)
   //  a[i]=i;
    int b[n];
    double start_time = omp_get_wtime();
    #pragma omp parallel num_threads(1000)
    {
        #pragma omp for schedule(dynamic,1000)
        for(i=0; i<n;i++)
        {
            b[i]=(a[i])/2;
        }
     }
        
    printf("guided scheduling time = %lfs\n",omp_get_wtime()-start_time);
}

