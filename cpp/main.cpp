//EXTRA 1: Show if statement and loop
//EXTRA 2 : Show a working function

#include <iostream>
#include <string>

using namespace std;

//Extra 1: Implement working function to return postive number
int main() {
  
  int number;
  
  cout << "Enter an number: ";
  cin >> number;

  if (number > 0) {
    cout << "This number is postive: " << number << endl;
  }
  //Base Project
  cout << "Hello World.";

  return 0;
}


//Extra 2 Show a working if and loop: 
int max(int x, int y)
{
  if (y > x)
    return y;
  else
    return x;
}


