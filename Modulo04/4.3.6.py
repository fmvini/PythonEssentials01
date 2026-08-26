def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = days[month - 1]
    if month == 2 and is_year_leap(year):
            return 29
    return result

def day_of_year(year, month, day):
    soma = 0
    for i in range(1, month):
        soma += days_in_month(year, i)
    soma += day
    return soma

print(day_of_year(2000, 12, 31))