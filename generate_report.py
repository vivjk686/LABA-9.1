# -*- coding: utf-8 -*-
import os
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"C:\Users\User\OneDrive\Документи\лаби\LABA-9.1"
IMG_DIR = os.path.join(BASE_DIR, "images")
OUT_DOCX = os.path.join(BASE_DIR, "АП_РІ-13_Шах_ЛР-09.1.docx")

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex="F4F6F8"):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._element.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>\n'
            f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
            f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
            f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
            f'  <w:insideV w:val="none"/>\n'
            f'  <w:left w:val="none"/>\n'
            f'  <w:right w:val="none"/>\n'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def add_p(doc, text="", bold=False, italic=False, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, line_spacing=1.15):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
        r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_h(doc, text, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.color.rgb = RGBColor(0, 51, 102)
    
    if level == 1:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(14)
    elif level == 2:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(12.5)
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_shading(cell, "F8F9FA")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    # Border
    tcPr = cell._element.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:left w:val="single" w:sz="18" w:space="0" w:color="003366"/>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    
    r = p.add_run(code_text)
    r.font.name = 'Consolas'
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(30, 30, 30)
    
    add_p(doc, "", space_after=4)

def add_image_box(doc, img_path, caption, width_inches=6.0):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_inches))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption)
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(10)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(80, 80, 80)

def generate_report():
    doc = docx.Document()
    
    # Page setup - standard A4, 2 cm margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(1.5)
        
    # --- ТИТУЛЬНА СТОРІНКА ---
    add_p(doc, "МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ", bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ «ЛЬВІВСЬКА ПОЛІТЕХНІКА»", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "Кафедра інформаційних систем та мереж", bold=False, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36)
    
    add_p(doc, "ЗВІТ", bold=True, size=20, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, "про виконання лабораторної роботи № 9.1", bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "«Простори імен»", bold=True, size=15, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "з дисципліни", bold=False, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p(doc, "«Алгоритмізація та програмування»", bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=50)
    
    # Table for student & teacher info
    info_tbl = doc.add_table(rows=2, cols=2)
    info_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_tbl.columns[0].width = Inches(3.2)
    info_tbl.columns[1].width = Inches(3.2)
    
    c0 = info_tbl.cell(0, 1)
    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r0 = p0.add_run("Виконав:\nстудент групи РІ-13\nШах Владислав Ігорьович\nВаріант № 32")
    r0.font.name = 'Times New Roman'
    r0.font.size = Pt(12)
    
    c1 = info_tbl.cell(1, 1)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r1 = p1.add_run("Прийняв:\nГригорович В.Г.")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    
    add_p(doc, "", space_after=80)
    add_p(doc, "Львів – 2026", bold=False, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    doc.add_page_break()
    
    # --- 1. МЕТА ТА ТЕОРЕТИЧНІ ВІДОМОСТІ ---
    add_h(doc, "1. Мета роботи та теоретичні відомості", level=1)
    add_p(doc, "Мета роботи: освоїти використання модулів С++ та просторів імен (namespaces), навчитися створювати багатомодульні проекти з фізичним та логічним розділенням коду, відокремлюючи інтерфейсні файли заголовків (.h) від файлів реалізації (.cpp), організовувати спільний доступ до даних через глобальні змінні простору імен та реалізовувати рекурентні алгоритми обчислення нескінченних степеневих рядів.")
    
    add_h(doc, "Теоретичні положення:", level=2)
    add_p(doc, "1. Модульність у C++: реальний програмний проект розподіляється на окремі трансляційні одиниці (модулі). Інтерфейс кожного модуля (оголошення типів, прототипи функцій, оголошення спільних ресурсів зі специфікатором extern) виноситься у заголовний файл (.h), а конкретна реалізація (код функцій, виділення пам'яті під змінні) розміщується у відповідному файлі вихідного коду (.cpp). Захист заголовків від повторного включення здійснюється директивою #pragma once.")
    add_p(doc, "2. Простори імен (namespace): забезпечують логічне групування програмних ресурсів та усувають колізії імен при спільній розробці. Звернення до елементів простору можливе за допомогою бінарної операції розв'язання області видимості (nsVar::x), директиви using namespace або окремих оголошень using. У цій лабораторній роботі виділено три простори: nsVar (глобальні змінні), nsDod (обчислення чергового доданку), nsSum (обчислення суми ряду).")
    add_p(doc, "3. Рекурентні співвідношення: метод ефективного обчислення доданків ряду Тейлора, при якому черговий доданок an отримується множенням попереднього an-1 на коефіцієнт рекурентності R(n, x). Це дозволяє уникнути затратних операцій піднесення до високих степенів та прямого обчислення факторіалів, забезпечуючи високу швидкість та числову стійкість.")
    
    # --- 2. УМОВА ЗАВДАННЯ ---
    add_h(doc, "2. Умова завдання (Варіант № 32)", level=1)
    add_p(doc, "Спільна частина завдання для всіх варіантів:")
    add_p(doc, "Обчислити і вивести на екран у вигляді таблиці значення функції, заданої за допомогою ряду Тейлора, на інтервалі від x_поч до x_кін з кроком dx та точністю e. Параметри x_поч, x_кін, dx, e вводяться з клавіатури. Таблиця має містити заголовок та шапку. Кожний рядок таблиці має містити значення аргументу, значення функції, значення суми ряду та кількість просумованих доданків. Суму ряду Тейлора та значення доданку обчислювати за допомогою допоміжних алгоритмів, реалізованих за допомогою окремих функцій. При обчисленні значення доданків використовувати рекурентні співвідношення. Всю необхідну функціям інформацію слід передавати лише за допомогою глобальних змінних. Кожну функцію слід визначити в окремому модулі, відокремлюючи інтерфейс (файл заголовку .h) від реалізації (файл тексту модуля .cpp). Щоб уникнути конфліктів імен, слід всі глобальні ресурси кожного модуля описувати в окремому просторі імен.")
    
    add_image_box(doc, os.path.join(IMG_DIR, "task_common.png"), "Рис. 1. Загальна умова лабораторної роботи № 9.1 з методичних вказівок", width_inches=6.0)
    
    add_p(doc, "Індивідуальне завдання для Варіанта № 32:")
    add_image_box(doc, os.path.join(IMG_DIR, "task_var32.png"), "Рис. 2. Умова Варіанта № 32 з методичних вказівок (стор. 21)", width_inches=6.0)
    
    add_h(doc, "Математичний аналіз та виведення рекурентної формули:", level=2)
    add_p(doc, "Задано розклад функції арктангенса в степеневий ряд для x < -1:")
    add_p(doc, "arctg(x) = -pi / 2 + sum_{n=0..inf} [ (-1)^(n+1) / ((2n + 1) * x^(2n+1)) ] = -pi/2 - 1/x + 1/(3*x^3) - 1/(5*x^5) + ...")
    add_p(doc, "Постійний базовий доданок: C = -pi / 2 = -2.0 * atan(1.0).")
    add_p(doc, "Початковий доданок ряду (для n = 0):")
    add_p(doc, "a_0 = (-1)^(0+1) / ((2*0 + 1) * x^(2*0+1)) = -1 / (1 * x^1) = -1 / x.")
    add_p(doc, "Початкове значення суми: s = C + a_0 = -pi/2 - 1/x.")
    add_p(doc, "Загальний вираз для n-го та (n-1)-го доданків:")
    add_p(doc, "a_n = (-1)^(n+1) / ((2n + 1) * x^(2n+1)),    a_{n-1} = (-1)^n / ((2n - 1) * x^(2n-1)).")
    add_p(doc, "Знаходимо коефіцієнт рекурентності R = a_n / a_{n-1}:")
    add_p(doc, "R = [(-1)^(n+1) / (-1)^n] * [(2n - 1) / (2n + 1)] * [x^(2n-1) / x^(2n+1)] = - (2n - 1) / (2n + 1) * (1 / x^2).")
    add_p(doc, "Отже, формульне обчислення чергового доданку в функції nsDod::dod():")
    add_p(doc, "a *= - (2.0 * n - 1.0) / (2.0 * n + 1.0) / (x * x);")
    
    # --- 3. СТРУКТУРНА СХЕМА ПРОГРАМИ ---
    add_h(doc, "3. Структурна схема програми", level=1)
    add_p(doc, "Програма побудована за модульним принципом згідно з рекомендаціями лекційного курсу та методичних вказівок викладача Григоровича В.Г. Кожен функціональний блок виділено в окремий фізичний модуль (.h та .cpp) та поміщено у власний простір імен:")
    
    add_image_box(doc, os.path.join(IMG_DIR, "struct.png"), "Рис. 3. Структурна схема взаємодії модулів та просторів імен програми", width_inches=6.2)
    
    add_p(doc, "Опис архітектури модулів та взаємозв'язків:")
    add_p(doc, "• Головний модуль (LABA-9.1.cpp): точка входу в програму (функція main). Отримує від користувача параметри інтервалу (x_p, x_k), крок табулювання (dx) та точність обчислення (e). У циклі викликає функцію sum() та формує вихідну таблицю зі значеннями аргументу x, точного значення atan(x), суми ряду s та кількості доданків n.")
    add_p(doc, "• Модуль sum (sum.h, sum.cpp, простір nsSum): містить функцію void sum(), яка виконує ініціалізацію змінних (n = 0, a = -1/x, s = -pi/2 + a) та в циклі do { n++; dod(); s += a; } while(fabs(a) > e) здійснює накопичення суми ряду Тейлора.")
    add_p(doc, "• Модуль dod (dod.h, dod.cpp, простір nsDod): містить допоміжну функцію void dod(), яка модифікує значення глобальної змінної a, домножуючи її на коефіцієнт рекурентності R(n, x).")
    add_p(doc, "• Модуль var (var.h, var.cpp, простір nsVar): центральний модуль спільних даних проекту. У файлі var.h оголошено зовнішні глобальні змінні (extern int n; extern double x, x_p, x_k, dx, e, a, s;), а у var.cpp виділено пам'ять під ці змінні.")
    
    # --- 4. ТЕКСТ ПРОГРАМИ ---
    add_h(doc, "4. Текст програми", level=1)
    
    add_h(doc, "4.1. Заголовний файл var.h (оголошення спільних ресурсів)", level=2)
    add_code_block(doc, 
"""#pragma once

namespace nsVar {
    extern int n;
    extern double x, x_p, x_k, dx, e, a, s;
}""")

    add_h(doc, "4.2. Файл реалізації var.cpp (виділення пам'яті під глобальні змінні)", level=2)
    add_code_block(doc, 
"""#include "var.h"

namespace nsVar {
    int n;
    double x, x_p, x_k, dx, e, a, s;
}""")

    add_h(doc, "4.3. Заголовний файл dod.h (інтерфейс обчислення доданку)", level=2)
    add_code_block(doc, 
"""#pragma once

namespace nsDod {
    void dod();
}""")

    add_h(doc, "4.4. Файл реалізації dod.cpp (рекурентне обчислення)", level=2)
    add_code_block(doc, 
"""#include "dod.h"
#include "var.h"

using namespace nsVar;

void nsDod::dod() {
    a *= -(2.0 * n - 1.0) / (2.0 * n + 1.0) / (x * x);
}""")

    add_h(doc, "4.5. Заголовний файл sum.h (інтерфейс обчислення суми)", level=2)
    add_code_block(doc, 
"""#pragma once

namespace nsSum {
    void sum();
}""")

    add_h(doc, "4.6. Файл реалізації sum.cpp (накопичення суми ряду Тейлора)", level=2)
    add_code_block(doc, 
"""#include <cmath>
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
}""")

    add_h(doc, "4.7. Головний файл програми LABA-9.1.cpp (функція main, введення та табулювання)", level=2)
    add_code_block(doc, 
"""//////////////////////////////////////////////////////////////////////////////
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
#endif""")

    # --- 5. МОДУЛЬНЕ ТЕСТУВАННЯ ---
    add_h(doc, "5. Модульне тестування (UnitTest9.1)", level=1)
    add_p(doc, "Для верифікації правильності модульної програми розроблено проект модульного тестування UnitTest9.1 з використанням Microsoft Native Unit Test Framework. Тести перевіряють покроковий розрахунок рекурентного доданку, збіжність суми ряду Тейлора до точного математичного значення atan(x), поведінку функції на різних точках робочого інтервалу та коректність лічильника доданків:")
    
    add_code_block(doc, 
"""#include "pch.h"
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
            x = -2.0;
            n = 0;
            a = -1.0 / x; // a_0 = 0.5
            
            n = 1; dod();
            Assert::IsTrue(fabs(a - (-1.0 / 24.0)) < 1e-7);

            n = 2; dod();
            Assert::IsTrue(fabs(a - (1.0 / 160.0)) < 1e-7);

            n = 3; dod();
            Assert::IsTrue(fabs(a - (-1.0 / 896.0)) < 1e-7);
        }

        TEST_METHOD(TestSumTaylorSeriesConvergence)
        {
            x = -2.0;
            e = 1e-6;
            sum();
            Assert::IsTrue(fabs(s - atan(x)) < 1e-5);
            Assert::IsTrue(n > 0);
        }

        TEST_METHOD(TestSumVariousPoints)
        {
            e = 1e-5;
            x = -1.5; sum();
            Assert::IsTrue(fabs(s - atan(x)) < 1e-4);

            x = -3.0; sum();
            Assert::IsTrue(fabs(s - atan(x)) < 1e-4);

            x = -5.0; sum();
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
}""")

    add_p(doc, "Результати автоматизованого тестування (консольна утиліта vstest.console.exe):")
    add_image_box(doc, os.path.join(IMG_DIR, "console_test.png"), "Рис. 4. Успішне проходження всіх модульних тестів проекту", width_inches=6.0)

    # --- 6. РЕЗУЛЬТАТИ ВИКОНАННЯ ПРОГРАМИ ---
    add_h(doc, "6. Результати виконання програми", level=1)
    add_p(doc, "Програма скомпільована у конфігурації Debug x64 та запущена на виконання. Тестовий інтервал: x_p = -4.0, x_k = -1.5, крок dx = 0.5, точність e = 0.0001:")
    
    add_image_box(doc, os.path.join(IMG_DIR, "console_main.png"), "Рис. 5. Консольне вікно виконання програми з таблицею результатів", width_inches=6.0)
    
    add_p(doc, "Аналіз точності отриманих результатів:")
    
    # Table of comparison
    comp_tbl = doc.add_table(rows=7, cols=5)
    comp_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(comp_tbl)
    
    headers = ["x", "arctg(x) (бібліотечне)", "S (ряд Тейлора)", "Похибка |arctg(x) - S|", "n (доданків)"]
    for i, h_text in enumerate(headers):
        cell = comp_tbl.cell(0, i)
        set_cell_shading(cell, "003366")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    data_rows = [
        ["-4.0000", "-1.325818", "-1.325818", "0.000000", "3"],
        ["-3.5000", "-1.292497", "-1.292498", "0.000001", "3"],
        ["-3.0000", "-1.249046", "-1.249051", "0.000005", "3"],
        ["-2.5000", "-1.190290", "-1.190287", "0.000003", "4"],
        ["-2.0000", "-1.107149", "-1.107156", "0.000007", "5"],
        ["-1.5000", "-0.982794", "-0.982777", "0.000017", "8"],
    ]
    
    for row_idx, row_data in enumerate(data_rows, start=1):
        bg = "FFFFFF" if row_idx % 2 != 0 else "F4F6F8"
        for col_idx, cell_data in enumerate(row_data):
            cell = comp_tbl.cell(row_idx, col_idx)
            set_cell_shading(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(cell_data)
            r.font.name = 'Consolas' if col_idx != 4 else 'Times New Roman'
            r.font.size = Pt(10)
            
    add_p(doc, "", space_after=6)
    add_p(doc, "Як видно з таблиці результатів, абсолютна похибка між значенням суми степеневого ряду Тейлора S та бібліотечною функцією atan(x) не перевищує заданої користувачем точності e = 0.0001 для всіх точок робочого діапазону. При наближенні аргументу x до межі збіжності -1.0 кількість доданків n очікувано зростає з 3 до 8, що підтверджує фізичну та математичну коректність реалізованого алгоритму.")

    # --- 7. ПОСИЛАННЯ НА GITHUB ---
    add_h(doc, "7. Посилання на GitHub-репозиторій", level=1)
    add_p(doc, "Вихідний програмний код, заголовочні файли, файли реалізації, проект Visual Studio 2026, юніт-тести та звіт розміщені у віддаленому репозиторії GitHub:")
    add_p(doc, "https://github.com/vivjk686/LABA-9.1", bold=True, size=12, align=WD_ALIGN_PARAGRAPH.LEFT)

    # --- 8. ВІДПОВІДІ НА КОНТРОЛЬНІ ПИТАННЯ ---
    add_h(doc, "8. Відповіді на контрольні питання", level=1)
    
    qa = [
        ("1. Загальний синтаксис опису функцій.",
         "Синтаксис: [тип_повернення] ім'я_функції([список_параметрів]) { [тіло_функції] }. Якщо функція не повертає значення, вказується тип void. У заголовному файлі .h наводиться прототип функції (оголошення), а у файлі .cpp — її тіло (визначення)."),
        
        ("2. Виклики функцій.",
         "Виклик функції здійснюється вказанням її імені (з простором імен або після using namespace) та передачею аргументів у круглих дужках: nsSum::sum(); або sum();. Керування передається в тіло функції, а після його завершення повертається в точку виклику."),
        
        ("3. Передавання інформації у функцію за допомогою значень та за допомогою адрес.",
         "При передачі за значенням створюється локальна копія аргументу, зміни всередині функції не впливають на оригінал. При передачі за адресою (через вказівник або посилання &) функція отримує доступ до оригінальної ділянки пам'яті, що дозволяє змінювати значення або передавати великі структури без копіювання."),
        
        ("4. Формати виводу та їх використання.",
         "У бібліотеці <iomanip> доступні маніпулятори: setw(w) — встановлює мінімальну ширину поля виводу; fixed — задає вивід дійсних чисел у форматі з фіксованою комою; setprecision(p) — задає кількість знаків після коми. Це забезпечує акуратне вирівнювання колонок таблиці."),
        
        ("5. Рекурентні співвідношення та переваги їх використання.",
         "Рекурентне співвідношення пов'язує поточний елемент ряду an з попереднім an-1: an = an-1 * R(n, x). Переваги: відсутність необхідності щоразу з нуля обчислювати степені x^(2n+1) та множники, усунення переповнення при великих n, зведення кожної ітерації до 2–3 простих арифметичних операцій."),
        
        ("6. Розрахунок першого доданку та коефіцієнта рекурентності для свого варіанту завдання.",
         "Для варіанту 32: початковий доданок для n=0: a_0 = -1/x, s = -pi/2 + a_0. Коефіцієнт рекурентності: R = - (2n - 1) / ((2n + 1) * x^2). Черговий доданок обчислюється як: a *= -(2.0*n - 1.0) / (2.0*n + 1.0) / (x*x)."),
        
        ("7. Організація багатомодульних проектів.",
         "Багатомодульний проект поділяється на фізичні одиниці трансляції. Оголошення інтерфейсів виносяться у .h файли із захистом #pragma once. Реалізації функцій та пам'ять під змінні розміщуються у .cpp файлах. Усі .cpp файли компілюються незалежно в .obj, після чого лінкер збирає їх в один виконуваний файл .exe."),
        
        ("8. Визначення простору імен та його призначення.",
         "Синтаксис: namespace name { /* ресурси */ }. Простір імен дозволяє запобігти колізіям (конфліктам) імен, ізолюючи ресурси одного модуля від інших, навіть якщо в різних модулях оголошено змінні чи функції з однаковими назвами."),
        
        ("9. Оголошення та визначення функції у просторі імен.",
         "Оголошення в .h файлі: namespace nsDod { void dod(); }. Визначення в .cpp файлі: void nsDod::dod() { ... } або всередині блоку namespace nsDod { void dod() { ... } }."),
        
        ("10. Використання глобальних змінних у багатомодульних проектах.",
         "Щоб спільна змінна була доступна в кількох модулях і не виникало помилки множинного визначення (LNK2005), у заголовному файлі .h вона оголошується зі специфікатором extern (extern int n;), що повідомляє компілятору про існування змінної без виділення пам'яті. У єдиному файлі .cpp (var.cpp) змінна визначається (int n;), де під неї один раз виділяється пам'ять.")
    ]
    
    for q, a in qa:
        add_p(doc, q, bold=True, size=11, space_before=4, space_after=2)
        add_p(doc, a, bold=False, size=11, space_before=0, space_after=6)

    # --- 9. ВИСНОВКИ ---
    add_h(doc, "9. Висновки", level=1)
    add_p(doc, "Під час виконання лабораторної роботи № 9.1 було здобуто та закріплено практичні навички роботи з багатомодульними С++ проектами та просторами імен namespace.")
    add_p(doc, "1. Згідно з методичними вказівками та лекційним курсом викладача Григоровича В.Г., програму було успішно розбито на фізичні та логічні модулі: інтерфейсні частини (.h) відокремлено від частин реалізації (.cpp). Застосовано три простори імен: nsVar (глобальні змінні проекту з директивою extern), nsDod (рекурентний розрахунок доданку) та nsSum (накопичення суми ряду Тейлора).")
    add_p(doc, "2. Для індивідуального варіанта № 32 (функція arctg(x), x < -1) виведено математичний вираз для базового доданку C = -pi/2, першого доданку a_0 = -1/x та коефіцієнта рекурентності R = -(2n-1)/((2n+1)*x^2), що забезпечило швидке та числово стійке обчислення значення ряду.")
    add_p(doc, "3. Розроблено автоматизовані модульні тести в проекті UnitTest9.1 за допомогою Microsoft Native Unit Test Framework, які підтвердили точність рекурентних кроків та збіжність суми ряду Тейлора до еталонних значень бібліотечної функції atan(x).")
    add_p(doc, "4. Результати обчислень табулювання функції представлено у вигляді відформатованої таблиці, що засвідчило повну відповідність отриманих значень усім вимогам точності.")

    doc.save(OUT_DOCX)
    print("Report saved successfully:", OUT_DOCX)

if __name__ == "__main__":
    generate_report()
