Revisé tus archivos y ejecuté las pruebas: **7 aprobadas**. También reproduje el análisis de hongos corrigiendo el tratamiento de los valores `?`: la SVM obtuvo **F1 macro = 1.0000** en la partición utilizada.

El notebook original contiene una frase en español dentro de una celda de Python que impide ejecutarlo completo. La versión siguiente corrige ese problema. Los archivos originales permanecen sin modificar.

Te entrego los seis apartados en bloques Markdown independientes.

**1. README**

````md
# Clasificación de hongos mediante SVM

**Autor:** Roberto Byas de la Cruz  
**Asignatura:** INF-8239 — Ciencia de Datos II  
**Conjunto de datos:** Mushroom Classification

## Objetivo

Construir y evaluar un modelo de clasificación que distinga las categorías de comestibilidad del conjunto Mushroom mediante sus características físicas y ecológicas.

El proyecto incluye auditoría de datos, reconocimiento de valores ausentes, separación de entrenamiento y prueba, preprocesamiento mediante pipeline y comparación de una SVM con una línea base.

## Datos y target

El archivo analizado contiene:

- 8,124 registros.
- 23 columnas: 22 predictores y un target.
- 4,208 registros de clase `e`.
- 3,916 registros de clase `p`.

La variable objetivo es `class`:

- `e`: comestible.
- `p`: venenoso; la documentación original agrupa también en esta clase los casos de comestibilidad desconocida y no recomendada.

Los registros describen muestras hipotéticas. El proyecto tiene fines académicos y no debe utilizarse para decidir el consumo de hongos reales.

## Organización

- `data/raw/dataset.csv`: datos de entrada.
- `docs/`: procedencia, diccionario y conclusión.
- `notebooks/02_svm_automatizado.ipynb`: análisis de hongos.
- `src/inf8239_u01/data.py`: procedimiento de descarga.
- `src/inf8239_u01/models.py`: constructor de SVM para variables numéricas del ejercicio guiado.
- `tests/`: pruebas del entorno, datos y modelo.
- `reports/mushroom/`: resultados generados por el notebook de hongos.

El notebook `01_svm_guiada.ipynb` corresponde al ejercicio de tumores. Sus resultados no deben atribuirse al conjunto Mushroom.

## Instalación en Windows

Ejecutar desde la raíz del proyecto en PowerShell:

```powershell
python -m venv .venv

.\.venv\Scripts\python.exe -m pip install --upgrade pip

.\.venv\Scripts\python.exe -m pip install pandas==2.2.3 scikit-learn==1.8.0 pytest==9.1.1 notebook ipykernel matplotlib joblib kagglehub
```

Estos comandos utilizan directamente el intérprete del entorno virtual y no requieren ejecutar `Activate.ps1`.

La comprobación realizada utilizó Python 3.12.14, pandas 2.2.3, scikit-learn 1.8.0 y pytest 9.1.1. La ejecución en el equipo del autor debe verificarse con su entorno instalado.

## Obtención de los datos

Página utilizada:

https://www.kaggle.com/datasets/uciml/mushroom-classification

Documentación original:

https://archive.ics.uci.edu/dataset/73/mushroom

El archivo ya incluido en el proyecto debe ubicarse en:

`data/raw/dataset.csv`

Si se necesita descargarlo nuevamente, ejecutar desde la raíz:

```powershell
$env:PYTHONPATH = "src"

.\.venv\Scripts\python.exe -c "from inf8239_u01.data import download_csv; print(download_csv('https://www.kaggle.com/datasets/uciml/mushroom-classification'))"
```

La función recibida utiliza `kagglehub` para descargar el dataset, localiza un CSV en el directorio obtenido y lo guarda en la carpeta del proyecto.

Si Kaggle solicita autenticación, debe configurarse mediante sus mecanismos oficiales. Las credenciales no deben escribirse en el notebook ni incorporarse al repositorio.

La caché interna de Kaggle puede estar fuera del proyecto; la copia de trabajo se guarda en `data/raw/dataset.csv`.

La descarga no se volvió a ejecutar durante esta revisión: se utilizó el CSV recibido.

## Identificación de la copia analizada

SHA-256 de `dataset.csv`:

`0df7573924b7a06785dbd7f1ed95db39e690ee13fd409da82b505afd77fdd7f2`

Una descarga futura puede cambiar su representación o contenido. Conservar esta huella permite identificar la copia utilizada.

## Tratamiento de datos

La lectura utiliza:

```python
pd.read_csv(DATA_PATH, na_values=["?"])
```

Se identificaron 2,480 valores ausentes en `stalk-root`, equivalentes al 30.53 % de sus registros.

Los predictores son categóricos. Se aplica:

1. Imputación mediante la categoría más frecuente.
2. Codificación One-Hot.
3. Clasificación mediante SVM con kernel RBF.

La imputación y la codificación se ajustan exclusivamente con entrenamiento.

## Métricas

Se conserva el **F1 macro** como métrica principal del notebook recibido. Esta métrica asigna el mismo peso a ambas clases.

Como métricas complementarias se presentan:

- Recall de la clase `p`.
- Precision de la clase `p`.
- Accuracy.
- Matriz de confusión.

El error de mayor interés es clasificar como comestible un registro cuya etiqueta real es `p`.

## Diseño de evaluación

- Entrenamiento: 6,499 registros.
- Prueba: 1,625 registros.
- División estratificada.
- Semilla: 42.
- Línea base: `DummyClassifier(strategy="most_frequent")`.
- SVM: kernel RBF, `C=1`, `gamma="scale"`.

Esta versión utiliza parámetros fijos. No realiza búsqueda de hiperparámetros ni validación cruzada.

## Ejecución del notebook

Desde la raíz del proyecto:

```powershell
.\.venv\Scripts\python.exe -m notebook
```

Abrir `notebooks/02_svm_automatizado.ipynb`, seleccionar el entorno del proyecto y ejecutar todas las celdas desde un kernel reiniciado.

La versión corregida localiza los datos desde la raíz o desde `notebooks/`.

## Pruebas

Desde la raíz:

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m pytest -q
```

Resultado de la revisión:

`7 passed in 3.05s`

## Resultados reproducidos

| Modelo | F1 macro | Recall de p | Accuracy |
|---|---:|---:|---:|
| Línea base | 0.3413 | 0.0000 | 0.5182 |
| SVM RBF | 1.0000 | 1.0000 | 1.0000 |

Estos valores corresponden a una partición concreta de este dataset. No demuestran capacidad de generalización a hongos reales o especies nuevas.
````

**2. Ficha de procedencia y licencia**

Verifiqué la licencia **CC BY 4.0** en UCI y la identificación del donante en la documentación original. ([archive.ics.uci.edu][1])

```md
# Ficha de procedencia y licencia

## Identificación

| Campo | Información |
|---|---|
| Nombre | Mushroom |
| Copia utilizada | Mushroom Classification, publicada en Kaggle por `uciml` |
| Repositorio original | UCI Machine Learning Repository |
| Fuente documental original | The Audubon Society Field Guide to North American Mushrooms, 1981 |
| Donante identificado | Jeff Schlimmer |
| Incorporación según la página UCI | 26 de abril de 1987 |
| Fecha indicada en el archivo histórico `.names` | 27 de abril de 1987 |
| Fecha de verificación de fuentes | 23 de septiembre de 2026 |
| Dominio | Clasificación biológica con fines académicos |
| Unidad de análisis | Descripción de una muestra hipotética de hongo |
| Tipo de tarea | Clasificación supervisada binaria |
| Usuario previsto | Estudiantes, docentes e investigadores |
| Error más costoso | Predecir `e` cuando la etiqueta real es `p` |

Las dos fechas de abril de 1987 se conservan indicando su fuente; no se presentan como si fueran una única fecha inequívoca.

## Enlaces

- Documentación institucional: https://archive.ics.uci.edu/dataset/73/mushroom
- Diccionario original: https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names
- Descarga original en ZIP: https://archive.ics.uci.edu/static/public/73/mushroom.zip
- Copia utilizada en Kaggle: https://www.kaggle.com/datasets/uciml/mushroom-classification
- DOI: https://doi.org/10.24432/C5959T

## Licencia

UCI publica Mushroom bajo Creative Commons Attribution 4.0 International, CC BY 4.0:

https://creativecommons.org/licenses/by/4.0/

La reutilización debe acompañarse de la atribución correspondiente, un enlace a la licencia y la identificación de los cambios realizados.

Esta declaración corresponde a la licencia verificada en UCI. No se atribuye una licencia independiente a la página de Kaggle sin haberla comprobado.

## Características de la copia recibida

| Característica | Resultado |
|---|---:|
| Registros | 8,124 |
| Columnas | 23 |
| Predictores | 22 |
| Registros de clase e | 4,208 |
| Registros de clase p | 3,916 |
| Filas completamente duplicadas | 0 |
| Valores ausentes en stalk-root | 2,480 |
| Porcentaje ausente en stalk-root | 30.53 % |

La clase `p` reúne hongos venenosos y los de comestibilidad desconocida no recomendados, según la documentación original.

## Procedimiento de obtención

El módulo `src/inf8239_u01/data.py` encapsula la descarga desde Kaggle mediante `kagglehub` y escribe una copia CSV en `data/raw/dataset.csv`.

Para reproducir el análisis con los archivos recibidos no es necesario descargar nuevamente los datos.

La descarga original de UCI es un ZIP y sus datos no tienen el mismo encabezado que el CSV de Kaggle. No debe sustituirse un archivo por otro sin adaptar su lectura y comprobar el esquema.

## Transformaciones del análisis

- Reconocimiento de `?` como valor ausente.
- Separación de `class` respecto de los predictores.
- Imputación de predictores con la categoría más frecuente de entrenamiento.
- Codificación One-Hot.
- Conservación de las 22 variables predictoras.

No se eliminan columnas por su efecto sobre las métricas.

## Referencia

Mushroom [Conjunto de datos]. (1981). UCI Machine Learning Repository. https://doi.org/10.24432/C5959T
```

**3. Diccionario de datos**

Los códigos observados se comprobaron en tu CSV. El enlace al diccionario original permite consultar su interpretación completa. ([archive.ics.uci.edu][2])

```md
# Diccionario de datos — Mushroom

## Convenciones comunes

- **Fuente de todas las variables:** conjunto Mushroom; copia CSV recibida y documentación UCI.
- **Representación:** códigos de texto.
- **Tipo analítico:** variables categóricas; `ring-number` representa un conteo codificado.
- **Unidad:** no aplica a las categorías; en `ring-number`, anillos.
- **Target:** `class`.
- **Predictores:** las otras 22 columnas.
- **Disponibilidad prevista:** características registradas antes de asignar la predicción. Es un supuesto del ejercicio, no una disponibilidad validada en campo.
- **Transformación T:** imputación por moda de entrenamiento y codificación One-Hot dentro del pipeline.
- **Transformación Y:** conservar la etiqueta como objetivo y excluirla de `X`.

Los códigos de una columna no deben interpretarse utilizando el significado de otra. Por ejemplo, `p` no significa lo mismo en `class` y en `veil-type`.

## Variables

| Variable | Significado | Códigos observados | Disponibilidad | Transformación | Riesgo o consideración |
|---|---|---|---|---|---|
| class | Clase de comestibilidad | e, p | Etiqueta conocida para entrenar y evaluar | Y | Fuga directa si se incorpora a X |
| cap-shape | Forma del sombrero | b, c, f, k, s, x | Tras observación del sombrero | T | Posible confusión entre formas |
| cap-surface | Superficie del sombrero | f, g, s, y | Tras observación de superficie | T | Clasificación visual subjetiva |
| cap-color | Color del sombrero | b, c, e, g, n, p, r, u, w, y | Tras observación del color | T | Variación por iluminación o estado |
| bruises | Presencia de magulladuras o cambios asociados | f, t | Tras registrar esta característica | T | No debe suponerse disponible sin observación |
| odor | Olor registrado | a, c, f, l, m, n, p, s, y | Tras evaluación del olor | T | Medición subjetiva |
| gill-attachment | Unión de las láminas | a, f | Tras inspección de láminas | T | Requiere reconocimiento morfológico |
| gill-spacing | Separación de las láminas | c, w | Tras inspección de láminas | T | Posible ambigüedad entre categorías |
| gill-size | Anchura de las láminas | b, n | Tras inspección de láminas | T | Categoría relativa, no medida continua |
| gill-color | Color de las láminas | b, e, g, h, k, n, o, p, r, u, w, y | Tras observación de láminas | T | Variación visual |
| stalk-shape | Forma del pie | e, t | Tras inspección del pie | T | Requiere observar su forma |
| stalk-root | Forma de la base del pie | b, c, e, r; ? como ausente | Tras inspección de la base | ? → ausente; luego T | 2,480 ausentes; imputación puede simplificar la variación |
| stalk-surface-above-ring | Superficie del pie sobre el anillo | f, k, s, y | Tras inspección de esa zona | T | Dependencia de observación suficiente |
| stalk-surface-below-ring | Superficie del pie bajo el anillo | f, k, s, y | Tras inspección de esa zona | T | Dependencia de observación suficiente |
| stalk-color-above-ring | Color del pie sobre el anillo | b, c, e, g, n, o, p, w, y | Tras inspección de esa zona | T | Variación visual |
| stalk-color-below-ring | Color del pie bajo el anillo | b, c, e, g, n, o, p, w, y | Tras inspección de esa zona | T | Variación visual |
| veil-type | Tipo de velo | p | Tras identificación del velo | T | Constante en esta copia; se conserva |
| veil-color | Color del velo | n, o, w, y | Tras observación del velo | T | Posible dificultad de observación |
| ring-number | Número de anillos | n, o, t | Tras contar los anillos | T | Conteo codificado, no número leído directamente |
| ring-type | Tipo de anillo | e, f, l, n, p | Tras inspección del anillo | T | Requiere reconocimiento morfológico |
| spore-print-color | Color de la impresión de esporas | b, h, k, n, o, r, u, w, y | Después de disponer de la impresión | T | No disponible en una observación visual inmediata |
| population | Categoría de agrupación o abundancia | a, c, n, s, v, y | Tras registrar el contexto de crecimiento | T | Puede faltar al observar un ejemplar aislado |
| habitat | Hábitat | d, g, l, m, p, u, w | Tras registrar el lugar de procedencia | T | Puede desconocerse fuera del lugar de recolección |

## Interpretaciones esenciales

- `class`: `e` = comestible; `p` = venenoso o no recomendado.
- `bruises`: `t` = sí; `f` = no.
- `gill-size`: `b` = ancha; `n` = estrecha.
- `veil-type`: `p` = parcial.
- `ring-number`: `n` = ninguno; `o` = uno; `t` = dos.
- `stalk-root`: `?` = información ausente.

Para interpretar todos los códigos, utilizar el diccionario original:

https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names

Los códigos observados no incluyen necesariamente todas las categorías admitidas por la documentación original.

## Exclusiones

`DROP_COLUMNS = []`

No se han establecido exclusiones adicionales. La columna `class` se retira de X porque es la variable que se desea predecir.

La alta capacidad predictiva de una característica, como el olor, no demuestra por sí misma fuga de información. Debe revisarse cómo se obtuvo y si estará disponible en el escenario de predicción.

## Variable constante

`veil-type` presenta una única categoría en el archivo analizado.

Se conserva para mantener el esquema recibido. Su presencia no permite distinguir registros dentro de esta copia y no debe confundirse con una fuga de información.
```

**4. Notebook completo corregido**

Este contenido reemplaza el análisis de `02_svm_automatizado.ipynb`. Cada sección de texto corresponde a una celda Markdown y cada bloque Python a una celda de código.

````md
# Clasificación de hongos mediante SVM

**Autor:** Roberto Byas de la Cruz  
**Asignatura:** INF-8239 — Ciencia de Datos II

## Pregunta

¿Qué desempeño presenta una SVM con kernel RBF al clasificar las etiquetas de comestibilidad del conjunto Mushroom, en comparación con una línea base que siempre predice la clase mayoritaria?

## Diseño

- Unidad de análisis: descripción de una muestra hipotética de hongo.
- Target: `class`.
- Clases: `e` y `p`.
- Métrica principal: F1 macro.
- Métrica complementaria prioritaria: recall de `p`.
- División estratificada: 80 % entrenamiento y 20 % prueba.
- Semilla: 42.
- Parámetros de SVM fijados de antemano: `C=1`, `gamma="scale"`.

El ejercicio no permite determinar si un hongo real puede consumirse.

## 1. Importaciones y localización del proyecto

### Comentario de entrada

Se importan las herramientas necesarias y se localiza la carpeta del proyecto a partir del archivo de datos. Se admiten ejecuciones desde la raíz o desde la carpeta `notebooks`.

```python
from pathlib import Path
import platform

import pandas as pd
import sklearn
import joblib
import matplotlib.pyplot as plt

from IPython.display import display
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    precision_score,
    recall_score,
)

candidates = [Path.cwd(), *Path.cwd().parents]
ROOT = next(
    (
        folder for folder in candidates
        if (folder / "data" / "raw" / "dataset.csv").is_file()
    ),
    None,
)

if ROOT is None:
    raise FileNotFoundError(
        "No se encontró data/raw/dataset.csv. "
        "Ejecute desde la raíz del proyecto o desde notebooks/."
    )

DATA_PATH = ROOT / "data" / "raw" / "dataset.csv"
REPORTS = ROOT / "reports" / "mushroom"

print("Datos:", DATA_PATH)
print("Python:", platform.python_version())
print("pandas:", pd.__version__)
print("scikit-learn:", sklearn.__version__)
```

### Comentario de salida

La ruta identificada permite leer la copia local del dataset sin depender de una ubicación personal fija. También se registran las versiones del entorno.

## 2. Cargar y reconocer el esquema

### Comentario de entrada

Se carga el CSV reconociendo `?` como dato ausente. Esto permite que la auditoría y la imputación posterior interpreten correctamente los faltantes.

```python
df = pd.read_csv(DATA_PATH, na_values=["?"])

assert not df.empty
assert df.columns.is_unique

print("Dimensiones:", df.shape)
print(df.dtypes)
display(df.head())
display(df.tail())
```

### Comentario de salida

El archivo recibido contiene 8,124 filas y 23 columnas. Los códigos de las variables se conservan como categorías de texto y los signos `?` se reconocen como ausentes.

## 3. Construir la auditoría

### Comentario de entrada

Se revisan los tipos, los valores ausentes, su porcentaje, la cantidad de valores distintos y las filas duplicadas.

```python
audit = pd.DataFrame({
    "tipo": df.dtypes.astype(str),
    "ausentes": df.isna().sum(),
    "porcentaje_ausente": df.isna().mean().mul(100).round(2),
    "unicos_incluyendo_ausentes": df.nunique(dropna=False),
}).sort_values("porcentaje_ausente", ascending=False)

print("Filas duplicadas:", df.duplicated().sum())
display(audit)

constants = df.columns[
    df.nunique(dropna=False).eq(1)
].tolist()
print("Columnas constantes:", constants)
```

### Comentario de salida

Se identifican 2,480 ausentes en `stalk-root`, equivalentes al 30.53 %. No se encuentran filas completamente duplicadas. `veil-type` es constante y se conserva para mantener el esquema.

## 4. Definir target y retirar fugas

### Comentario de entrada

Se define `class` como target y se excluye de los predictores. No se eliminan otras columnas sin una justificación semántica o de disponibilidad.

```python
TARGET = "class"
DROP_COLUMNS = []

assert TARGET in df.columns

X = df.drop(columns=[TARGET] + DROP_COLUMNS)
y = df[TARGET]

assert y.notna().all()
assert set(y.unique()) == {"e", "p"}
assert TARGET not in X.columns

print("Distribución del target:")
print(y.value_counts(dropna=False))
print("Predictores:", X.shape[1])
```

### Comentario de salida

Se obtienen 22 predictores. La variable objetivo contiene 4,208 registros `e` y 3,916 registros `p`, sin valores ausentes.

## 5. Reservar el conjunto de prueba

### Comentario de entrada

Se separa el 20 % de los registros para prueba mediante estratificación. El preprocesamiento todavía no se ajusta.

```python
Xtr, Xte, ytr, yte = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

assert Xtr.index.is_unique
assert Xte.index.is_unique
assert set(Xtr.index).isdisjoint(Xte.index)
assert len(Xtr) + len(Xte) == len(X)

print("Entrenamiento:", Xtr.shape)
print("Prueba:", Xte.shape)
print("Clases en prueba:")
print(yte.value_counts())
```

### Comentario de salida

Se obtienen 6,499 registros de entrenamiento y 1,625 de prueba. En prueba hay 842 registros `e` y 783 registros `p`.

## 6. Crear el preprocesamiento

### Comentario de entrada

Los predictores de este archivo son categóricos. Se define una imputación por moda y una codificación One-Hot que admite categorías desconocidas.

```python
num_cols = Xtr.select_dtypes(include="number").columns.tolist()
cat_cols = Xtr.select_dtypes(exclude="number").columns.tolist()

print("Numéricas:", len(num_cols))
print("Categóricas:", len(cat_cols))

assert len(num_cols) == 0, (
    "El esquema cambió: revisar las columnas numéricas."
)
assert len(cat_cols) == 22

cat_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore")),
])

preprocess = ColumnTransformer([
    ("cat", cat_pipe, cat_cols),
])
```

### Comentario de salida

El preprocesamiento queda definido para los 22 predictores categóricos. Su ajuste se realizará con entrenamiento al ejecutar cada pipeline.

## 7. Entrenar la línea base y la SVM

### Comentario de entrada

Se construyen dos pipelines independientes. La línea base utiliza la clase mayoritaria y la SVM emplea un kernel RBF con parámetros fijos. No se solicitan probabilidades porque la evaluación utiliza etiquetas.

```python
models = {
    "dummy": Pipeline([
        ("prep", clone(preprocess)),
        ("model", DummyClassifier(strategy="most_frequent")),
    ]),
    "svm": Pipeline([
        ("prep", clone(preprocess)),
        ("model", SVC(
            kernel="rbf",
            C=1.0,
            gamma="scale",
        )),
    ]),
}

for name, model in models.items():
    model.fit(Xtr, ytr)
    print("Entrenado:", name)
```

### Comentario de salida

Ambos modelos quedan ajustados con entrenamiento. El uso de copias independientes del preprocesamiento evita compartir accidentalmente un mismo objeto ajustado entre los pipelines.

## 8. Evaluar los modelos

### Comentario de entrada

Se generan las predicciones de prueba y se calculan las métricas. La etiqueta positiva para precision y recall es `p`.

```python
predictions = {}
rows = []

for name, model in models.items():
    pred = model.predict(Xte)
    predictions[name] = pred

    assert len(pred) == len(yte)
    assert set(pred).issubset({"e", "p"})

    rows.append({
        "modelo": name,
        "f1_macro": f1_score(yte, pred, average="macro"),
        "recall_p": recall_score(
            yte, pred, pos_label="p", zero_division=0
        ),
        "precision_p": precision_score(
            yte, pred, pos_label="p", zero_division=0
        ),
        "accuracy": accuracy_score(yte, pred),
    })

results = pd.DataFrame(rows).set_index("modelo")
display(results.round(4))

print(classification_report(
    yte,
    predictions["svm"],
    labels=["e", "p"],
    digits=4,
    zero_division=0,
))
```

### Comentario de salida

En la ejecución de comprobación, la línea base obtuvo F1 macro de 0.3413 y la SVM obtuvo 1.0000. La precision de `p` en la línea base se informa como cero por convención, ya que no predice ningún registro de esa clase.

## 9. Analizar los errores

### Comentario de entrada

Se presenta la matriz de confusión con el orden `e`, `p` y se cuentan los registros de clase `p` clasificados incorrectamente como `e`.

```python
cm = confusion_matrix(
    yte,
    predictions["svm"],
    labels=["e", "p"],
)

display(pd.DataFrame(
    cm,
    index=["Real e", "Real p"],
    columns=["Predicho e", "Predicho p"],
))

dangerous_errors = (
    (yte.to_numpy() == "p")
    & (predictions["svm"] == "e")
).sum()

print("Registros p clasificados como e:", int(dangerous_errors))

ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["e", "p"],
).plot(cmap="Blues", values_format="d")

plt.title("SVM — matriz de confusión")
plt.tight_layout()
plt.show()
```

### Comentario de salida

La matriz reproducida es:

| Clase real | Predicho e | Predicho p |
|---|---:|---:|
| e | 842 | 0 |
| p | 0 | 783 |

No se observaron errores en esta partición. El resultado no garantiza desempeño perfecto en otros conjuntos ni en condiciones reales.

## 10. Guardar los resultados

### Comentario de entrada

Se guardan la auditoría, las métricas, las predicciones y el pipeline completo en una carpeta exclusiva del análisis de hongos.

```python
REPORTS.mkdir(parents=True, exist_ok=True)

audit.to_csv(REPORTS / "auditoria.csv")
results.to_csv(REPORTS / "metricas.csv")

pd.DataFrame({
    "indice_original": Xte.index,
    "real": yte.to_numpy(),
    "pred_dummy": predictions["dummy"],
    "pred_svm": predictions["svm"],
}).to_csv(REPORTS / "predicciones.csv", index=False)

joblib.dump(
    models["svm"],
    REPORTS / "svm_mushroom.joblib",
)

print("Resultados guardados en:", REPORTS)
```

### Comentario de salida

Los resultados quedan separados de los informes del ejercicio de tumores. El archivo del modelo contiene tanto el preprocesamiento como la SVM.

## 11. Límites de interpretación

- Se utilizó una única división estratificada.
- No se realizó búsqueda de hiperparámetros.
- El conjunto de prueba ya había sido consultado en el notebook recibido.
- Esta ejecución verifica reproducibilidad; no constituye una nueva validación independiente.
- No se evaluó generalización a especies nuevas.
- Los datos representan descripciones hipotéticas.
- La disponibilidad real de todas las características no fue validada en campo.
````

**5. Pruebas aprobadas**

````md
# Informe de pruebas

## Resultado verificado

Se ejecutaron los archivos de pruebas recibidos sin modificar su contenido.

Comando utilizado en el entorno de revisión:

```bash
PYTHONPATH=src python -m pytest -q
```

Salida real:

```text
.......                                                                  [100%]
7 passed in 3.05s
```

## Entorno de comprobación

- Python: 3.12.14.
- pandas: 2.2.3.
- scikit-learn: 1.8.0.
- pytest: 9.1.1.

## Pruebas ejecutadas

| Archivo | Prueba | Resultado |
|---|---|---|
| test_environment.py | test_environment_message | Aprobada |
| test_data_contract.py | test_dataset_is_not_empty | Aprobada |
| test_data_contract.py | test_required_columns_exist | Aprobada |
| test_data_contract.py | test_target_has_no_missing_and_two_classes | Aprobada |
| test_models.py | test_svm_returns_one_prediction_per_row | Aprobada |
| test_models.py | test_svm_rejects_non_positive_c | Aprobada |
| test_models.py | test_pipeline_contains_scaler_and_model | Aprobada |

## Alcance

Las pruebas comprueban:

1. El mensaje esperado del módulo de entorno.
2. Que el dataset no esté vacío.
3. La presencia de las columnas `class` y `odor`.
4. La ausencia de faltantes en el target y la presencia exacta de las clases `e` y `p`.
5. Una predicción por fila en el modelo numérico.
6. El rechazo de `C=0`.
7. La existencia de los pasos de escalado y modelo en `build_svm`.

## Limitaciones de la suite recibida

Las tres pruebas de `test_models.py` utilizan el conjunto de tumores de scikit-learn y el constructor `build_svm`.

Por tanto, su aprobación no equivale a una prueba automatizada del pipeline categórico de Mushroom.

La suite tampoco comprueba la descarga desde Kaggle ni la ejecución completa del notebook.

## Verificación adicional del análisis Mushroom

Se ejecutó el flujo corregido de carga, reconocimiento de ausentes, partición, imputación, codificación y clasificación.

| Comprobación | Resultado |
|---|---|
| Dimensiones | 8,124 × 23 |
| Ausentes reconocidos | 2,480 en stalk-root |
| Filas duplicadas | 0 |
| Predictores duplicados por fila | 0 |
| Entrenamiento | 6,499 registros |
| Prueba | 1,625 registros |
| F1 macro de referencia | 0.3413052290 |
| F1 macro de SVM | 1.0000000000 |
| Recall de p en SVM | 1.0000000000 |

Esta ejecución adicional es una comprobación del análisis, no una ampliación de las siete pruebas pytest recibidas.

## Incidencia del notebook original

La primera celda de código del notebook de hongos contiene una instrucción en español sin comentar. Su análisis sintáctico produce un error.

La instrucción debe estar en una celda Markdown o convertirse en comentario. La versión corregida presentada en esta entrega elimina esa incidencia.

## Repetir las pruebas en Windows

Desde la raíz del proyecto:

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m pytest -q
```

El tiempo de ejecución puede variar entre equipos.
````

**6. Conclusión — 300 a 500 palabras**

```md
# Conclusión

El proyecto permitió desarrollar y comprobar un procedimiento de clasificación supervisada para distinguir las etiquetas de comestibilidad del conjunto Mushroom mediante una máquina de vectores de soporte con kernel RBF. Se trabajó con 8,124 registros y 22 variables predictoras categóricas. La variable objetivo, denominada `class`, presentó 4,208 registros comestibles y 3,916 registros pertenecientes a la categoría venenosa o no recomendada.

La auditoría evidenció la importancia de interpretar los códigos antes de evaluar la calidad de los datos. Aunque la lectura inicial no identificaba valores ausentes, el reconocimiento del símbolo `?` permitió detectar 2,480 faltantes en `stalk-root`, equivalentes al 30.53 % de esa columna. No se encontraron filas completamente duplicadas. También se identificó que `veil-type` era constante; se conservó para mantener el esquema, sin atribuirle capacidad para diferenciar los registros.

El procedimiento utilizó una división estratificada de 80 % para entrenamiento y 20 % para prueba, con semilla 42. La imputación por categoría más frecuente y la codificación One-Hot se incorporaron dentro de pipelines, ajustados exclusivamente con los datos de entrenamiento. Esta organización evitó incorporar información del conjunto de prueba al aprendizaje de las transformaciones. La SVM utilizó parámetros fijos, sin búsqueda de hiperparámetros.

La línea base obtuvo un F1 macro de 0.3413 y una exactitud de 0.5182. Como siempre predijo la clase mayoritaria, no identificó ningún registro de clase `p`. La SVM alcanzó F1 macro, exactitud, precisión y sensibilidad de la clase `p` iguales a 1.0000. En los 1,625 registros de prueba clasificó correctamente 842 casos `e` y 783 casos `p`, sin errores observados.

Estos resultados muestran una mejora clara frente a la referencia dentro de la partición utilizada, pero requieren una interpretación limitada. El conjunto contiene descripciones hipotéticas y la evaluación no demuestra generalización a nuevas especies o condiciones de observación. Además, la partición de prueba ya había sido examinada en el notebook original; la ejecución realizada constituye una comprobación de reproducibilidad, no una nueva validación independiente.

Finalmente, las siete pruebas recibidas fueron aprobadas, aunque las pruebas del modelo numérico corresponden al ejercicio de tumores. Como continuación, conviene incorporar pruebas específicas del pipeline categórico y diseñar una evaluación adicional previamente definida. El principal aporte del trabajo consiste en integrar auditoría, tratamiento explícito de ausentes, prevención de fugas y comunicación verificable de resultados.
```

[1]: https://archive.ics.uci.edu/dataset/73/mushroom?utm_source=chatgpt.com "UCI Machine Learning Repository"
[2]: https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names?utm_source=chatgpt.com "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names"
