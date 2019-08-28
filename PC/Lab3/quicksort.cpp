#include <bits/stdc++.h> 
#include <omp.h>
#include <cstdlib>
using namespace std;  
  
 
void swap(int* a, int* b)  
{  
    int t = *a;  
    *a = *b;  
    *b = t;  
}  
  
int partition ( vector <int> arr, int low, int high)  
{  
    int pivot = arr[high]; 
    int i = (low - 1); 
  
    for (int j = low; j <= high - 1; j++)  
    {  
        
        if (arr[j] < pivot)  
        {  
            i++;   
            swap(&arr[i], &arr[j]);  
        }  
    }  
    swap(&arr[i + 1], &arr[high]);  
    return (i + 1);  
}  
  

void quickSort(vector <int> arr, int low, int high)  
{  
    if (low < high)  
    {  
       
        int pi = partition(arr, low, high);  
  
        quickSort(arr, low, pi - 1);  
        quickSort(arr, pi + 1, high);  
    }  
}  
  

void printArray(vector <int> arr, int size)  
{  
    int i;  
    for (i = 0; i < size; i++)  
        cout << arr[i] << " ";  
    cout << endl;  
}  
  

int main()  
{  
    
	vector <int> arr;
	int n=10000;
	for(int i=0; i<n; i++)
    {
	   arr.push_back(rand()%1003);
    }	
      
    double start_time = omp_get_wtime();
    quickSort(arr, 0, n - 1);  
    //cout << "Sorted array: \n";  
    //printArray(arr, n);  
    double end_time = omp_get_wtime();
    cout<<"Time taken(serially): "<<end_time - start_time<<endl;
    return 0;  
}
