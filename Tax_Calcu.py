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
            du_lieu =  int(input(cau_hoi))
            if du_lieu < 0:
                print("Vui lòng nhập số dương!")
            else:
                return du_lieu
        except ValueError:
            print("Vui lòng chỉ nhập số, Không nhập chữ và kí tự khác!")

def main():
    bang_thu_thap = {}
    Ten_nguoi = input("Họ và tên: ")
    Nam_tinh_thue = nhap_so("Năm tính thuế: ")
    So_nguoi_phu_thuoc = nhap_so("Số người phụ thuộc: ")
    print("----- Nhập Lương 12 tháng -----")
    for thang in range(1,13):
        tien = nhap_so(f"Nhập thu thập tháng {thang}: ")
        bang_thu_thap[thang] = tien
    print("===== Bảng Thuế Cả Năm =====")
    print(f"Họ và tên: {Ten_nguoi}")
    print(f"Năm tính thuế: {Nam_tinh_thue}")
    print(f"Số người phụ thuộc: {So_nguoi_phu_thuoc}")
    print("-" * 60)
    print(f"| {"THÁNG":^10} | {"THU THẬP (VNĐ)":^20} | {"THUẾ TẠM TÍNH(VNĐ)":^20}")
    print("-" * 60)
    Tong_thu_thap = 0
    Tong_thue_tam_tinh = 0
    for thang in range(1,13):
        thu_thap = bang_thu_thap[thang]
        tien_thue = 0
        if thu_thap <= (11000000 + So_nguoi_phu_thuoc * 4400000):
            tien_thue = 0
        else:
            tien_thue = tinh_thue(thu_thap)
            Tong_thue_tam_tinh += tien_thue
        Tong_thu_thap += thu_thap
        print(f"| {thang:^10} | {thu_thap:>20,} | {tien_thue:>20,.0f} |")
    print("-" * 60)
    print(f"| {"TỔNG":^10} | {Tong_thu_thap:>20,} | {Tong_thue_tam_tinh:>20,.0f} |")
    print("-" * 60)
    Tong_giam_tru_nam = (11000000 * 12) + (So_nguoi_phu_thuoc * 12 * 4400000)
    TNCT_trung_binh_thang = Tong_thu_thap - Tong_giam_tru_nam
    Tong_thue_thuc_te = tinh_thue(TNCT_trung_binh_thang / 12) * 12
    do_lech = Tong_thue_thuc_te - Tong_thue_tam_tinh
    if do_lech < 0:
        print(f"Cần nộp thêm: {(Tong_thue_tam_tinh - Tong_thue_thuc_te):,.0f} VNĐ")
    elif do_lech > 0:
        print(f"Được hoàn trả: {(Tong_thue_thuc_te - Tong_thue_tam_tinh):,.0f} VNĐ")
    else:
        print("Đã nộp đủ")
if __name__ == "__main__":
    main()
