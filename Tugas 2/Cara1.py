def newton_raphson(f, df, xi, e, max_iterations=100):
    print("Nilai xi: ", xi)
    
    for i in range(max_iterations):
        f_xi = f(xi)
        df_xi = df(xi)
        
        if abs(f_xi) < e:
            return xi, i + 1  # Mengembalikan hasil dan jumlah iterasi
        
        if df_xi == 0:
            print("Turunan f'(xi) menjadi nol. Metode Newton-Raphson gagal.")
            return None, i + 1
        
        xi = xi - f_xi / df_xi
        print(f"Iterasi {i + 1}: xi = {xi:.6f}, f(xi) = {f_xi:.6f}")

    print("Metode Newton-Raphson tidak konvergen dalam {} iterasi.".format(max_iterations))
    return None, max_iterations

# Definisikan f(x), f'(x), dan nilai awal
fx = lambda x: x**2 + 3*x - 108
f_prime = lambda x: 2*x + 3

try:
    n = float(input("Masukkan Nilai Aproksimasi Awal: "))

    # Pemanggilan fungsi Newton Raphson
    estimate, iterations = newton_raphson(fx, f_prime, n, 1e-3)
    
    if estimate is not None:
        print(f"Estimasi Akar = {estimate:.3f}")
        print(f"Jumlah Iterasi = {iterations}")
except ValueError:
    print("Input yang dimasukkan tidak valid. Harap masukkan angka float.")
