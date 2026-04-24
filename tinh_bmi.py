# Bài 3 - Phạm Tùng Lâm


def tinh_bmi(can_nang, chieu_cao):
    """
    Tính chỉ số BMI theo công thức: BMI = cân nặng / chiều cao²
    Raises ZeroDivisionError nếu chiều cao = 0
    """
    return can_nang / (chieu_cao ** 2)


def phan_loai_bmi(bmi):
    """
    Phân loại chỉ số BMI và trả về (nhãn, biểu tượng, lời khuyên).
    """
    if bmi < 18.5:
        return "GẦY", "", "Bạn nên bổ sung dinh dưỡng và tăng cường ăn uống hợp lý."
    elif 18.5 <= bmi <= 24.9:
        return "BÌNH THƯỜNG", "", "Tuyệt vời! Hãy duy trì lối sống lành mạnh hiện tại."
    else:
        return "THỪA CÂN", "", "Bạn nên điều chỉnh chế độ ăn và tăng cường vận động."


def nhap_so_thuc(thong_bao):
    """
    Nhập một số thực từ người dùng với xử lý lỗi:
    - ValueError: nhập chữ thay vì số
    - Vòng lặp cho đến khi nhập đúng
    """
    while True:
        try:
            gia_tri = float(input(thong_bao))
            return gia_tri
        except ValueError:
            print("  ❌ Lỗi: Vui lòng nhập một số hợp lệ (ví dụ: 65 hoặc 1.70), không nhập chữ!\n")


def hien_thi_ket_qua(can_nang, chieu_cao, bmi, nhan, bieu_tuong, loi_khuyen):
    """In bảng kết quả phân tích BMI."""
    print("\n" + "=" * 50)
    print("           KẾT QUẢ TÍNH CHỈ SỐ BMI")
    print("=" * 50)
    print(f"   Cân nặng   : {can_nang} kg")
    print(f"   Chiều cao  : {chieu_cao} m")
    print(f"   Chỉ số BMI : {bmi:.2f}")
    print("-" * 50)
    print(f"  {bieu_tuong} Phân loại    : {nhan}")
    print(f"   Lời khuyên : {loi_khuyen}")
    print("=" * 50)


def hien_thi_bang_phan_loai():
    """In bảng phân loại BMI tham khảo."""
    print("\n   BẢNG PHÂN LOẠI BMI THAM KHẢO:")
    print("  " + "-" * 35)
    print("    Gầy          : BMI < 18.5")
    print("    Bình thường  : 18.5 – 24.9")
    print("    Thừa cân     : BMI ≥ 25.0")
    print("  " + "-" * 35)


def main():
    print("=" * 50)
    print("     CÔNG CỤ TÍNH CHỈ SỐ BMI THÔNG MINH")
    print("=" * 50)

    hien_thi_bang_phan_loai()

    print("\n  Nhập thông tin của bạn:\n")

    # Nhập cân nặng — xử lý ValueError bên trong hàm nhap_so_thuc
    can_nang = nhap_so_thuc("  Cân nặng (kg): ")

    # Nhập chiều cao — xử lý cả ValueError lẫn ZeroDivisionError
    while True:
        chieu_cao = nhap_so_thuc("  Chiều cao (m): ")

        try:
            bmi = tinh_bmi(can_nang, chieu_cao)
            break  # Tính thành công → thoát vòng lặp

        except ZeroDivisionError:
            print("   Lỗi: Chiều cao không thể bằng 0! Vui lòng nhập lại.\n")

    # Phân loại và hiển thị kết quả
    nhan, bieu_tuong, loi_khuyen = phan_loai_bmi(bmi)
    hien_thi_ket_qua(can_nang, chieu_cao, bmi, nhan, bieu_tuong, loi_khuyen)


if __name__ == "__main__":
    main()
