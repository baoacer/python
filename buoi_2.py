don_vi = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
chuc = ["", "Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi", "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]

# def doc_chu_so (number):
#     hang_chuc = number // 10
#     hang_don_vi = number % 10
#     if(hang_chuc == 1 and hang_don_vi == 0):
#         return "Mười"
#     elif hang_don_vi == 1:
#         return chuc[hang_chuc] + " Mốt"
#     elif hang_chuc == 1:
#         return "Mười" + don_vi[hang_don_vi]    
#     elif hang_chuc == 0:
#         return don_vi[hang_don_vi]
#     else:
#         if hang_don_vi == 0:
#             return chuc[hang_chuc]
#         else:
#             return chuc[hang_chuc] + " " + don_vi[hang_don_vi]
        
        
# try: 
#     number = int(input("nhap vao so 2 chu so: "))
#     print(doc_chu_so(number))
# except:
#     print("Loi: Ban phai nhap so hop le!")










# ========== BAI 1 ===========
# ========== Doc so ===========
def doc_so(number):
    hang_chuc = number // 10
    hang_don_vi = number % 10

    if(hang_don_vi == 0):
        return chuc[hang_chuc]
    if(hang_chuc == 1):
        if(hang_don_vi == 5):
            return "Mười lăm"
        if(hang_don_vi == 0):
            return "Mười"
        return "Mười " + don_vi[hang_don_vi]
    return chuc[hang_chuc] + " " + don_vi[hang_don_vi]

# try:
#     number = int(input("Nhap so 2 chu so: "))
#     print(doc_so(number))
# except:
#     print("Loi: Ban phai nhap so hop le!")
    



# ========== BAI 2 ===========
# ========== Tim ngay ke tiep ===========

def tim_ngay_ke_tiep(day, month, year):
    # neu la ngay cuoi cung cua thang thi tang ngay len 1 ngay -> tang thang len 1
    # neu la ngay cuoi cung cua nam -> tang nam len 1 -> ngay = 1 thang = 1
    # neu la thang 2 nam nhuan -> thang co 29 day <> 28
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day == 29:
                return 1, month + 1, year
            return day + 1, month, year
        if day == 28:
            return 1, month + 1, year
        return day + 1, month, year
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if(day == 31 and month == 12):
            return 1, 1, year + 1
        if day == 31:
            return 1, month + 1, year
        return day + 1, month, year
    else:
        if day == 30:
            return 1, month + 1, year
        return day + 1, month, year
        



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