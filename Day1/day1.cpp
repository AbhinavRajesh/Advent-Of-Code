#include <iostream>
#include <fstream>

using namespace std;

void problem1(int a[], int &i)
{
    int temp;
    ifstream in("input.txt");
    while (in >> temp)
    {
        a[i] = temp;
        i++;
    }
    in.close();
}

int main()
{
    int a[100];
    int i = 0;
    problem1(a, i);
    cout << i;
    for (int j = 0; j < i; j++)
    {
        for (int k = j + 1; k < i; k++)
        {
            if ((a[j] + a[k]) == 2020)
                cout << a[j] * a[k];
        }
    }
    return 0;
}