from calculator import (
    summation, 
    subtraction, 
    multiplication, 
    division
)

def test_summation():
    
    assert summation(5, 10) == 15
    assert summation(2, 9) == 11
    assert summation(1, 4) == 5

def test_subtraction():
    
    assert subtraction(7, 3) == 4
    assert subtraction(8, 2) == 6
    assert subtraction(21, 22) == -1

def test_multiplication():
    
    assert multiplication(3, 2) == 6
    assert multiplication(8, 2) == 16
    assert multiplication(2, 6) == 12

def test_Division():
    
    assert division(10, 5) == 2
    assert division(12, 3) == 4
    assert division(44, 4) == 11

