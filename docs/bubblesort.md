# Algoritmo de Burbuja (`Bubblesort.py`)

## Funcionamiento
El ordenamiento de burbuja (Bubble Sort) es un algoritmo sencillo que revisa repetidamente una lista, compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que no se necesiten más intercambios, lo que indica que la lista está ordenada.
En esta implementación específica, se utiliza una bandera (`swapped`) como optimización para detener el algoritmo prematuramente si en una pasada completa no hubo ningún intercambio, lo que significa que la lista ya está completamente ordenada.

## Explicación Matemática
El algoritmo se basa en el número de inversiones (pares de elementos que están desordenados) presentes en la lista. En cada pasada $i$, el elemento más grande de la sublista no ordenada "burbujea" hasta su posición final.
La cantidad de comparaciones en el peor de los casos está dada por la suma de los primeros $n-1$ enteros:
$$ C = (n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2} $$

## Tiempo de Resolución (Complejidad)
- **Peor Caso:** $\mathcal{O}(n^2)$ — Ocurre cuando la lista está ordenada en orden inverso.
- **Caso Promedio:** $\mathcal{O}(n^2)$
- **Mejor Caso:** $\mathcal{O}(n)$ — Gracias a la variable `swapped`, si la lista ya está ordenada, el algoritmo solo hace una pasada.
- **Complejidad Espacial:** $\mathcal{O}(1)$ — Ya que el ordenamiento se hace sobre la misma lista modificando los elementos (in-place).
