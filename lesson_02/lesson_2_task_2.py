def is_year_leap(y):
    return True if y % 4 == 0 else False


year = int(input("Введите год: "))
result_year = is_year_leap(year)
print(f"год {year}: {result_year}")
