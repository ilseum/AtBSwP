def is_phone_number(number):
    if len(number) != 12:
        return False
    for i in range(0, 3):
        if not number[i].isdecimal():
            return False
    if number[3] != '-':
        return False
    for i in range(4, 7):
        if not number[i].isdecimal():
            return False
    if number[7] != '-':
        return False
    for i in range(8, 12):
        if not number[i].isdecimal():
            return False
    return True


print("415-555-4242 is a phone number:")
print(is_phone_number("415-555-4242"))
print("Moshi moshi is a phone number:")
print(is_phone_number("Moshi moshi"))
