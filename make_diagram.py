# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

w, h = 1000, 640
img = Image.new('RGB', (w, h), (255, 255, 255))
draw = ImageDraw.Draw(img)

font_title = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 16)
font_bold = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 13)
font_code = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 12)
font_label = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 12)

# Background border
draw.rectangle([5, 5, w-5, h-5], outline=(210, 210, 210), width=1)

# Title
draw.text((w/2 - 230, 15), 'Структурна схема багатомодульної програми (Лаб. 9.1)', font=font_title, fill=(20, 20, 20))

def draw_block(x, y, bw, bh, header_text, file_h_text, file_cpp_text, color_head):
    # Header box (module name)
    draw.rectangle([x, y, x + bw, y + 26], fill=color_head, outline=(60, 60, 60), width=1)
    draw.text((x + 8, y + 5), header_text, font=font_bold, fill=(255, 255, 255))
    
    # Body box
    mid_y = y + 26 + (bh - 26) // 2
    draw.rectangle([x, y + 26, x + bw, y + bh], fill=(250, 250, 252), outline=(60, 60, 60), width=1)
    
    # Split line between .h and .cpp
    draw.line([x, mid_y, x + bw, mid_y], fill=(190, 190, 190), width=1)
    
    # .h section
    for idx, line in enumerate(file_h_text):
        draw.text((x + 8, y + 30 + idx * 16), line, font=font_code, fill=(30, 30, 30))
        
    # .cpp section
    for idx, line in enumerate(file_cpp_text):
        draw.text((x + 8, mid_y + 6 + idx * 16), line, font=font_code, fill=(30, 30, 30))

# Blocks layout:
# 1. Main module (top left)
draw_block(30, 60, 280, 220, 'Головний модуль (програма)',
           ['// LABA-9.1.cpp', '#include "sum.h"', '#include "var.h"'],
           ['int main() {', '    cin >> x_p >> ...;', '    sum();', '    cout << x << s << n;', '    return 0;', '}'],
           (41, 128, 185))

# 2. Module sum (top middle)
draw_block(360, 60, 290, 220, 'Модуль sum (обчислення суми)',
           ['// sum.h', 'namespace nsSum {', '    void sum();', '}'],
           ['// sum.cpp', 'void nsSum::sum() {', '    n = 0; a = -1/x;', '    s = -pi/2 + a;', '    do { n++; dod(); s += a; }', '    while(fabs(a) > e);', '}'],
           (39, 174, 96))

# 3. Module dod (top right)
draw_block(700, 60, 270, 220, 'Модуль dod (доданок)',
           ['// dod.h', 'namespace nsDod {', '    void dod();', '}'],
           ['// dod.cpp', 'void nsDod::dod() {', '    a *= - (2n-1)/(2n+1)', '              / (x*x);', '}'],
           (211, 84, 0))

# 4. Module var (bottom center, shared global variables)
draw_block(180, 350, 640, 210, 'Модуль var (спільні ресурси проекту — глобальні змінні простору nsVar)',
           ['// var.h  -- заголовочний файл (оголошення ресурсів)', 'namespace nsVar {', '    extern int n;', '    extern double x, x_p, x_k, dx, e, a, s;', '}'],
           ['// var.cpp -- файл реалізації (визначення ресурсів)', 'namespace nsVar {', '    int n;', '    double x, x_p, x_k, dx, e, a, s;', '}'],
           (142, 68, 173))

# Connecting arrows:
# Arrow from Main to sum()
draw.line([310, 160, 360, 160], fill=(200, 0, 0), width=2)
draw.polygon([(360, 160), (348, 154), (348, 166)], fill=(200, 0, 0))
draw.text((312, 138), 'виклик', font=font_label, fill=(180, 0, 0))
draw.text((312, 168), 'sum()', font=font_label, fill=(180, 0, 0))

# Arrow from sum() to dod()
draw.line([650, 160, 700, 160], fill=(200, 0, 0), width=2)
draw.polygon([(700, 160), (688, 154), (688, 166)], fill=(200, 0, 0))
draw.text((652, 138), 'виклик', font=font_label, fill=(180, 0, 0))
draw.text((652, 168), 'dod()', font=font_label, fill=(180, 0, 0))

# Data access arrows from var:
# var -> Main
draw.line([300, 350, 190, 280], fill=(0, 100, 200), width=2)
draw.polygon([(190, 280), (196, 292), (205, 284)], fill=(0, 100, 200))
draw.text((150, 310), 'nsVar (x_p, x_k, s, n)', font=font_label, fill=(0, 80, 180))

# var -> sum
draw.line([505, 350, 505, 280], fill=(0, 100, 200), width=2)
draw.polygon([(505, 280), (499, 292), (511, 292)], fill=(0, 100, 200))
draw.text((515, 310), 'nsVar (n, a, s, x, e)', font=font_label, fill=(0, 80, 180))

# var -> dod
draw.line([710, 350, 820, 280], fill=(0, 100, 200), width=2)
draw.polygon([(820, 280), (805, 284), (814, 292)], fill=(0, 100, 200))
draw.text((770, 310), 'nsVar (a, n, x)', font=font_label, fill=(0, 80, 180))

# Legend
draw.rectangle([50, 585, 70, 597], fill=(200, 0, 0))
draw.text((80, 584), '— звертання (виклик функцій між модулями)', font=font_label, fill=(50, 50, 50))

draw.rectangle([450, 585, 470, 597], fill=(0, 100, 200))
draw.text((480, 584), '— доступ до спільних глобальних даних простору nsVar', font=font_label, fill=(50, 50, 50))

out_dir = r'C:\Users\User\OneDrive\Документи\лаби\LABA-9.1\images'
img.save(f'{out_dir}\\struct.png')
img.save(f'{out_dir}\\structural_scheme.png')
print('Successfully saved struct.png and structural_scheme.png')
