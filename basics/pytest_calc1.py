from calc import square

def test_square():
    pass
    

def test_square_positives():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

def test_square_negatives():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16

def test_square_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


# def test_argument():
#     for name in ["Hermione", "Harry", "Ron"]:
#         assert fun(name) == f"Hello, {name}"