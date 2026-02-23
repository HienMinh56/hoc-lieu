# Chương trình con người dùng nhập và in ra lời chào
# Hình 1 trong SGK trang 87
def Hello():
    hoten = input("Xin cho biết tên bạn: ")
    chaomung = "Xin chào" + hoten
    print(chaomung)
    
Hello()

# Chương trình con giải phương trình bậc nhất
# Hình 2 + 3 trong SGK trang 87
def ptb1():
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    if a != 0:
        print("Nghiệm của phương trình là: ", -b/a)
    elif b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
        
ptb1()

def try_ptb1(a, b):
    if a != 0:
        print("Nghiệm của phương trình là: ", -b/a)
    elif b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
    
try_ptb1(2, 3)

# Chương trình con tính chỉ số sức khỏe BMI
# Hình 4 trong SGK trang 89
def BMI(h, w):
    bmi = w / h ** 2
    print("Chỉ số BMI của bạn là: ", bmi)
    
cao = float(input("Nhập chiều cao của bạn (m): "))
nang = float(input("Nhập cân nặng của bạn (kg): "))
BMI(cao, nang)

# Chương trình con tính tổng chiều cao
def chieu_cao(m ,cm):
    tong = (m * 100) + cm
    return tong
# Nhập dữ iệu để đổi sang cm
m = float(input("Nhập chiều cao của bạn (m): "))
cm = float(input("Nhập chiều cao của bạn (cm): "))
print("Tổng chiều cao của bạn là: ", chieu_cao(m, cm))

# Chương trình tính ước chung lớn nhất
# Hình 7 trong SGK trang 90
# Cách 1
def ucln(a, b):
    u = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            u = i
    return u

# Cách 2
from math import gcd
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
print("Ước chung lớn nhất của", a, "và", b, "là: ", gcd(a, b))

# Bài 1. Với hàm BSCNN được xây dựng ở chương trình sau đây
# (Hình 8), trong những dòng lệnh có sử dụng hàm BSCNN, dòng
# lệnh nào đúng, dòng lệnh nào sai và tại sao? 
from math import gcd

def BSCNN(x, y):
    return x*y // gcd(x, y)

a = int(input("a = "))
b = int(input("b = "))

print("Bội số chung nhỏ nhất: ", BSCNN(a, b))

c = a + b + BSCNN(a, b) # Thiếu truyền tham số a và b
print("c = ", c)

# Bài 2. Chương trình ở (Hình 9), xây dựng một hàm tính diện tích
# một tam giác bằng công thức Heron theo ba cạnh của tam giác. Em
# hãy hoàn thiện chương trình bằng lời gọi hàm thích hợp để đưa ra
# màn hình kết quả diện tích của tam giác có ba cạnh là 3, 4, 5
def dientichtg (a, b, c):
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    return s ** 0.5

print("Dien tich tam giac co ba canh la 3, 4, 5 la: ", dientichtg(3, 4, 5))

# Bài 3. Sử dụng kết quả của Bài 2 phần Luyện tập, em hãy viết
# chương trình giải bai toan ở Hoat động 1
def dientich(a,b,c):
    p = (a+b+c) /2 # => p-a = (b+c-a)/2 ; p-b = (a+c-b)/2 ; p-c = (a+b-c)/2 thế vào công thức heron thì sẽ ra công thức gốc trong HĐ 1
    s = p* (p-a) * (p-b) * (p-c)
    return s ** 0.5
a = float (input ("a = ") )
b = float (input ("b = ") )
c = float (input ("c = ") )
u = float (input ("u = ") )
v = float (input ("v = ") )
w = float (input ("w = ") )
p = float (input ("p = ") )
q = float (input ("q = ") )
r = float (input ("r = ") )
s1 = dientich(a,b,c)
s2 = dientich (u, v,w)
s3 = dientich (p,q,r)
print ("Diện tích của 3 tam giác lần lượt là: ", s1, s2, s3)
print ("Diện tích lớn nhất là: ", max (s1, s2, s3) )