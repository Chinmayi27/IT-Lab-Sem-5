#include<stdio.h>
#include<omp.h>

int main(){
	//num_threads(1);
	int num_threads = 0;
	printf("Enter number of threads: ");
	scanf("%d", &num_threads);
	//omp_set_num_threads(num_threads);
	#pragma omp parallel num_threads(num_threads)
	{
		int ID = omp_get_thread_num();
		printf("hello world!(%d)\n",ID);
	}
	return 0;
}	