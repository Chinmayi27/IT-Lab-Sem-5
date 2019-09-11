#include <omp.h>

//static long num_steps= 10000000;
// #define 

double serial(long num_steps, int num_of_threads){
	int i;
	double x, pi, sum = 0.0, step;
	step = 1.0/(double) num_steps;
	for(i=0;i<1000000000;i++)
		;
	double start_time =  omp_get_wtime();
	for (i=0;i< num_steps; i++)
	{	
		x = (i+0.5)*step;
		sum = sum + 4.0/(1.0+x*x);
	}

	pi = step * sum;
	double end_time = omp_get_wtime();
	//printf("Area under curve = %lf \n",pi);
	return (end_time - start_time);
}

double parallel(long num_steps, int num_of_threads){
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
		for (i=id, lsum=0.0; i< num_steps; i = i+num_of_threads)
		{	
			x = (i)*step;
			lsum += 4.0/(1.0+x*x);
		}
		
		pi += step * lsum;
	}
	double end_time = omp_get_wtime();	
	
	printf("Area under curve = %lf \n",pi);
	return (end_time - start_time);
}

int main ()
{
	int i, j, num_of_threads=1;
	double pi, sum[num_of_threads], step, nthreads;
	
	for (j=1000; j<=10000; j+=2000, num_of_threads+=2){
		double _serial = serial(j, num_of_threads);
		double _parallel = parallel(j, num_of_threads);
		printf("%lf %lf",_serial,_parallel);
		double speedup = _serial/(_parallel);
		printf("Speedup = %lf, no. of threads = %d\n",speedup, num_of_threads );
	}
	
}