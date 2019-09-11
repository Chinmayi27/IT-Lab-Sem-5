#include<stdio.h>
#include<omp.h>

int main(){
	int n=500;
	int m1[n][n],m2[n][n];
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
		m1[i][j]=j;
		m2[i][j]=j;
	}
	}

	long int res[n][n];
	int i,j,k;
	double startime=omp_get_wtime();


	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			res[i][j]=0;
			for(k=0;k<n;k++){
				res[i][j]+=m1[i][k]*m2[k][j];			
			}
		}
	}
	
	printf("Matrix multiplication, Time taken serially: %f \n",omp_get_wtime()-startime);
}