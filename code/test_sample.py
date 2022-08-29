from calculator import Calculator

def test_add_int():
    obj = Calculator()
    assert obj.add(3,2) == 5

def test_add_float():
    obj = Calculator()
    assert obj.add(3.1,1.1) == 4.2

def test_subtract_int():
    obj = Calculator()
    assert obj.subtract(3,2) == 1

def test_subtract_float():
    obj = Calculator()
    assert obj.subtract(3.1,1.1) == 2.0

def test_multiply_int():
    obj = Calculator()
    assert obj.multiply(3,2) == 6

def test_multiply_float():
    obj = Calculator()
    assert obj.multiply(3.1,1.1) == 3.41

def test_divide_int():
    obj = Calculator()
    assert obj.divide(3,2) == 1.5

def test_divide_float():
    obj = Calculator()
    assert obj.divide(3.1,1.1) == 2.82

def test_divide_by_zero():
    obj = Calculator()
    assert obj.divide(3,0) == 'Cannot divide by 0'