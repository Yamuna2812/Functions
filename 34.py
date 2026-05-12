def leap(year):
    if year % 4 == 0:
        return "Leap Year"
    return "Not Leap Year"

print(leap(2024))
