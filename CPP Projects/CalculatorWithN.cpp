#include <iostream>
using namespace std;
int main()
{
    int counter = 0;
    int number, n;
    int sum = 0;
    cout << "how many numbers? ";
    cin >> n;
    cout << endl
         << "enter ur numbers: ";
    while (counter < n)
    {
       cin >> number;
        sum = number + sum;
        counter++;
    }
    cout<<sum;

    return 0;
}