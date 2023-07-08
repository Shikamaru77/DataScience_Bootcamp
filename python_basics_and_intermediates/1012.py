a,b,c = map(float,input().split())


TRIANGULO = 0.5 * float(a) * float(c)
CIRCULO = 3.14159 * (float(c))**2
TRAPEZIO = 0.5 * ( float(a) + float(b) ) * float(c)
QUADRADO = (float(b))**2
RETANGULO = float(a) * float(b)

print("TRIANGULO: %0.3f" %TRIANGULO)
print("CIRCULO: %0.3f" %CIRCULO)
print("TRAPEZIO: %0.3f" %TRAPEZIO)
print("QUADRADO: %0.3f" %QUADRADO)
print("RETANGULO: %0.3f" %RETANGULO)