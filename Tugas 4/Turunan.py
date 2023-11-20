def interpolasi_newton(nilai_x, nilai_y, x):
    n = len(nilai_x)

    F = [[0] * n for _ in range(n)]

    for i in range(n):
        F[i][0] = nilai_y[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (nilai_x[i + j] - nilai_x[i])

    result = F[0][0]

    for j in range(1, n):
        term = F[0][j]
        for i in range(j):
            term *= (x - nilai_x[i])
        result += term
    return result

def hitung_turunan(f_interpolasi, x_evaluasi, h, turunan_ke, metode):
    if turunan_ke == 1:
        if metode == 1:
            return (f_interpolasi(x_evaluasi + h) - f_interpolasi(x_evaluasi)) / h
        elif metode == 2:
            return (f_interpolasi(x_evaluasi) - f_interpolasi(x_evaluasi - h)) / h
        elif metode == 3:
            return (f_interpolasi(x_evaluasi + h) - f_interpolasi(x_evaluasi - h)) / (2 * h)
        else:
            print("Pilihan metode tidak valid.")
            return None
    elif turunan_ke == 2:
        if metode == 1:
            return (f_interpolasi(x_evaluasi + 2 * h) - 2 * f_interpolasi(x_evaluasi + h) + f_interpolasi(x_evaluasi)) / h**2
        elif metode == 2:
            return (f_interpolasi(x_evaluasi) - 2 * f_interpolasi(x_evaluasi - h) + f_interpolasi(x_evaluasi - 2 * h)) / h**2
        elif metode == 3:
            return (f_interpolasi(x_evaluasi + h) - 2 * f_interpolasi(x_evaluasi) + f_interpolasi(x_evaluasi - h)) / h**2
        else:
            print("Pilihan metode tidak valid.")
            return None
    else:
        print("Turunan yang diminta tidak didukung.")
        return None

def main():
    n = int(input("Masukkan jumlah titik data: "))
    x_values = []
    y_values = []
    
    for i in range(n):
        x_values.append(float(input(f"Masukkan nilai x-{i + 1}: ")))
        y_values.append(float(input(f"Masukkan nilai f(x)-{i + 1}: ")))

    x_evaluasi = float(input("Masukkan titik evaluasi (x): "))

    print("Pilih metode:")
    print("1. Selisih Maju")
    print("2. Selisih Mundur")
    print("3. Selisih Pusat")
    metode = int(input("Masukkan nomor metode (1/2/3): "))

    h = float(input("Masukkan nilai h: "))

    f_interpolasi = lambda x: interpolasi_newton(x_values, y_values, x)

    turunan_ke = int(input("Masukkan turunan ke berapa yang ingin dihitung (1 atau 2): "))

    turunan = hitung_turunan(f_interpolasi, x_evaluasi, h, turunan_ke, metode)

    if turunan is not None:
        if metode == 1:
            print(f"Nilai turunan ke-{turunan_ke} menggunakan metode Selisih Maju: {turunan}")
        elif metode == 2:
            print(f"Nilai turunan ke-{turunan_ke} menggunakan metode Selisih Mundur: {turunan}")
        elif metode == 3:
            print(f"Nilai turunan ke-{turunan_ke} menggunakan metode Selisih Pusat: {turunan}")
        else:
            print("Pilihan metode tidak valid.")


if __name__ == "__main__":
    main()