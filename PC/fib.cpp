#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

int fibonacci(int n){
	if(n<=2)
		return 1;

	return fibonacci(n-1)+fibonacci(n-2);
}

int main(){
	int n;
	cin>>n;

	double start_time = omp_get_wtime();
	cout<<fibonacci(n)<<endl;
	double end_time = omp_get_wtime();
	cout<<"Time taken: "<<end_time - start_time;
}