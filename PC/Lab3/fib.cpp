#include <stdlib.h>
#include <stdio.h>
#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

int fib(int n)
{
	int i, j;
	if(n < 2) 
		return n;

	i= fib(n-1);
	j = fib(n-2);
	return (i+j);
}

int main()
{
	int n = 40;
	double start_time, end_time;
	start_time = omp_get_wtime();
	printf("Fib(%d) = %d", n, fib(n));
	end_time = omp_get_wtime();
	cout<<"\nTime taken (serially): "<<end_time- start_time<<endl;
}