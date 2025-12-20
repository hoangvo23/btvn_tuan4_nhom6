#Hằng số giảm trừ
Giam_tru_ban_than = 11000000
Giam_tru_nguoi_phu_thuoc = 4400000

def tinh_thue(Tien):
    if Tien <= 0:
        return 0
    elif Tien <= 5000000:
        return Tien * 0.05
    elif Tien <= 10000000:
        return 250000 + (Tien - 5000000) * 0.1
    elif Tien <= 18000000:
        return 750000 + (Tien - 10000000) * 0.15
    elif Tien <= 32000000:
        return 1950000 + (Tien - 18000000) * 0.2
    elif Tien <= 52000000:
        return 4750000 + (Tien - 32000000) * 0.25
    elif Tien <= 80000000:
        return 9750000 + (Tien - 52000000) * 0.3
    else:
        return 18150000 + (Tien - 80000000) * 0.35

def nhap_so(cau_hoi):
    while True:
        try:
            du_lieu = int(input(cau_hoi))
            if du_lieu < 0:
                print("Vui lòng nhập số dương!")
            else:
                return du_lieu
        except ValueError:
            print("Vui lòng chỉ nhập số, Không nhập chữ và kí tự khác!")

def main():
    bang_thu_nhap = {}
    
    Ten_nguoi = input("Họ và tên: ")
    Nam_tinh_thue = 2025 
    So_nguoi_phu_thuoc = nhap_so("Số người phụ thuộc: ")
    
    print("\n----- Nhập Lương 12 tháng (Năm 2025) -----")
    for thang in range(1, 13):
        tien = nhap_so(f"Nhập thu nhập tháng {thang}: ")
        bang_thu_nhap[thang] = tien

    print("\n" + "="*20 + " BẢNG QUYẾT TOÁN THUẾ NĂM " + "="*20)
    print(f"Họ và tên: {Ten_nguoi}")
    print(f"Năm tính thuế: {Nam_tinh_thue}")
    print(f"Số người phụ thuộc: {So_nguoi_phu_thuoc}")
    print("-" * 60)
    print(f"| {'Tháng':^10} | {'Thu Nhập(VNĐ)':^20} | {'Thuế tạm tính(VNĐ)':^20} |")
    print("-" * 60)
    
    Tong_thu_nhap = 0
    Tong_thue_tam_tinh = 0
    Giam_tru_gia_canh = Giam_tru_ban_than + So_nguoi_phu_thuoc * Giam_tru_nguoi_phu_thuoc
    
    for thang in range(1, 13):
        thu_nhap = bang_thu_nhap[thang]
        
        thu_nhap_tinh_thue = thu_nhap - Giam_tru_gia_canh
        if thu_nhap_tinh_thue < 0:
            thu_nhap_tinh_thue = 0
        
        tien_thue = tinh_thue(thu_nhap_tinh_thue)
        
        Tong_thue_tam_tinh += tien_thue
        Tong_thu_nhap += thu_nhap
        print(f"| {thang:^10} | {thu_nhap:>20,} | {tien_thue:>20,.0f} |")
    
    print("-" * 60)
    print(f"| {'Tổng':^10} | {Tong_thu_nhap:>20,} | {Tong_thue_tam_tinh:>20,.0f} |")
    print("-" * 60)
    
    Tong_giam_tru_nam = Giam_tru_gia_canh * 12
    Thu_nhap_tinh_thue_nam = Tong_thu_nhap - Tong_giam_tru_nam
    
    if Thu_nhap_tinh_thue_nam < 0:
        Thu_nhap_tinh_thue_nam = 0

    Tong_thue_thuc_te = tinh_thue(Thu_nhap_tinh_thue_nam / 12) * 12
    do_lech = Tong_thue_thuc_te - Tong_thue_tam_tinh
    
    print("\nKẾT QUẢ QUYẾT TOÁN:")
    if do_lech > 0:
        print(f"   Cần nộp thêm: {do_lech:,.0f} VNĐ")
    elif do_lech < 0:
        print(f"   Được hoàn trả: {abs(do_lech):,.0f} VNĐ")
    else:
        print("   Đã nộp đủ thuế.")

if __name__ == "__main__":
    main()