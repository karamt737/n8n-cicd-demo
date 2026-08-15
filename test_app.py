from app import calculate_discount, is_valid_email


def test_calculate_discount_basic():
    assert calculate_discount(100, 10) == 90


def test_calculate_discount_zero():
    assert calculate_discount(50, 0) == 50


def test_calculate_discount_full():
    assert calculate_discount(100, 100) == 0


def test_is_valid_email_true():
    assert is_valid_email("karamt@uw.edu") == True


def test_is_valid_email_false():
    assert is_valid_email("not-an-email") == False
