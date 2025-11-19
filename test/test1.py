import pytest
from string_processor import StringProcessor

@pytest.mark.parametrize(
        'text, result', 
        [("погода", "Погода."), 
         ("хорошая погода", "Хорошая погода."), 
         ("Хорошая погода.", "Хорошая погода.")])
def positive_tests(text, result):
    stringprocessor = StringProcessor()
    stringprocessor.process(text) == result

@pytest.mark.parametrize(
        'text, result', 
        [("", "."), ("     ", ".")])
def negative_tests(text, result):
    stringprocessor = StringProcessor()
    stringprocessor.process(text) == result

def negative_test():
    stringprocessor = StringProcessor()
    with pytest.raises(TypeError):
        stringprocessor.process(123)
