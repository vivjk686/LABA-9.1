#include <cmath>
#include "dod.h"
#include "sum.h"
#include "var.h"

using namespace nsDod;
using namespace nsVar;

void nsSum::sum() {
    n = 0;
    const double PI = 4.0 * atan(1.0);
    a = -1.0 / x;
    s = -PI / 2.0 + a;
    do {
        n++;
        dod();
        s += a;
    } while (fabs(a) > e);
}
