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



don_vi = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
chuc = ["", "Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi", "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]

def doc_chu_so (number):
    hang_chuc = number // 10
    hang_don_vi = number % 10
    if(hang_chuc == 1 and hang_don_vi == 0):
        return "Mười"
    elif hang_don_vi == 1:
        return chuc[hang_chuc] + " Mốt"
    elif hang_chuc == 1:
        return "Mười" + don_vi[hang_don_vi]    
    elif hang_chuc == 0:
        return don_vi[hang_don_vi]
    else:
        if hang_don_vi == 0:
            return chuc[hang_chuc]
        else:
            return chuc[hang_chuc] + " " + don_vi[hang_don_vi]
        
try: 
    number = int(input("nhap vao so 2 chu so: "))
    print(doc_chu_so(number))
except:
    print("Loi: Ban phai nhap so hop le!")



from datetime import datetime, timedelta

def tim_ngay_ke_tiep(day, month, year):
    current_date = datetime(year, month, day)
    
    next_day = current_date + timedelta(days=1)
    
    return next_day.day, next_day.month, next_day.year

try:
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    
    if 1 <= month <= 12 and 1 <= day <= 31:
        next_day, next_month, next_year = tim_ngay_ke_tiep(day, month, year)
        print(f"Ngày tiếp theo là: {next_day}/{next_month}/{next_year}")
    else:
        print("Lỗi: Ngày, tháng, năm không hợp lệ!")
except ValueError:
    print("Lỗi: Bạn phải nhập số hợp lệ!")