#include <iostream>
using namespace std;
int main()
{
    float numbers;
    float sum = 0;
    cout << "enter ur numbers:";
    cin >> numbers;

    while (numbers != -1)
{ 
       sum = sum + numbers;
       cin >> numbers;
}


    cout << "sum is:"<<sum;
    return 0;
}