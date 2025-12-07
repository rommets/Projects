#include <iostream>
using namespace std;
int main()
{
    int x;
    float a, b, c;
    cout << "2adad vared konid: \n";
    cin >> a >> b;
    cout << "1)SUM\t2)SUB\n3)MUL\t4)DIV\n";
    cin >> x;
    switch (x)
    {
    case 1:
        cout << "javab shoma: " << a + b;
        break;
    case 2:
        cout << "javab shoma: " << a - b;
        break;
    case 3:
        cout << "javab shoma: " << a * b;
        break;
    case 4:
        cout << "javab shoma: " << a / b;
        if (b == 0)
        {
            cout << "INFINITY!!!!";
        }
        break;
    }
    return 0;
}
