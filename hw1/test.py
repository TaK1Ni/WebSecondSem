import subprocess
import pytest

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
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50']),
        (['5', '5'], ['10', '0', '25'])
    ],
    'division': [
        (['3', '5'], ['0', '0.6']),
        (['11', '4'], ['2', '2.75']),
        (['0', '35'], ['0', '0.0']),
        (['5', '0'], ['ноль нельзя']),
    ],
    'loops': [
        (['1'], ['0']),
        (['2'], ['0', '1']),
        (['3'], ['0', '1', '4'])
    ],
    'print_function': [
        (['1'], ['1']),
        (['8'], ['12345678']),
        (['0'], [''])
    ],
    'second_score': [
        (['5', '2 3 6 6 5'], ['5']),
        (['5', '1 2 3 4 5'], ['4']),
        (['0'], ['']),
        (['6', '4 6 52 67 5 27'], ['52'])
    ],
    'nested_list': [
        (['5', 'Гарри', '37.21', 'Берри', '37.21', 'Тина', '37.2', 'Акрити', '41', 'Харш', '39'], ['Харш']),
        (['4', 'chi', '20.0', 'beta', '50.0', 'alpha', '50.0', 'sigma', '80.0'], ['beta', 'alpha'])
    ],
    'lists': [
        (['4', 'append 1', 'append 2', 'insert 1 3', 'print'], ['[1, 3, 2]']),
        (['5', 'insert 0 5', 'insert 1 10', 'print', 'print', 'remove'],
             ['[5, 10]', '[5, 10]'])
    ],
    'swap_case': [
        (['Www.MosPolytech.ru'], ['wWW.mOSpOLYTECH.RU']),
        (['WWWwwwWWW'], ['wwwWWWwww']),
        ([''], ['']),
        (['MINmax'], ['minMAX'])
    ],
    'split_and_join': [
        (['this is a string'], ['this-is-a-string']),
        (['i hz chto pisat'], ['i-hz-chto-pisat']),
        (['for money, yes'], ['for-money,-yes'])
    ],
    'max_word': [
        (['example.txt'], ['сосредоточенности']),
    ],
    'anagram': [
        (['монолог', 'ономгол'], ['YES']),
        [['раз', 'два'], ['NO']],
        (['нет', 'часть'], ['NO']),
        (['да', 'ДА'], ['NO'])
    ],
    'metro': [
        (['2', '4 5', '5 6', '2'], ['0']),
        (['5', '2 8', '3 8', '5 6', '1 2', '3 4', '6'], ['3']),
        (['0', '9'], ['0'])
    ],
    'minion_game': [
        (['BANANA'], ['Выиграл Стюарт с 12']),
        (['APENO'], ['Выиграл Кевин с 9']),
        (['HELLL'], ['Выиграл Стюарт с 11'])
    ],
    'is_leap': [
        (['2024'], ['True']),
        (['1800'], ['False']),
        (['1600'], ['True']),
        (['1200'], ['True']),
        (['3000'], ['False']),
        (['2001'], ['False'])
    ],
    'happiness': [
        (['3 2', '1 5 3', '3 1', '5 7'], ['1']),
        (['7 4', '1 5 7 8 3 90 67', '90 5 2 6', '1 7 67 27'], ['-1']),
        (['5 1', '1 2 3 4 5', '5', '3'], ['0'])
    ],
    'pirate_ship': [
        (['45 4', 'ром 100 200', 'алмазы 2 2000', 'мука 150 400', 'сабли 10 1000'], ['алмазы 2 2000.0', 'сабли 10 1000.0', 'мука 33 88.0']),
        (['500 7', 'крабы 10 500', 'уголь 500 750', 'брилианты 8 10000', 'сапоги 70 1400', 'пистолеты 90 3600', 'вода 500 1000',
           'грибы 2 7500'], ['грибы 2 7500.0', 'брилианты 8 10000.0', 'крабы 10 500.0', 'пистолеты 90 3600.0', 'сапоги 70 1400.0', 'вода 320 640.0'])
    ],
    'matrix_mult': [
        (['3', '3 3 3', '3 3 3', '3 3 3', '3 3 3', '3 3 3', '3 3 3'], ['27 27 27 ', '27 27 27 ', '27 27 27']),
        (['3', '0 0 0', '0 0 0', '0 0 0', '0 0 0', '0 0 0 ', '0 0 0'], ['0 0 0 ', '0 0 0 ', '0 0 0']),
        (['3', '1 1 1', '1 1 1', '1 1 1', '1 1 1', '1 1 1', '1 1 1'], ['3 3 3 ', '3 3 3 ', '3 3 3'])
    ]

}

def test_hello_world():
    assert run_script('hello.py') == 'Hello, World!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['max_word'])
def test_max_word(input_data, expected):
    assert run_script('max_word.py', input_data).split('\n') == expected

def test_price_sum():
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.9'

@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected