# Bài 1 SGK: Em hãy dự đoán xem chương trình
# ở Hình 1 sau đây sẽ đưa ra màn hình
# những gì. Chạy chương trình để kiểm
# tra kết quả (Stop tại 5)

# i = 1
# total = 0
# while total < 10:
#     i += 1
#     total += i
#     print("i =", i, " total =", total)
    
# Bài 2 SGK: Bạn Hà viết chương trình ở hình 2 để đếm xem số
# nguyên n nhập vào từ bàn phím có bao nhiêu ước số
# thực sự (ước khác 1 và n). Tuy nhiên, chương trình
# chạy kết quả sai. Em hãy sửa lỗi giúp bạn Hà.

# n = int(input("Nhập số n: "))
# i = 2
# so_uoc = 0
# while i <= n // 2: # VD: 9 // 2 = 4 || 9 / 2 = 4.5 đã. Đã sửa thiếu :
#     if n % i == 0:
#         so_uoc += 1
#     i += 1
# print(n, "có số ước thực sự là", so_uoc) # Đã sửa cho ra ngoài while

# Bài 3 SGK: Tham khảo chương trình ở Ví dụ 5 trong Bài 8, em hãy
# viết chương trình yêu cầu người dùng nhập một số
# nguyên lớn hơn 1 000 000. Chừng nào người dùng
# nhập chưa đúng yêu cầu thì có thông báo yêu cầu nhập
# lại, chương trình chỉ kết thúc với dòng thông báo “Cảm
# ơn, bạn đã nhập dữ liệu đúng yêu cầu.” khi số người
# dùng gõ vào thỏa điều kiện đặt ra.

# so_nguyen = int(input("Nhập số nguyên lớn hơn 1 000 000: "))
# while so_nguyen <= 1000000:
#     print("Số bạn nhập chưa đúng yêu cầu, vui lòng thử lại.")
#     so_nguyen = int(input("Nhập số nguyên lớn hơn 1 000 000: "))
# print("Cảm ơn, bạn đã nhập dữ liệu đúng yêu cầu.")

# Bài 4 SGK: Em hãy lập trình giải bài toán cổ ở hình dưới đây một
# cách tống quát bằng cách nhập hai số nguyên dương n,
# m tương ứng là tổng số con và tổng số chân sau đó đưa
# ra màn hình số lượng gà và số lượng chó. Kiểm tra thử
# chương trình với n = 36 và m = 100

# for ga in range(1, 37): # ga từ 1 đến 36
#     cho = 36 - ga
#     if (ga * 2 + cho * 4) == 100:
#         print("Số gà:", ga, "con")
#         print("Số chó:", cho, "con")
#         break

# Bài 5 SGK: Hãy viết chương trình nêu những câu hỏi để
# kiểm tra xem người ngồi trước máy tính có
# thuộc bảng nhân 6 hay không. Chương trình cho
# phép người trả lời bỏ qua một câu hỏi nào đó
# hoặc dừng trả lời

# bang = 6
# for i in range (1, 11):
#     print(bang, "x", i, "= ?")
#     tra_loi = input()
#     if tra_loi == "dừng":
#         break
#     if tra_loi == "bỏ qua":
#         print("Câu tiếp theo:")
#         continue
#     dap_an = i * bang
#     if int(tra_loi) == dap_an:
#         print("Đáp án đúng!")
#     else:
#         print("Đáp án sai. Đáp án đúng là:", dap_an)
# print("Kết thúc chương trình kiểm tra bảng nhân 6.")

# Bài 6: Để thử nghiệm lâm sàng vacxin mới ở giai đoạn 1,
# người ta cần những người trong độ tuổi từ 18 đến 64
# tuối và thỏa mãn điều kiện 18.5 ≤ cân nặng/(chiêu
# cao)2 ≤ 22.9. Theo tập hồ sơ nhận được từ những người
# tình nguyện, hãy đưa ra màn hình số người sẽ được xét
# đế tham gia thử nghiệm. Số liệu về tuổi, cân nặng (kg)
# và chiều cao (m) của mỗi hồ sơ nhập vào từ bàn phím,
# mỗi số trên một dòng. Nhập tuổi bằng 0 để kết thúc tập
# hồ sơ.

p = 1
dem = 0

while True:
    print("Nhập hồ sơ người thứ:", p)
    tuoi = int(input("Nhập tuổi (nhập 0 để kết thúc): "))
    if tuoi == 0:
        break

    can_nang = float(input("Nhập cân nặng (kg): "))
    chieu_cao = float(input("Nhập chiều cao (m): "))

    bmi = can_nang / (chieu_cao ** 2)

    if 18 <= tuoi <= 64 and 18.5 <= bmi <= 22.9:
        dem += 1   # ĐẾM NGƯỜI ĐẠT

    p += 1        # ĐẾM HỒ SƠ

print("Số người được xét để tham gia thử nghiệm là:", dem)

    