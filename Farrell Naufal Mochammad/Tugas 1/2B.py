import numpy as np
import matplotlib.pyplot as plt

def my_bisection(f, a, b, e, max_iterations=100):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    
    for _ in range(max_iterations):
        m = (a + b) / 2
        if np.abs(f(m)) < e:
            return m
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m
    
    raise Exception(f'Tidak konvergen setelah {max_iterations} iterasi')

# Input fungsi, batas akar, dan galat dari user
expression = input("Masukkan ekspresi fungsi f(x): ")
f = lambda x: eval(expression)
a = float(input("Masukkan batas bawah a: "))
b = float(input("Masukkan batas atas b: "))
e = float(input("Masukkan galat e: "))

# Panggil fungsi Bagi Dua dengan input pengguna
try:
    root = my_bisection(f, a, b, e)
    print("Akar:", root)
    print("f(akar):", f(root))

    # Plot fungsi
    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.plot(x, y, label='f(x)')
    
    # Tandai akar pada grafik
    plt.scatter(root, f(root), color='red', marker='o', label='Akar')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Grafik f(x)')
    plt.grid(True)
    plt.show()
    
except Exception as ex:
    print(ex)
