from power import power

def test_power_base_cases():
    assert power(2, 1) == 2
    assert power(3, 1) == 3
    assert power(5, 1) == 5
    assert power(10, 1) == 10

def test_power_small_exponents():
    assert power(2, 2) == 4
    assert power(2, 3) == 8
    assert power(2, 4) == 16
    assert power(2, 5) == 32
    assert power(3, 2) == 9
    assert power(3, 3) == 27
    assert power(3, 4) == 81
    assert power(5, 2) == 25
    assert power(5, 3) == 125

def test_power_negative_base():
    assert power(-2, 1) == -2
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8
    assert power(-2, 4) == 16
    assert power(-2, 5) == -32
    assert power(-3, 2) == 9
    assert power(-3, 3) == -27

def test_power_fractional_base():
    assert power(0.5, 1) == 0.5
    assert abs(power(0.5, 2) - 0.25) < 1e-10
    assert abs(power(0.5, 3) - 0.125) < 1e-10
    assert abs(power(1.5, 2) - 2.25) < 1e-10
    assert abs(power(1.5, 3) - 3.375) < 1e-10

def test_power_zero_base():
    assert power(0, 1) == 0
    assert power(0, 2) == 0
    assert power(0, 5) == 0

def test_power_one_base():
    assert power(1, 1) == 1
    assert power(1, 2) == 1
    assert power(1, 10) == 1

def test_power_larger_exponents():
    assert power(2, 10) == 1024
    assert power(3, 5) == 243
    assert power(4, 4) == 256
    assert power(5, 3) == 125

def test_power_edge_cases():
    assert abs(power(0.1, 2) - 0.01) < 1e-10
    assert abs(power(0.1, 3) - 0.001) < 1e-10
    assert power(10, 2) == 100
    assert power(10, 3) == 1000
