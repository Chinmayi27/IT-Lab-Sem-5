#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

int fibonacci(int n){
	if(n<=2)
		return 1;


	long long int res1;
	omp_set_dynamic(8);
	omp_set_num_threads(2);

	#pragma omp parallel 
	{
		#pragma omp task
		res1 = fibonacci(n-1)+fibonacci(n-2);
	}
	
	return res1;
}

int main(){
	int n;
	cin>>n;

	//omp_set_dynamic(8);
	//omp_set_num_threads(2);

	double start_time = omp_get_wtime();

	{
		cout<<fibonacci(n)<<endl;
	}
	
	double end_time = omp_get_wtime();
	cout<<"Time taken: "<<end_time - start_time;
}