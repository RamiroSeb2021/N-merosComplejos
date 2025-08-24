# 📌 Descripción del proyecto

Este proyecto implementa una **clase en Python para representar y operar con números complejos** de manera manual, sin utilizar librerías externas como `complex`.  

La clase `NumeroComplejo` permite realizar operaciones aritméticas básicas, obtener propiedades (módulo, argumento, conjugado), y convertir números complejos entre diferentes representaciones:

- Forma **binómica**  
- Forma **polar**  
- Forma **exponencial (Euler)**  

Además, se incluyen pruebas unitarias con el módulo estándar `unittest` para verificar el correcto funcionamiento de cada método.

---

# ⚙️ Contenido principal

## Clase `NumeroComplejo`

- `__init__(real, complejo)` → Constructor  
- `__str__()` → Representación en forma binómica (ej: 3 + 4i)  
- `__add__`, `__sub__`, `__mul__`, `__truediv__` → Operaciones aritméticas  
- `modulo` → Devuelve el módulo (norma)  
- `argumento` → Devuelve el argumento en radianes  
- `conjugado()` → Retorna el número complejo conjugado  
- `ComplejoaPolar()` → Conversión a forma polar (módulo, fase)  
- `mostrar_polar(grados=False)` → Representación polar (radianes o grados)  
- `desde_polar(modulo, angulo)` → Crea un complejo desde coordenadas polares  
- `a_exponencial(grados=False)` → Representación en forma exponencial  

---

# ✅ Pruebas con `unittest`

El archivo `test.py` contiene un conjunto completo de pruebas para garantizar la correctitud de la implementación.  

Ejemplo de ejecución desde la terminal:

```bash
python -m unittest test.py -v
```

Esto verificará:

- Operaciones aritméticas (suma, resta, multiplicación, división)  
- Propiedades (`modulo`, `argumento`, `conjugado`)  
- Conversiones entre formas (polar y exponencial)  
- Representación en cadenas (`__str__`, `mostrar_polar`)  

---

# 🚀 Ejemplo de uso

```python
from NumeroComplejo import NumeroComplejo
import math

z1 = NumeroComplejo(3, 4)
z2 = NumeroComplejo(1, -2)

print("z1 =", z1)                      # 3 + 4i
print("z2 =", z2)                      # 1 - 2i
print("z1 + z2 =", z1 + z2)            # 4 + 2i
print("z1 * z2 =", z1 * z2)            # 11 - 2i
print("Conjugado de z1:", z1.conjugado())  
print("Módulo de z1:", z1.modulo)     
print("Argumento de z1:", z1.argumento)
print("Forma polar:", z1.mostrar_polar(grados=True))
print("Exponencial:", z1.a_exponencial())
```

---

# 🧑‍💻 Autor

- **Ramiro Sebastián Ramírez**  
  Estudiante de Ingeniería Estadística - Escuela Colombiana de Ingeniería Julio Garavito  
```
