import subprocess
import pytest
import os
import math
from plane_angle import Point
from complex_numbers import Complex


INTERPRETER = 'python'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'fact_it': [
        (1, 1),
        (4, 24),
        (7, 5040),
        (9, 362880),
        (15, 1307674368000),
        (23, 25852016738884976640000)
    ],
    'show_employee': [
        (["Башкатов Никита Валерьевич", '90000'], ["Башкатов Никита Валерьевич: 90000 ₽"]),
        (["Серафимов Абдулла Загирович"], ["Серафимов Абдулла Загирович: 100000 ₽"]),
        (["Новеньков Ифрит Адольфович", ''], ["Новеньков Ифрит Адольфович:  ₽"])
    ],
    'sum_and_sub': [
        ([0, 0], '0 0'),
        ([1, 0], '1 1'),
        ([2, 3], '5 -1'),
        ([3, 3], '6 0'),
        ([13, 5], '18 8')
    ],
    'process_list': [
        ([1, 2, 3, 4, 5], [1, 4, 27, 16, 125]),
        ([6, 3, 14, 11], [36, 27, 196, 1331]),
        ([7, 4, 9, 12, 25], [343, 16, 729, 144, 15625]),
        ([5, 13, 18, 17, 20], [125, 2197, 324, 4913, 400])
    ],
    'my_sum': [
        (['1 2 3 4 5'], 15),
        (['3 1 2'], 6),
        (['7 7 7'], 21),
        (['5 5 5'], 15),
        (['10 10 10'], 30)
    ],
    'my_sum_argv': [
        ([1, 3, 5, 7, 9], 25),
        ([2, 4, 6, 8], 20),
        ([7, 3, 41], 51),
        ([32, 171], 203),
    ],
    'files_sort': [
        (".\\", ['test.log','a.py', 'average_scores.py','b.py','c.py', 'circle_square_mk.py', 'complex_numbers.py', 'email_validation.py', 'fact.py', 'fibonacci.py', 
'file_search.py', 'files_sort.py', 'log_decorator.py', 'my_sum.py', 'my_sum_argv.py', 'people_sort.py', 'phone_number.py', 'plane_angle.py',
'process_list.py', 'show_employee.py', 'sum_and_sub.py', 'test.py', 'a.txt', 'b.txt', 'c.txt', 'text.txt'])
    ],
    'file_search': [
        ('text.txt', ''),
        ('d.txt', 'Файл d.txt не найден'),
        ('e.txt', 'Файл e.txt не найден'),
        ('2.txt', 'Файл 2.txt не найден')
    ],
    'fun': [
        ('nvbashkatov@mospolytech.ru', True),
        ('serg-38@mospolytech.ru', True),
        ('tem_21@mospolytech.ru', True),
        ('flexer228@mail@ru', False),
        ('pimp@mos.ru>', False),
        ('elprimo@pom?ru', False),
        ('eklmn', False),
        ('doter@mos', False),
        ('gerichat@mos.2ru', False),
        ('kukold@pomos2-.ru>', False)
    ],
    'fibonacci': [
        (5, [0, 1, 1, 2, 3]),
        (6, [0, 1, 1, 2, 3, 5]),
        (7, [0, 1, 1, 2, 3, 5, 8])
    ],
    'compute_average_scores': [
        ([(89.0, 90.0, 78.0, 93.0, 80.0), (90.0, 91.0, 85.0, 88.0, 86.0), (91.0, 92.0, 83.0, 89.0, 90.5)], [90.0, 91.0, 82.0, 90.0, 85.5]),
        ([(10, 20, 30), (30, 10, 20), (40, 30, 20), (10, 10, 10), (30, 20, 40)], [24.0, 18.0, 24.0]),
        ([(5, 10), (7, 12)], [6.0, 11.0])
    ],
    'plane_angle': [
        ([Point(0, 7, 1), Point(2, -1, 5), Point(1, 6, 3), Point(3, -9, 8)], 140.76847951640775),
        ([Point(1,2,0), Point(2,2,0), Point(2,3,0), Point(3,3,0)], 180.0),
        ([Point(6,3,0), Point(12,78,0), Point(2,3,10), Point(0,5,7)], 61.19649343422453),
        ([Point(67,0,4), Point(1,6,34), Point(2,3,90), Point(4,5,76)], 35.52562731540138)

    ],
    'sort_phone': [
        (['09035434606', '89258878675', '9195969878'], ['+7 (903) 543-46-06', '+7 (919) 596-98-78', '+7 (925) 887-86-75']),
        (['7856409816', '6745368907', '87810674537'], ['+7 (674) 536-89-07', '+7 (781) 067-45-37', '+7 (785) 640-98-16']),
        (['05643189509', '06734256410'], ['+7 (564) 318-95-09', '+7 (673) 425-64-10']),
    ],
    'name_format': [
        ([['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']],
            ['Mr. Mike Thomson', 'Ms. Andria Bustle', 'Mr. Robert Bustle']),
        ([['Nikita', 'Bashkatov', '19', 'M'], ['Serg', 'Med', '18', 'M'], ['Maria', 'Cool', '15', 'F']],
            ['Ms. Maria Cool', 'Mr. Serg Med', 'Mr. Nikita Bashkatov'])
    ],
    'comp_operate': [
        ([Complex(2,1), Complex(5,6)], ['7.00+7.00i', '-3.00-5.00i', '4.00+17.00i', '0.26-0.11i', '2.24+0.00i', '7.81+0.00i']),
        ([Complex(7,2), Complex(3,4)], ['10.00+6.00i', '4.00-2.00i', '13.00+34.00i', '1.16-0.88i', '7.28+0.00i', '5.00+0.00i']),
        ([Complex(1,2), Complex(9,0)], ['10.00+2.00i', '-8.00+2.00i', '9.00+18.00i', '0.11+0.22i', '2.24+0.00i', '9.00+0.00i'])
    ],
    'circle_square_mk': [
        ([5, 10000000], 4.0)
    ]
    
}

from fact import fact_it
from show_employee import show_employee
from sum_and_sub import sum_and_sub
from process_list import process_list
from my_sum import my_sum
from my_sum_argv import my_sum_argv
from files_sort import files_sort
from file_search import file_search
from email_validation import fun
from fibonacci import fibonacci
from average_scores import compute_average_scores
from plane_angle import plane_angle
from phone_number import sort_phone
from people_sort import name_format
from complex_numbers import comp_operate
from circle_square_mk import circle_square_mk

@pytest.mark.parametrize("input_data, expected", test_data['fact_it'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['show_employee'])
def test_show_employee(input_data, expected):
    assert show_employee(*input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    assert sum_and_sub(*input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list(input_data, expected):
    assert process_list(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['my_sum'])
def test_my_sum(input_data, expected):
    assert my_sum(*input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['my_sum_argv'])
def test_my_sum_argv(input_data, expected):
    assert my_sum_argv(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['files_sort'])
def test_files_sort(input_data, expected):
    assert files_sort(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['file_search'])
def test_file_search(input_data, expected):
    assert file_search(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['fun'])
def test_fun(input_data, expected):
    assert fun(input_data) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['fibonacci'])
def test_fibonacci(input_data, expected):
    assert fibonacci(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['compute_average_scores'])
def test_compute_average_scores(input_data, expected):
    assert compute_average_scores(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['plane_angle'])
def test_plane_angle(input_data, expected):
    assert plane_angle(*input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['sort_phone'])
def test_sort_phone(input_data, expected):
    assert sort_phone(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['name_format'])
def test_name_format(input_data, expected):
    assert name_format(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['comp_operate'])
def test_complex_actions(input_data, expected):
    assert comp_operate(*input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['circle_square_mk'])
def test_circle_square_mk(input_data, expected):
    assert circle_square_mk(*input_data) == expected