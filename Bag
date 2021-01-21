#include <iostream>
#include <string>

class Bag {
public:
  Bag (
  void Remove (int n);
  bool Add (int n);
  bool isEmtpy();
  bool search (int s);
  void print();
private:
  int *data;
  unsigned int size;
  unsigned int capacity;
};

Bag :: Bag (){
  data = NULL;
  size = 0;
  cin>>capacity;
  data = new int[capacity];
}

bool Bag :: Add (int n){
  if(size==capacity) return false;
  else{
    data[size++] = n;
    return ture;
}

void Bag ::Remove(int n){
	if (isEmtpy() == true) 
		cout<<"This can't '";
	for (int i = 0; i < size; i++){    //  search for the item n
		if (data[i] == n){
			data[i]=data[i+1];
			for(int j=i+1;j<size;j++){
				data[j]=data[j+1];
			}
		}	
	}
}

bool Bag :: isEmtpy{
  if(size==0) return false;
}

bool Bag :: search (int s){
	for(int i=0;i<size;i++){
		if(data[i]==s) return true;
	}
	return false;
}

void Bag :: print(){
	
}

int main(){
	Bag bag;
	bag.add(1); bag.add(2); bag.add(3); bag.add(4); bag.add(5);
}
