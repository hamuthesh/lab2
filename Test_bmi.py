import bmi as bmi

def test_bmi_normal_weight():
    expected_result = 0
    test_height = 1.65
    test_weight = 60
    test_result = bmi.calculate_bmi(test_height, test_weight)
    assert (expected_result == test_result)

def test_bmi_over_weight():
    expected_result = 1
    test_height = 1.90
    test_weight = 120
    test_result = bmi.calculate_bmi(test_height, test_weight)
    assert (expected_result == test_result)

def test_bmi_under_weight():
    expected_result = -1
    test_height = 1.80
    test_weight = 40
    test_result = bmi.calculate_bmi(test_height, test_weight)
    assert (expected_result == test_result)