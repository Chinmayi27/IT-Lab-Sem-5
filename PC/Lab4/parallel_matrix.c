#include<stdio.h>
#include<omp.h>

int main(){
	int n=100;
	int m1[n][n],m2[n][n];
	// for(int i=0;i<n;i++){
	// 	for(int j=0;j<n;j++){
	// 	m1[i][j]=j;
	// 	m2[i][j]=j;
	// }
	// }

	long int res[n][n];
	int i=0,j,k;

	double startime;//=omp_get_wtime();
	int tnum =10;
	for(tnum = 1; tnum<50; tnum*=2){
		omp_set_num_threads(i);
		startime=omp_get_wtime();

		#pragma omp parallel
		{
			for(;i<n;i++){
				for(j=0;j<n;j++){
					res[i][j]=0;

					#pragma parallel for nowait
					for(k=0;k<n;k++){
						res[i][j]+=m1[i][k]*m2[k][j];			
					}
				}
			}
		}

		printf("Matrix multiplication(%d X %d), parallely: %lf (s) using %d threads\n", n, n, omp_get_wtime()-startime, tnum);
	}
	
	
	//printf("Matrix multiplication, Time taken parallely: %lf\n", omp_get_wtime()-startime);
}
