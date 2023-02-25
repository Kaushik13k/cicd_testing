from main import Calculator


class TestCalculator:
    def test_add(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(-1, 1) == -2

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(-1, 5) == -5
