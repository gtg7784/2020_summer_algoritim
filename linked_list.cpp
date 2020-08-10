#include <iostream>
#include <list>
using namespace std;

int main(){
  list<char> A;
  A.push_back(3);
  A.push_back(5);
  A.push_back(7);
  A.pop_back();
  A.pop_front();
  return 0;
}
