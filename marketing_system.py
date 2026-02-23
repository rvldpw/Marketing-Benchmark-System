# DUMMY DATA
# Dataset awal sebagai simulasi database benchmark campaign
benchmarks = [
    {"Tanggal": "2020-01-25", "Kategori": "Imlek", "Platform": "Facebook", "CPR Terbaik": 12000, "Notes": "High season sales spike"},
    {"Tanggal": "2021-02-12", "Kategori": "Imlek", "Platform": "Instagram", "CPR Terbaik": 13500, "Notes": "Engagement strong"},
    {"Tanggal": "2022-02-01", "Kategori": "Imlek", "Platform": "TikTok", "CPR Terbaik": 12500, "Notes": "Video ads worked well"},
    {"Tanggal": "2021-02-14", "Kategori": "Valentine", "Platform": "Instagram", "CPR Terbaik": 17000, "Notes": "Gift trend increased"},
    {"Tanggal": "2021-02-14", "Kategori": "Valentine", "Platform": "Facebook", "CPR Terbaik": 15500, "Notes": "Better reach than IG"},
    {"Tanggal": "2022-02-14", "Kategori": "Valentine", "Platform": "TikTok", "CPR Terbaik": 14800, "Notes": "Short video promo effective"},
    {"Tanggal": "2022-04-03", "Kategori": "Ramadan", "Platform": "TikTok", "CPR Terbaik": 13000, "Notes": "Video content performed well"},
    {"Tanggal": "2023-03-23", "Kategori": "Ramadan", "Platform": "Facebook", "CPR Terbaik": 14500, "Notes": "Conversion focused"},
    {"Tanggal": "2024-03-12", "Kategori": "Ramadan", "Platform": "Google", "CPR Terbaik": 15000, "Notes": "High intent search traffic"},
    {"Tanggal": "2024-05-05", "Kategori": "Company Anniversary", "Platform": "Facebook", "CPR Terbaik": 14000, "Notes": "Big discount campaign"},
    {"Tanggal": "2024-05-05", "Kategori": "Company Anniversary", "Platform": "Instagram", "CPR Terbaik": 13800, "Notes": "Stories ads effective"},
    {"Tanggal": "2024-05-05", "Kategori": "Company Anniversary", "Platform": "Google", "CPR Terbaik": 16500, "Notes": "Search cost higher"},
    {"Tanggal": "2020-09-09", "Kategori": "Marketplace Sale", "Platform": "Shopee Ads", "CPR Terbaik": 9500, "Notes": "9.9 strong marketplace push"},
    {"Tanggal": "2022-11-11", "Kategori": "Marketplace Sale", "Platform": "Shopee Ads", "CPR Terbaik": 9000, "Notes": "11.11 lowest CPR recorded"},
    {"Tanggal": "2021-12-12", "Kategori": "Marketplace Sale", "Platform": "TikTok", "CPR Terbaik": 11000, "Notes": "12.12 flash sale traffic spike"},
    {"Tanggal": "2024-03-03", "Kategori": "Marketplace Sale", "Platform": "Tokopedia Ads", "CPR Terbaik": 10000, "Notes": "3.3 cost efficient campaign"},
    {"Tanggal": "2023-01-01", "Kategori": "New Year", "Platform": "Google", "CPR Terbaik": 21000, "Notes": "Awareness heavy"},
    {"Tanggal": "2024-01-01", "Kategori": "New Year", "Platform": "Google", "CPR Terbaik": 20000, "Notes": "Slightly improved CPR"},
    {"Tanggal": "2023-06-06", "Kategori": "Mid Year Sale", "Platform": "Facebook", "CPR Terbaik": 13500, "Notes": "Stable performance"},
    {"Tanggal": "2022-10-31", "Kategori": "Halloween", "Platform": "Instagram", "CPR Terbaik": 16000, "Notes": "Seasonal promo"},
]

# LIBRARY
# Import dependency yang digunakan dalam program
from collections import defaultdict
from tabulate import tabulate
from datetime import datetime
import pandas as pd

# ID GENERATOR
# Membuat fungsi generator untuk ID unik campaign
def generate_pk(data):
    # Mapping kode singkat platform
    platform_code = {
        "facebook": "FB",
        "instagram": "IG",
        "tiktok": "TT",
        "google": "GG",
        "shopee ads": "SP",
        "tokopedia ads": "TP",
        "youtube": "YT"
    }

    counter = defaultdict(int)  # Counter untuk menjaga keunikan ID

    # Generate ID untuk data awal
    for row in data:
        tanggal = row["Tanggal"].replace("-", "")[2:]
        platform = platform_code.get(row["Platform"].lower(), "XX")
        code = f"{platform}{tanggal}"
        counter[code] += 1
        row["ID"] = f"{code}{counter[code]:04d}"

    # Fungsi untuk generate ID saat menambah data baru
    def generate(platform, tanggal):
        tanggal_format = tanggal.replace("-", "")[2:]
        platform_code_value = platform_code.get(platform.lower(), "XX")
        code = f"{platform_code_value}{tanggal_format}"
        counter[code] += 1
        return f"{code}{counter[code]:04d}"

    return generate

# Inisialisasi generator ID
generate_id = generate_pk(benchmarks)

# LOGIN & PROGRAM STATE
# Variabel global status program dan data user
program_running = True
users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "staff", "password": "staff123", "role": "staff"}
]

# Fungsi autentikasi login
def login():
    print("\n==== Welcome to PWD Marketing System ====\n")

    username_input = input("Username: ").strip()
    password_input = input("Password: ").strip()

    for user in users:
        if user["username"] == username_input and user["password"] == password_input:
            print("\nLogin berhasil!")
            return user["role"]

    print("\nUsername atau password salah!")
    return None

# MATCH CHECKER
# Mencari benchmark berdasarkan kategori & platform
def checker(category, platform):
    for b in benchmarks:
        if b["Kategori"].lower() == category.lower() and b["Platform"].lower() == platform.lower():
            return b
    return None

# Mencari benchmark berdasarkan ID
def checker_by_id(primary_id):
    for b in benchmarks:
        if b["ID"].lower() == primary_id.lower():
            return b
    return None

# CONFIRMATION
# Konfirmasi jika input tidak valid
def warning_continue():
    while True:
        print("\nInput tidak sesuai!")
        warning = input("Apakah anda ingin melanjutkan program? (Y/N): ").strip().lower()
        if warning == "y":
            return True
        elif warning == "n":
            dashboard()
            return False
        else:
            print("Input hanya Y atau N.")

# Konfirmasi sebelum menyimpan perubahan
def confirm_save():
    while True:
        save = input("Simpan perubahan data? (Y/N): ").strip().lower()
        if save == "y":
            return True
        elif save == "n":
            dashboard()
            return False
        else:
            print("Input hanya Y atau N.")

# TABLE DATA
# Menampilkan tabel benchmark
def table_benchmark(data=None):
    if data is None:
        data = benchmarks

    if not data:
        print("\nData masih belum tersedia.")
        return

    tabel = [[
        b["ID"],
        b["Tanggal"],
        b["Kategori"],
        b["Platform"],
        f"{int(b['CPR Terbaik']):,}",
        b["Notes"]
    ] for b in data]

    print("\n==== List Data Benchmark ====")
    print(tabulate(tabel,
        headers=["ID","Tanggal","Kategori","Platform","CPR Terbaik","Notes"],
        tablefmt="rounded_outline")
    )

# Menampilkan kombinasi kategori & platform unik
def table_category_platform(data=None):
    if data is None:
        data = benchmarks

    seen = set()
    tabel = []

    for b in data:
        key = (b["Kategori"].lower(), b["Platform"].lower())
        if key not in seen:
            seen.add(key)
            tabel.append([b["Kategori"], b["Platform"]])

    if not tabel:
        print("\nData masih belum tersedia.")
        return

    tabel = [[i+1, *row] for i, row in enumerate(tabel)]

    print("\n==== List Kategori & Platform ====")
    print(tabulate(tabel,
        headers=["No","Kategori","Platform"],
        tablefmt="rounded_outline")
    )

# MAIN MENU
# Menampilkan dashboard sesuai role
def dashboard(role):
    print("\n--- Sistem Performance Marketing ---\n")
    print("1. Tampilkan Data Benchmark Campaign")

    if role == "admin":
        print("2. Tambahkan Data Benchmark Campaign")
        print("3. Perbarui Data Benchmark Campaign")
        print("4. Hapus Data Benchmark Campaign")
        print("5. Evaluasi Performa Campaign")
        print("6. Keluar dari Sistem")
    else:
        print("3. Evaluasi Performa Campaign")
        print("4. Keluar dari Sistem")

# CREATE
# Menambahkan benchmark baru
def add_benchmark():
    while True:
        print("\n--- Menu Tambahkan Data ---")
        print("1. Tambah Data")
        print("2. Kembali")
        choice = input("\nPilih: ").strip()

        if choice == "1":
            table_benchmark()
            print("\nSilakan isi data berikut! (ketik 'K' untuk batal)")

            # Validasi tanggal
            while True:
                date = input("\nTanggal mulai campaign (YYYY-MM-DD): ").strip()
                if date.lower() == "k":
                    break
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    break
                except:
                    if not warning_continue():
                        continue

            if date.lower() == "k":
                continue

            # Input kategori
            while True:
                cat = input("Kategori campaign: ").strip()
                if cat.lower() == "k":
                    break
                if cat.isdigit():
                    print("Input tidak boleh angka")
                    continue
                break

            if cat.lower() == "k":
                continue

            # Validasi platform
            allowed_platform = ["facebook","instagram","tiktok","google","shopee ads","tokopedia ads","youtube"]
            while True:
                plat = input("Platform iklan: ").strip()

                if plat.lower() == "k":
                    break

                if plat.lower() not in allowed_platform:
                    print("\nPlatform tidak tersedia.")
                    if not warning_continue():
                        continue
                    else:
                        continue 

                break 

            if plat.lower() == "k":
                continue

            # Validasi CPR
            while True:
                cpr_input = input("Cost per result (Rp): ").strip()

                if cpr_input.lower() == "k":
                    break

                try:
                    cpr = float(cpr_input)

                    if cpr == 0:
                        print("\nInput tidak bisa 0")
                        continue

                    if cpr < 1000:
                        print("\nInput tidak bisa kurang dari Rp 1000")
                        continue

                    break

                except ValueError:
                    print("\nMasukkan angka yang valid atau 'k' untuk keluar.")
                    if not warning_continue():
                        continue

            if cpr_input.lower() == "k":
                continue

            # Input notes
            while True:
                notes = input("Catatan: ").strip()
                if notes.lower() == "k":
                    break
                if notes.isdigit():
                    print("Input tidak boleh angka")
                    continue
                break

            if notes.lower() == "k":
                continue

            # Cek duplikasi
            if checker(cat, plat):
                print("\nBenchmark sudah tersedia untuk kategori & platform ini.")
                continue

            # Simpan data
            if confirm_save():
                benchmarks.append({
                    "Tanggal": date,
                    "Kategori": cat,
                    "Platform": plat,
                    "CPR Terbaik": cpr,
                    "Notes": notes,
                    "ID": generate_id(plat, date)
                })
                print(f"\nBenchmark {cat} berhasil ditambahkan.")

        elif choice == "2":
            break
        else:
            warning_continue()

# READ
# Menampilkan dan memfilter data
def read_table():
    while True:
        print("\n--- Menu Table ---")
        print("1. Tampilkan Semua")
        print("2. Filter Data")
        print("3. Kembali")
        main_choice = input("\nPilih: ")

        if main_choice == "1":
            table_benchmark()
            print("\nNote: Informasi yang ditampilkan merupakan data benchmark.")

        elif main_choice == "2":
            while True:
                print("\n--- Filter Berdasarkan ---")
                print("1. Tanggal")
                print("2. Kategori")
                print("3. Platform")
                print("4. Kembali")
                filter_choice = input("\nPilih: ")

                # Menampilkan data berdasarkan range tanggal
                if filter_choice == "1":
                    print("\n(ketik 'K' untuk batal)\n")
                    while True:
                        df = pd.DataFrame(benchmarks)
                        df["Tanggal"] = pd.to_datetime(df["Tanggal"])

                        start_input = input("Masukkan Tanggal Awal (YYYY-MM-DD): ").strip()
                        if start_input.lower() == "k":
                            break

                        end_input = input("Masukkan Tanggal Akhir (YYYY-MM-DD): ").strip()
                        if end_input.lower() == "k":
                            break

                        try:
                            awalan = datetime.strptime(start_input, "%Y-%m-%d")
                            akhiran = datetime.strptime(end_input, "%Y-%m-%d")

                            filtered = df[df["Tanggal"].between(awalan, akhiran)]

                            if not filtered.empty:
                                table_benchmark(filtered.to_dict("records"))
                            else:
                                print("\nData tidak ditemukan.")
                            break

                        except ValueError:
                            print("\nFormat tanggal salah. Gunakan YYYY-MM-DD.")
                            continue

                # Menampilkan data berdasarkan kategori
                elif filter_choice == "2":
                    while True:
                        print("\n(ketik 'K' untuk batal)\n")
                        cat = input("Kategori: ").strip().lower()

                        if cat == "k":
                            break

                        if cat.isdigit():
                            print("Input tidak boleh angka")
                            continue

                        results = [b for b in benchmarks if b["Kategori"].lower() == cat]

                        if results:
                            table_benchmark(results)
                        else:
                            print("\nData tidak ditemukan.")

                        break

                # Menampilkan data berdasarkan platform
                elif filter_choice == "3":
                    while True:
                        print("\n(ketik 'K' untuk batal)\n")
                        plat = input("Platform: ").strip().lower()

                        if plat == "k":
                            break

                        if plat.isdigit():
                            print("Input tidak boleh angka")
                            continue

                        results = [b for b in benchmarks if b["Platform"].lower() == plat]

                        if results:
                            table_benchmark(results)
                        else:
                            print("\nPlatform tidak tersedia.")

                        break

                elif filter_choice == "4":
                    break
                else:
                    warning_continue()

        elif main_choice == "3":
            break
        else:
            warning_continue()

# UPDATE
# Memperbarui data benchmark
def update_benchmark():
    while True:
        print("\n--- Menu Update Data ---")
        print("1. Update Data")
        print("2. Kembali")
        choice = input("\nPilih: ").strip()

        if choice == "1":
            table_benchmark()
            print("\n(ketik 'K' untuk batal)")

            kid = input("\nID campaign yang ingin diperbarui: ").strip()
            if kid.lower() == "k":
                continue

            b = checker_by_id(kid)
            if not b:
                print("\nData benchmark tidak ditemukan!")
                continue

            print("\nKosongkan data jika tidak ingin di update!\n")

            # Update platform
            while True:
                plat_input = input(f"Platform ({b['Platform']}): ").strip()

                if plat_input.lower() == "k":
                    break

                if not plat_input:
                    plat = b["Platform"]
                    break

                if plat_input.isdigit():
                    print("Input tidak boleh angka")
                    continue

                allowed_platform = ["facebook","instagram","tiktok","google","shopee ads","tokopedia ads","youtube"]
                if plat_input.lower() not in allowed_platform:
                    print("\nPlatform tidak tersedia.")
                    continue

                plat = plat_input
                break

            if plat_input.lower() == "k":
                continue

            # Update CPR
            while True:
                cpr_input = input(f"CPR terbaik ({b['CPR Terbaik']}): ").strip()

                if cpr_input.lower() == "k":
                    break

                if not cpr_input:
                    cpr = b["CPR Terbaik"]
                    break

                try:
                    cpr = float(cpr_input)
                    break
                except:
                    if not warning_continue():
                        continue

            if cpr_input.lower() == "k":
                continue

            # Update notes
            while True:
                notes_input = input(f"Notes ({b['Notes']}): ").strip()

                if notes_input.lower() == "k":
                    break

                if not notes_input:
                    notes = b["Notes"]
                    break

                if notes_input.isdigit():
                    print("Input tidak boleh angka")
                    continue

                notes = notes_input
                break

            if notes_input.lower() == "k":
                continue

            # Cek apakah ada perubahan
            if (plat == b["Platform"] and cpr == b["CPR Terbaik"] and notes == b["Notes"]):
                print("\nTidak ada perubahan data.")
                continue

            # Simpan perubahan
            if confirm_save():
                b.update({"Platform": plat, "CPR Terbaik": cpr, "Notes": notes})
                print(f"\nData benchmark {b['ID']} berhasil diperbarui.")

        elif choice == "2":
            break
        else:
            warning_continue()

# DELETE
# Menghapus data benchmark
def delete_benchmark():
    while True:
        print("\n--- Menu Hapus Data ---")
        print("1. Hapus Data")
        print("2. Kembali")
        choice = input("\nPilih: ").strip()

        if choice == "1":
            table_benchmark()
            kid = input("\nID campaign yang ingin dihapus: ").strip()

            if kid.lower() == "k":
                break

            b = checker_by_id(kid)
            if not b:
                print("\nData benchmark tidak ditemukan!")
                continue

            if confirm_save():
                benchmarks.remove(b)
                print(f"\nData benchmark {b['ID']} berhasil dihapus.")

        elif choice == "2":
            break
        else:
            warning_continue()

# PERFORMANCE
# Membandingkan CPR aktual dengan benchmark
def performance_check():
    while True:
        print("\n--- Menu Performance ---")
        print("1. Check Performance Campaign")
        print("2. Kembali")
        choice = input("\nPilih: ").strip()

        if choice == "1":
            table_category_platform()
            print("\n(ketik 'K' untuk batal)")

            while True:
                cat = input("\nKategori: ").strip()
                if cat.lower() == "k":
                    return
                if cat.isdigit():
                    print("Input tidak boleh angka")
                    continue
                break
            
            allowed_platform = ["facebook","instagram","tiktok","google","shopee ads","tokopedia ads","youtube"]
            while True:
                plat = input("Platform: ").strip()

                if plat.lower() == "k":
                    return

                if plat.isdigit():
                    print("Input tidak boleh angka")
                    continue

                if plat.lower() not in allowed_platform:
                    print("\nPlatform tidak tersedia.")
                    if not warning_continue():
                        continue
                    continue

                break

            b = checker(cat, plat)
            if not b:
                print("\nBenchmark tidak ditemukan.")
                continue

            # Input CPR aktual
            while True:
                actual_input = input("CPR Aktual: ").strip()

                if actual_input.lower() == "k":
                    return

                try:
                    actual = int(actual_input)

                    if actual == 0:
                        print("\nInput tidak bisa 0")
                        continue

                    if actual < 1000:
                        print("\nInput tidak bisa kurang dari Rp 1000")
                        continue

                    break

                except ValueError:
                    warning_continue()
                    continue

            benchmark = b["CPR Terbaik"]

            print(f"\nBenchmark : Rp {benchmark}")
            print(f"Actual    : Rp {actual}")

            if actual > benchmark:
                print(f"\nPerforma belum sesuai benchmark, lebih mahal Rp {actual - benchmark}. Perlu evaluasi!")
            elif actual == benchmark:
                print("\nPerforma sudah sesuai benchmark, pertahankan!")
            else:
                print(f"\nPerforma lebih baik, lebih murah Rp {benchmark - actual}!")

        elif choice == "2":
            break
        else:
            warning_continue()

# MAIN LOOP
# Entry point program
while True:
    role = login()
    if not role:
        continue

    while program_running:
        dashboard(role)
        menu = input("\nPilih Nomor Menu: ").strip()

        if role == "admin":
            if menu == "1":
                read_table()
            elif menu == "2":
                add_benchmark()
            elif menu == "3":
                update_benchmark()
            elif menu == "4":
                delete_benchmark()
            elif menu == "5":
                performance_check()
            elif menu == "6":
                print("\nLogout berhasil.")
                break
            else:
                print("\nInput tidak valid!\n")

        else:
            if menu == "1":
                read_table()
            elif menu == "2":
                add_benchmark()
            elif menu == "3":
                print("\nLogout berhasil.")
                break
            else:
                print("\nInput tidak valid!\n")