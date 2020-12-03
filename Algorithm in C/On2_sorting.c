#include <stdio.h>

void bubbleSort(int* inArr[]);
void insertionSort(int* inArr[]);
void selectionSort(int* inArr[]);
void swap(int *num1, int *num2);

int main(int argc, char* argv){

}

void bubbleSort(int* inArr[]){
	int count = -1;
	size_t n = sizeof(inArr)/sizeof(int);

	while(count != 0){
		count = 0;
		for(int i = 0; i < n-1; i++){
			if(inArr[i] > inArr[i+1]){
				swap(&inArr[i], &inArr[i+1]);
				count++;
			}
	}
}

void insertionSort(int* inArr[]){

}

void selectionSort(int* inArr[]){
	size_t n = sizeof(inArr)/sizeof(int);
	for(int i = 0; i < n; i++){
		int smallest = inArr[i];
		int index = i;
		for(int j = i+1; j < n; j++){
			if(inArr[j] < smallest){
				smallest = inArr[j];
				index = j;
			}
		}
		swap(&inArr[index], &inArr[i]);
	}
}

void swap(int *num1, int *num2){
	int tmp = *num1;
	*num1 = *num2;
	*num2 = tmp;
}
