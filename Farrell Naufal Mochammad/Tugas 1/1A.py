import numpy as np

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

f1 = lambda x: x**3 - 2*x + 1

r1 = my_bisection(f1, -2, 2, 0.001)
print("Akar f(x) = x^3 - 2x + 1: r1 =", r1)
print("f(r1) =", f1(r1))
