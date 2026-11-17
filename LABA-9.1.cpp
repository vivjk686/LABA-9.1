//////////////////////////////////////////////////////////////////////////////
// LABA-9.1.cpp
// Головний файл проекту – функція main
// Варіант 32: arctg(x) = -pi/2 + sum_{n=0}^inf (-1)^{n+1} / ((2n+1)*x^{2n+1}), x < -1
#include <iostream>
#include <iomanip>
#include <cmath>
#include "dod.h"
#include "sum.h"
#include "var.h"

using namespace std;
using namespace nsDod;
using namespace nsSum;
using namespace nsVar;

#ifndef UNIT_TESTING
int main()
{
    cout << "Laboratorna robota No 9.1 (Variant 32)" << endl;
    cout << "Obchyslennya sumy ryadu Teilora dlya arctg(x), de x < -1" << endl << endl;

    cout << "Vvedit x_p (pochatkove x < -1): "; cin >> x_p;
    cout << "Vvedit x_k (kintseve x < -1):   "; cin >> x_k;
    cout << "Vvedit dx  (krok > 0):           "; cin >> dx;
    cout << "Vvedit e   (tochnist > 0):       "; cin >> e;
    cout << endl;

    if (x_p >= -1.0 || x_k >= -1.0) {
        cout << "Uvaha: za umovoyu zadachi (Variant 32) x maye buty < -1!" << endl << endl;
    }

    cout << "--------------------------------------------------------" << endl;
    cout << "|" << setw(10) << "x" << " |"
         << setw(14) << "arctg(x)" << " |"
         << setw(14) << "S" << " |"
         << setw(8) << "n" << " |" << endl;
    cout << "--------------------------------------------------------" << endl;

    x = x_p;
    while (x <= x_k + dx / 2.0) {
        sum();
        cout << "|" << setw(10) << setprecision(4) << fixed << x << " |"
             << setw(14) << setprecision(6) << fixed << atan(x) << " |"
             << setw(14) << setprecision(6) << fixed << s << " |"
             << setw(8) << n << " |" << endl;
        x += dx;
    }
    cout << "--------------------------------------------------------" << endl;

    return 0;
}
#endif
