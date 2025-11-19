# import pytest
from string_processor import StringProcessor

stringprocessor = StringProcessor()

# @pytest.mark.parametrize('text, processed_text', [("погода", "Погода."), ("хорошая погода", "Хорошая погода."), ("Хорошая погода.", "Хорошая погода.")])
# def positive_tests(text, processed_text):
#     stringprocessor = StringProcessor()
#     result = stringprocessor.process(text)
#     assert result == processed_text


def positive_test():
    stringprocessor = StringProcessor()
    res = stringprocessor.process("погода")
    assert res == "Погода."
