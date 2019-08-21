#include <omp.h>

static long num_steps= 10000000;
#define num_of_threads 8

int main ()
{
	int i;
	double pi=0.0, sum[num_of_threads], step, nthreads;
	step = 1.0/(double) num_steps;

	omp_set_num_threads(num_of_threads);
	double start_time =  omp_get_wtime();
	#pragma omp parallel
	{
		int i, id;
		double x,lsum;
		id = omp_get_thread_num();
		// if (id == 0)   
		// 	nthreads= nthrds;
		for (i=id, lsum=0.0;i< num_steps; i = i+num_of_threads)
		{	
			x = (i)*step;
			lsum += 4.0/(1.0+x*x);
		}
		pi += step * lsum;
	}
	double end_time = omp_get_wtime();	
	
	printf("Area under curve = %lf \n",pi);
	printf("Time taken = %lf\n", end_time - start_time);
}