import pytest
from string_processor import StringProcessor

stringprocessor = StringProcessor()

@pytest.mark.parametrize('text, result', [("погода", "Погода."), ("хорошая погода", "Хорошая погода."), ("Хорошая погода.", "Хорошая погода.")])
def positive_tests(text: str, result: str):
    stringprocessor = StringProcessor()
    res = stringprocessor.process(text)
    assert res == result

# def positive_test():
#     stringprocessor = StringProcessor()
#     res = stringprocessor.process("погода")
#     assert res == "Погода."
