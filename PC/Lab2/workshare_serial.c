#include <omp.h>
#include <stdio.h>
int main(){
    long int i;
    long int n=100000;
    int a=0, b=0, d[n], c[n];

   // for(i=0;i<n;i++)
   //  a[i]=i; 

    double start_time = omp_get_wtime();

    for(i=0; i<n;i++)
    {
        a+=1;
    }
 
    for(i=0; i<n;i++)
    {
        b+=1;
    }
    
    printf("Serial time = %lfsec",omp_get_wtime()-start_time);
}