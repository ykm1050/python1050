import calendar
def month(month_name,yr):
    monthnum = list(calendar.month_name).index(month_name)
    return calendar.monthrange(yr,monthnum)[1]
month_name = str(input('enter the month :'))
yr=2024
print(f'no of days in {month_name} {yr} is {month(month_name,yr)}')