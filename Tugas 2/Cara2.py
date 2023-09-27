def newton_raphson(f, g, x0, e, max_iterations):
    step = 1
    while step <= max_iterations:
        if g(x0) == 0.0:
            raise ValueError("Turunan f'(x) menjadi nol. Metode Newton-Raphson tidak dapat dilanjutkan.")
        
        x1 = x0 - f(x0)/g(x0)
        f_x1 = f(x1)
        print(f'Iterasi-{step}, x1 = {x1:.6f}, f(x1) = {f_x1:.6f}')
        
        if abs(f_x1) < e:
            print(f'\nKonvergensi tercapai. Akar yang dibutuhkan: {x1:.8f}')
            return

        x0 = x1
        step += 1

    print(f"\nMetode Newton-Raphson tidak konvergen dalam {max_iterations} iterasi.")

def main():
    try:
        x0 = float(input('Perkiraan: '))
        e = float(input('Perkiraan Error: '))
        N = int(input('Jumlah Step: '))

        newton_raphson(lambda x: x**2 - 2*x - 8, lambda x: 2*x - 2, x0, e, N)

    except ValueError:
        print('Input yang dimasukkan tidak valid. Harap masukkan nilai numerik yang valid.')
    except KeyboardInterrupt:
        print('Proses dihentikan oleh pengguna.')

if __name__ == "__main__":
    main()
