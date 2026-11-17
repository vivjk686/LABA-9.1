#include "pch.h"
#include "CppUnitTest.h"
#include <cmath>
#include "../LABA-9.1/var.h"
#include "../LABA-9.1/dod.h"
#include "../LABA-9.1/sum.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;
using namespace nsVar;
using namespace nsDod;
using namespace nsSum;

namespace UnitTest91
{
    TEST_CLASS(UnitTest91)
    {
    public:
        TEST_METHOD(TestDodRecurrence)
        {
            // Тестування рекурентного розрахунку доданків для x = -2.0
            x = -2.0;
            n = 0;
            a = -1.0 / x; // a_0 = 0.5
            
            // Перший крок: n = 1, очікуване a_1 = 1 / (3 * (-2)^3) = -1/24
            n = 1;
            dod();
            Assert::IsTrue(fabs(a - (-1.0 / 24.0)) < 1e-7);

            // Другий крок: n = 2, очікуване a_2 = -1 / (5 * (-2)^5) = 1/160 = 0.00625
            n = 2;
            dod();
            Assert::IsTrue(fabs(a - (1.0 / 160.0)) < 1e-7);

            // Третій крок: n = 3, очікуване a_3 = 1 / (7 * (-2)^7) = -1/896
            n = 3;
            dod();
            Assert::IsTrue(fabs(a - (-1.0 / 896.0)) < 1e-7);
        }

        TEST_METHOD(TestSumTaylorSeriesConvergence)
        {
            // Перевірка збіжності суми ряду Тейлора до atan(x) для x = -2.0
            x = -2.0;
            e = 1e-6;
            sum();

            double exact = atan(x);
            Assert::IsTrue(fabs(s - exact) < 1e-5);
            Assert::IsTrue(n > 0);
        }

        TEST_METHOD(TestSumVariousPoints)
        {
            // Перевірка обчислення для кількох точок інтервалу x < -1
            e = 1e-5;

            // Точка x = -1.5
            x = -1.5;
            sum();
            Assert::IsTrue(fabs(s - atan(x)) < 1e-4);

            // Точка x = -3.0
            x = -3.0;
            sum();
            Assert::IsTrue(fabs(s - atan(x)) < 1e-4);

            // Точка x = -5.0
            x = -5.0;
            sum();
            Assert::IsTrue(fabs(s - atan(x)) < 1e-4);
        }

        TEST_METHOD(TestTermsCountPositive)
        {
            x = -4.0;
            e = 0.0001;
            sum();
            Assert::IsTrue(n >= 1);
            Assert::IsTrue(s < 0.0);
        }
    };
}
