#include <stdlib.h>
#include <stdio.h>
#include <bits/stdc++.h>
#include <omp.h>

using namespace std;
int fib_serial(int n)
{
	int i, j;
	if(n < 2) 
		return n;

	i= fib_serial(n-1);
	j = fib_serial(n-2);
	return (i+j);
}

int fib(int n){
	int i, j, id;
	if(n < 20)
		return fib_serial(n);

	#pragma omptask shared (i) private (id)
	{	
		i= fib(n-1);
	}

	#pragma omptask shared (j) private (id)
	{
		j = fib(n-2);
	}

	#pragma omp taskwait
	return (i+j);
}

int main()
	{
	int nthreads;
	int n = 40;
	double start_time, end_time;
	#pragma omp parallel num_threads(2)
	{
		#pragma omp single
		{
			start_time = omp_get_wtime();
			printf("Fib(%d) = %d", n, fib(n));
			end_time = omp_get_wtime();
		}
	} 
	cout<<"\nTime taken (using task + taskwait directive): "<<end_time- start_time<<endl;
}

