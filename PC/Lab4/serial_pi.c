#include <omp.h>

static long num_steps= 10000000;
int main ()
{
	int i;
	double x, pi, sum = 0.0, step;
	step = 1.0/(double) num_steps;
	double start_time =  omp_get_wtime();
	for (i=0;i< num_steps; i++)
	{	
		x = (i+0.5)*step;
		sum = sum + 4.0/(1.0+x*x);
	}

	pi = step * sum;
	double end_time = omp_get_wtime();
	printf("Area under curve = %lf \n",pi);
	printf("Time taken = %lf\n", end_time - start_time);
}