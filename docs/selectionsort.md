# Ordenamiento por Selección (`SelectionSort.py`)

## Funcionamiento
El algoritmo de ordenamiento por selección (Selection Sort) divide la lista en dos partes: la parte ordenada al principio y la parte desordenada al final. Iterativamente, busca el elemento más pequeño dentro de la porción desordenada y lo intercambia con el primer elemento desordenado, expandiendo así la sección ordenada en un elemento a la vez.

## Explicación Matemática
Sin importar el orden inicial de los elementos, el algoritmo siempre realiza el mismo número de comparaciones para encontrar el mínimo. En el primer paso hace $n-1$ comparaciones, en el segundo $n-2$, y así sucesivamente:
$$ \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2} \approx \frac{1}{2}n^2 $$
Esto significa que el número de operaciones de comparación es constante independientemente de si el arreglo está ordenado o no.

## Tiempo de Resolución (Complejidad)
- **Peor Caso:** $\mathcal{O}(n^2)$
- **Caso Promedio:** $\mathcal{O}(n^2)$
- **Mejor Caso:** $\mathcal{O}(n^2)$ — Siempre revisa todos los elementos restantes para estar seguro de que tiene el mínimo.
- **Complejidad Espacial:** $\mathcal{O}(1)$ — Se realiza de forma in-place.
