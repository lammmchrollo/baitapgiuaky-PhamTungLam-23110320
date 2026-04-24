# Bài 4 Phạm Tùng Lâm

import random
import time



DANH_SACH_TU = [
    "python", "apple", "river", "cloud", "music",
    "ocean", "tiger", "plant", "earth", "flame"
]

SO_LUOT_SAI_TOI_DA = 5


# ── Hiển thị số lượt sai bằng gạch ngang ─────
HINH_HANGMAN = ["", "-", "--", "---", "----", "-----"]


def chon_tu_ngau_nhien():
    """Chọn ngẫu nhiên một từ từ danh sách."""
    return random.choice(DANH_SACH_TU)


def tao_man_hinh(tu_bi_mat, da_doan):
    """
    Tạo chuỗi hiển thị từ bí mật.
    Chữ đã đoán đúng → hiện chữ, chưa đoán → hiện '_'
    """
    ket_qua = []
    for chu in tu_bi_mat:
        if chu in da_doan:
            ket_qua.append(chu.upper())
        else:
            ket_qua.append("_")
    return "  ".join(ket_qua)


def kiem_tra_thang(tu_bi_mat, da_doan):
    """Trả về True nếu tất cả chữ cái đã được đoán."""
    for chu in tu_bi_mat:
        if chu not in da_doan:
            return False
    return True


def ghi_ket_qua_file(tu_bi_mat, thang, thoi_gian, luot_sai):
    """Ghi kết quả ván chơi vào file ket_qua_hangman.txt."""
    ten_file = "ket_qua_hangman.txt"

    # Đọc lịch sử cũ (nếu có)
    try:
        with open(ten_file, "r", encoding="utf-8") as f:
            noi_dung_cu = f.read()
    except FileNotFoundError:
        noi_dung_cu = ""

    # Định dạng kết quả ván mới
    trang_thai = "THẮNG " if thang else "THUA "
    dong_moi = (
        f"Từ bí mật : {tu_bi_mat.upper()}\n"
        f"Kết quả   : {trang_thai}\n"
        f"Thời gian : {thoi_gian:.1f} giây\n"
        f"Lượt sai  : {luot_sai}/{SO_LUOT_SAI_TOI_DA}\n"
        f"{'-' * 35}\n"
    )

    # Ghi đè toàn bộ (lịch sử + ván mới)
    with open(ten_file, "w", encoding="utf-8") as f:
        tieu_de = " LỊCH SỬ KẾT QUẢ HANGMAN\n" + "=" * 35 + "\n"
        if noi_dung_cu == "":
            f.write(tieu_de)
        else:
            f.write(noi_dung_cu)
        f.write(dong_moi)

    print(f"\n   Kết quả đã được lưu vào file '{ten_file}'")


def main():
    print("=" * 45)
    print("        MINI HANGMAN — ĐOÁN CHỮ CÁI ")
    print("=" * 45)
    print(f"  Mỗi ván có tối đa {SO_LUOT_SAI_TOI_DA} lượt sai.")
    print("  Đoán từng chữ cái để tìm ra từ bí mật!\n")


    tu_bi_mat   = chon_tu_ngau_nhien()
    da_doan     = []          # Các chữ đã đoán (đúng + sai)
    sai         = []          # Chỉ các chữ đoán sai
    luot_sai    = 0
    bat_dau     = time.time()

    while luot_sai < SO_LUOT_SAI_TOI_DA:

        muc_sai = HINH_HANGMAN[luot_sai] if HINH_HANGMAN[luot_sai] else "(chưa có)"
        print(f"  Mức sai: {muc_sai}")


        print(f"  Từ    : {tao_man_hinh(tu_bi_mat, da_doan)}")
        print(f"  Sai   : {', '.join(sai) if sai else '(chưa có)'}")
        print(f"  Lượt sai còn lại: {SO_LUOT_SAI_TOI_DA - luot_sai}")
        print()
        nhap = input("  Đoán một chữ cái: ").strip().lower()


        if len(nhap) != 1 or not nhap.isalpha():
            print("    Vui lòng nhập đúng 1 chữ cái!\n")
            continue

        if nhap in da_doan:
            print(f"    Bạn đã đoán chữ '{nhap.upper()}' rồi!\n")
            continue

        da_doan.append(nhap)

        if nhap in tu_bi_mat:
            print(f"   Đúng! Chữ '{nhap.upper()}' có trong từ bí mật.\n")
        else:
            sai.append(nhap.upper())
            luot_sai += 1
            print(f"   Sai! Chữ '{nhap.upper()}' không có trong từ bí mật.\n")


        if kiem_tra_thang(tu_bi_mat, da_doan):
            thoi_gian = time.time() - bat_dau
            muc_sai = HINH_HANGMAN[luot_sai] if HINH_HANGMAN[luot_sai] else "(chưa có)"
            print(f"  Mức sai: {muc_sai}")
            print(f"  {tao_man_hinh(tu_bi_mat, da_doan)}")
            print("\n" + "=" * 45)
            print(f"   CHÚC MỪNG! Bạn đã đoán đúng từ: {tu_bi_mat.upper()}")
            print(f"    Thời gian: {thoi_gian:.1f} giây")
            print(f"   Số lượt sai: {luot_sai}/{SO_LUOT_SAI_TOI_DA}")
            print("=" * 45)
            ghi_ket_qua_file(tu_bi_mat, True, thoi_gian, luot_sai)
            return

    thoi_gian = time.time() - bat_dau
    print(f"  Mức sai: {HINH_HANGMAN[SO_LUOT_SAI_TOI_DA]}")
    print("\n" + "=" * 45)
    print(f"   GAME OVER! Từ bí mật là: {tu_bi_mat.upper()}")
    print(f"    Thời gian: {thoi_gian:.1f} giây")
    print(f"   Số lượt sai: {luot_sai}/{SO_LUOT_SAI_TOI_DA}")
    print("=" * 45)
    ghi_ket_qua_file(tu_bi_mat, False, thoi_gian, luot_sai)


if __name__ == "__main__":
    main()
