import pytest
import inspect
from assignment import only_odd_digits, is_cyclops, is_pandigital

def test1(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("num, expected", [
    (1357975313579, True), 
    (42, False),        
    (9713, True),   
    (71358, False),        
    (8, False),            
    (1, True),        
    (0, False),          
])
def test2(num, expected):
    assert only_odd_digits(num) == expected
    assert check_contains_loop(only_odd_digits)

@pytest.mark.parametrize("num, expected", [
    (0, True),          
    (101, True),       
    (98053, True),        
    (777888999, False),    
    (1056, False),        
    (675409820, False),    
    (505, True),          
    (50005, False),       
])
def test3(num, expected):
    assert is_cyclops(num) == expected
    assert check_contains_loop(is_cyclops)

@pytest.mark.parametrize("num, expected", [
    (123456789, True),      
    (987654321, True),     
    (123455678, False),     
    (2301938, False),      
    (192837465, True),     
    (987612345, True),     
    (111111111, False),     
    (12345678, False),    
    (1123456789, False),    
    (9876543201, False),   
])
def test_is_pandigital(num, expected):
    assert is_pandigital(num) == expected
    assert check_contains_loop(is_pandigital)
