import math

def pias_trapesium(f, a, b, h):
    n = int((b - a) / h)
    result = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        result += 2 * f(x_i)

    return (h / 2) * result

def pias_titik_tengah(f, a, b, h):
    n = int((b - a) / h)
    result = 0

    for i in range(1, n + 1):
        x_i = a + (i - 0.5) * h
        result += f(x_i)

    return h * result

def simpson_1_3(f, a, b, h):
    n = int((b - a) / h)

    # Make sure n is even
    if n % 2 != 0:
        n += 1

    result = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            result += 2 * f(x_i)
        else:
            result += 4 * f(x_i)

    return (h / 3) * result

try:
    a = float(input("Masukkan batas bawah integral (a): "))
    b = float(input("Masukkan batas atas integral (b): "))
    h = float(input("Masukkan nilai h (lebar subinterval): "))

    if h <= 0:
        raise ValueError("Nilai h harus lebih besar dari 0")

    fungsi_input = input("Masukkan fungsi integrand f(x): ")
    fungsi_input = fungsi_input.replace('e', str(math.e))
    fungsi_integrasi = lambda x: eval(fungsi_input)

    hasil_trapesium = pias_trapesium(fungsi_integrasi, a, b, h)
    hasil_titik_tengah = pias_titik_tengah(fungsi_integrasi, a, b, h)
    hasil_simpson_1_3 = simpson_1_3(fungsi_integrasi, a, b, h)

    print(f"\nHasil integral menggunakan metode Pias (trapesium): {hasil_trapesium}")
    print(f"Hasil integral menggunakan metode Pias (titik tengah): {hasil_titik_tengah}")
    print(f"Hasil integral menggunakan metode Newton-Cotes (Simpson 1/3): {hasil_simpson_1_3}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
