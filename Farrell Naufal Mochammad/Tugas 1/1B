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

f2 = lambda x: np.exp(x) - x

r2 = my_bisection(f2, -2, 2, 0.001)
print("Akar f(x) = e^x - x: r2 =", r2)
print("f(r2) =", f2(r2))
