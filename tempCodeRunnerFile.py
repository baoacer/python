don_vi = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
# chuc = ["", "Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi", "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]

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