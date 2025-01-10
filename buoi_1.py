import math

# ========== Chuyen doi giay ===========

# def chuyen_doi_giay(giay):
#     gio = giay // 3600
#     phut = (giay % 3600) // 60
#     giay_con_lai = giay % 60
#     return f"{gio}:{phut}:{giay_con_lai}"

# so_giay = int(input("Nhập số giây cần chuyển đổi: "))
# ket_qua = chuyen_doi_giay(so_giay)
# print("Kết quả:", ket_qua)


# ========== Tinh dien tich, chu vi ===========

# print("{0:>11}".format("Hello"))
# pi = 3.14
# try:
#     r = float(input("Nhap ban kinh hinh tron: "))
#     print("Dien tich hinh tron la: ", pi * r * r)
#     print("Chu vi hinh tron la: ", 2 * pi * r)
# except ValueError:
#      print("Loi: Ban phai nhap so hop le!")

# def tinh_dien_tich(r):
#     return round(math.pi * (r**2), 2)

# def tinh_chu_vi(r):
#     return round(2 * math.pi * r, - 2)

# def main():
#     """Hàm chính để nhập dữ liệu và gọi các hàm tính toán"""
#     try:
#         r = int(input("Nhập bán kính hình tròn: "))
#         print("Diện tích hình tròn là:", tinh_dien_tich(r))
#         print("Chu vi hình tròn là:", tinh_chu_vi(r))
#     except ValueError:
#         print("Lỗi: Bạn phải nhập một số  hợp lệ!")

# main()


# =========== Tinh diem trung binh ===========
# try:
#     toan = float(input("Nhap diem toan: "))
#     ly = float(input("Nhap diem ly: "))
#     hoa = float(input("Nhap diem hoa: "))
#     dtb = (toan + ly + hoa) / 3
#     print("Diem trung binh la: ", round(dtb, 2))
# except ValueError:
#     print("Loi: Ban phai nhap so hop le!")


# =========== Tim so lon nhat ===========

# try:
#     a = float(input("Nhap so thu nhat: "))
#     b = float(input("Nhap so thu hai: "))
#     c = float(input("Nhap so thu ba: "))

#     maxValue = a
#     for i in [a, b, c]:
#         if i > maxValue:
#             maxValue = i

#     print("So lon nhat la: ", maxValue)
# except ValueError:
#     print("Loi: Ban phai nhap so hop le!")

# ========== Tim ngay cua thang ===========

# try: 
#     thang = int(input("Nhap thang: "))

#     if(thang == 2):
#         nam = int(input("Nhap nam: "))
#         if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0:
#             print("Ngay cua thang la: 29")
#         else:
#             print("Ngay cua thang la: 28")

#     elif thang in [4, 6, 9, 11]:
#         print("Ngay cua thang la: 30")
#     else:
#         print("Ngay cua thang la: 31")
# except:
#     print("Loi: Ban phai nhap so hop le!")


# twinkies = float(input("Nhap so luong twinkies: "))

# if(twinkies < 100 or twinkies > 500):
#     print("Tin nhan qua it hoac qua nhieu")



