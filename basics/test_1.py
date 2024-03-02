from calc import square

def test_square():
    for i in range(0,12):
        if square(i) != i**2:
            print(f"bad score for:{i}")
    print("test came to end successfully")


def test_square2():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")

    for i in range(0,12):

        try:
            assert square(i) == i**2
        except AssertionError:
            print(f"{i} squared was not {i**2}")

def main():
    test_square()

    test_square2()

main()    

