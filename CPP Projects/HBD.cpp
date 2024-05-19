#include <iostream>
#include <thread>
using namespace std;
int main()
{
    int i=0;
    for(i=1;i<3;i++) 
{
    cout<<"Happy Birthday To You\a"<<endl;
    this_thread::sleep_for(chrono::seconds(4));
}
cout<<"Happy Birthday To The Best Uncle Ever"<<endl;
this_thread::sleep_for(chrono::seconds(5));
cout<<"Happy Birthday To You"<<endl;
cout<<endl;
cout<<endl;
cout<<endl;
return 0;
} 