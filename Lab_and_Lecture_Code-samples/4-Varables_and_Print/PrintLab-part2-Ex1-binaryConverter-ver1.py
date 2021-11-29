numberIn = int(input("enter an 8 digit binary number "))
digit_1 = numberIn % 10
numberIn = numberIn // 10
digit_2 = numberIn % 10
numberIn = numberIn // 10
digit_3 = numberIn % 10
numberIn = numberIn // 10
digit_4 = numberIn % 10
numberIn = numberIn // 10
digit_5 = numberIn % 10
numberIn = numberIn // 10
digit_6 = numberIn % 10
numberIn = numberIn // 10
digit_7 = numberIn % 10
numberIn = numberIn // 10
digit_8 = numberIn % 10
numberIn = numberIn // 10

print("the unsigned binary number ", digit_8, digit_7, digit_6, digit_5, digit_4, digit_3, digit_2, digit_1)
total = digit_1 * 1 
total += digit_2 * 2
total += digit_3 * 4
total += digit_4 * 8
total += digit_5 * 16
total += digit_6 * 32
total += digit_7 * 64
total += digit_8 * 128
print("equals the decimal number", total)