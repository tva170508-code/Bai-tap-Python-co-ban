# Bài 2: Tính tổng hai số

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

tong = a + b
hieu = a - b
tich = a * b

print("Tổng =", tong)
print("Hiệu =", hieu)
print("Tích =", tich)

if b != 0:
    print("Thương =", a / b)
else:
    print("Không thể chia cho 0")
