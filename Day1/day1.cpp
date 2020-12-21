#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream in("input.txt");
    vector<int> a;
    int temp;
    int i = 0;
    while (in >> temp)
    {

        a.push_back(temp);
        i++;
    }
    in.close();
    for (int j = 0; j < i; j++)
    {
        for (int k = j + 1; k < i; k++)
        {
            if (a[j] + a[k] == 2020)
                cout << "\n Part One answer: " << a[j] * a[k];
        }
    }
    for (int j = 0; j < i; j++)
    {
        for (int k = j + 1; k < i; k++)
        {
            for (int m = k + 1; m < i; m++)
            {
                if (a[j] + a[k] + a[m] == 2020)
                    cout << "\n Second Answer: " << a[j] * a[k] * a[m];
            }
        }
    }
    return 0;
}