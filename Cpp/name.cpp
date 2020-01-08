#include <iostream>
using namespace std;

int main()
{
    string name;
    cout<<"May i know your name\n";
    cin>>name;
// if u want full name to print use below code
  //getline(cin,name);
    cout<<"Hello, Mr."<<name<<"\nWelcome to CPP\n";
    return 0;
}