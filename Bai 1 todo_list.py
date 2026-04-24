#Bài 1 - Phạm Tùng Lâm

def hien_thi_danh_sach(danh_sach):
    """Hiển thị danh sách công việc ra màn hình."""
    if not danh_sach:
        print("\n  [Danh sách trống. Chưa có công việc nào!]")
    else:
        print("\n   DANH SÁCH CÔNG VIỆC:")
        print("  " + "-" * 35)
        for i, cong_viec in enumerate(danh_sach, start=1):
            print(f"  {i}. {cong_viec}")
        print("  " + "-" * 35)


def luu_vao_file(danh_sach, ten_file="todo_list.txt"):
    """Ghi đè toàn bộ danh sách công việc vào file."""
    with open(ten_file, "w", encoding="utf-8") as f:
        f.write("DANH SÁCH CÔNG VIỆC CẦN LÀM\n")
        f.write("=" * 35 + "\n")
        if danh_sach:
            for i, cong_viec in enumerate(danh_sach, start=1):
                f.write(f"{i}. {cong_viec}\n")
        else:
            f.write("(Danh sách trống)\n")
    print(f"\n   Đã lưu danh sách vào file '{ten_file}' thành công!")


def main():
    danh_sach = []

    print("=" * 45)
    print("       ỨNG DỤNG TO-DO LIST ĐƠN GIẢN")
    print("=" * 45)
    print("  Nhập công việc cần làm, gõ 'xong' để kết thúc.")
    print("  Gõ 'hien' để xem danh sách, 'luu' để lưu file.")
    print("=" * 45)

    while True:
        nhap = input("\n  Nhập công việc (hoặc lệnh): ").strip()

        if nhap == "":
            print("  ⚠️  Vui lòng nhập nội dung công việc!")

        elif nhap.lower() == "xong":
            print("\n  👋 Kết thúc nhập liệu.")
            break

        elif nhap.lower() == "hien":
            hien_thi_danh_sach(danh_sach)

        elif nhap.lower() == "luu":
            hien_thi_danh_sach(danh_sach)
            luu_vao_file(danh_sach)

        else:
            danh_sach.append(nhap)
            print(f"  ➕ Đã thêm: '{nhap}'")

    # Hiển thị và lưu file sau khi kết thúc
    hien_thi_danh_sach(danh_sach)
    luu_vao_file(danh_sach)
    print("\n  Cảm ơn bạn đã sử dụng To-Do List! 🎯\n")


if __name__ == "__main__":
    main()
