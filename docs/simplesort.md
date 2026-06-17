# Sorteo Equiprobable (`Simplesort.py`)

## Funcionamiento
Aunque el archivo se llama "Simplesort", en realidad implementa un **Sorteo Equiprobable** (clase `EquiprobableRaffle`). Este algoritmo no ordena elementos, sino que selecciona un ganador de forma aleatoria a partir de una lista de participantes, garantizando que todos tengan las mismas posibilidades de ser elegidos. Utiliza la función `random.choice()` de Python para realizar la selección.

## Explicación Matemática
Dado un conjunto de participantes $P$ de tamaño $n$ ($|P| = n$), definimos a la variable aleatoria $X$ como el participante ganador. Dado que es un sorteo equiprobable, la distribución de probabilidad es uniforme y discreta. 
La probabilidad de que cualquier participante específico $e_i$ resulte ganador se define como:
$$ P(X = e_i) = \frac{1}{n} $$
Para todos los $i \in \{1, 2, \dots, n\}$.

## Tiempo de Resolución (Complejidad)
- **Tiempo de Selección (Todos los casos):** $\mathcal{O}(1)$ — Seleccionar un elemento aleatorio de una lista (array en memoria contigua) toma tiempo constante.
- **Tiempo de Inicialización:** $\mathcal{O}(n)$ o $\mathcal{O}(1)$ dependiendo de cómo se asigne la lista, típicamente $\mathcal{O}(1)$ para almacenar la referencia y calcular su longitud.
- **Complejidad Espacial:** $\mathcal{O}(n)$ — Para almacenar la lista de $n$ participantes en el objeto.
