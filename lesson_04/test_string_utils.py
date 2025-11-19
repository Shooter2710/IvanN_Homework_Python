import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# CAPITALIZE POSITIVE
@pytest.mark.parametrize("text, result", [
    ("тест", "Тест"),
    ("второй тест", "Второй тест"),
    ("123", "123")])
def pos_capitalize_tests(text, result):
    assert string_utils.capitalize(text) == result


# CAPITALIZE NEGATIVE
@pytest.mark.parametrize("text, result", [
    ("", ""),
    (" ", " "),
    ("[]", "[]")])
def neg_capitalize_tests(text, result):
    assert string_utils.capitalize(text) == result


def neg_capitalize_test():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


# TRIM POSITIVE
@pytest.mark.parametrize("text, result", [
    (" тест", "тест"),
    (" второй тест", "второй тест"),
    (" 123", "123")])
def pos_trim_tests(text, result):
    assert string_utils.trim(text) == result


# TRIM NEGATIVE
@pytest.mark.parametrize("text, result", [
    ("", ""),
    (" ", ""),
    (" []", "[]")])
def neg_trim_tests(text, result):
    assert string_utils.trim(text) == result


def neg_trim_test():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


# CONTAINS POSITIVE
@pytest.mark.parametrize("text, sym, result", [
    ("тест", "е", True),
    ("второй тест", "о", True),
    ("123", "3", True)])
def pos_contains_tests(text, sym, result):
    assert string_utils.contains(text, sym) == result


# CONTAINS NEGATIVE
@pytest.mark.parametrize("text, sym, result", [
    ("", "", True),
    (" ", " ", True),
    ("[]", "[]", True)])
def neg_contains_tests(text, sym, result):
    assert string_utils.contains(text, sym) == result


def neg_contains_test():
    with pytest.raises(AttributeError):
        string_utils.contains(None, None)


# DELETE_SYMBOL POSITIVE
@pytest.mark.parametrize("text, sym, result", [
    ("тест", "е", "тст"),
    ("второй тест", "о", "втрй тест"),
    ("123", "3", "12")])
def pos_delete_symbol_tests(text, sym, result):
    assert string_utils.delete_symbol(text, sym) == result


# DELETE_SYMBOL NEGATIVE
@pytest.mark.parametrize("text, sym, result", [
    ("", "", ""),
    (" ", " ", ""),
    ("[]", "[]", "")])
def neg_delete_symbol_tests(text, sym, result):
    assert string_utils.delete_symbol(text, sym) == result


def neg_delete_symbol_test():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, None)
