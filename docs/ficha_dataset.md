# Fichas de los datasets: Mushroom Classification y Car Evaluation

Ambos datasets permiten completar los seis campos de la ficha. Esto es distinto de cumplir todos los criterios de aceptación del laboratorio.

| Campo | Mushroom Classification | Car Evaluation |
|---|---|---|
| **Dominio** | Clasificación biológica de hongos con fines académicos. | Evaluación multicriterio de automóviles. |
| **Unidad de análisis** | Una muestra hipotética de hongo descrita mediante características físicas y ecológicas. | Una configuración de automóvil descrita mediante seis atributos. |
| **Decisión** | Predecir la categoría de comestibilidad registrada para la muestra. | Predecir la aceptabilidad de la configuración según el modelo de referencia. |
| **Target** | `class`: `e` = comestible; `p` = venenoso o no recomendado. | `class`: `unacc` = inaceptable; `acc` = aceptable; `good` = bueno; `vgood` = muy bueno. |
| **Error más costoso** | Clasificar como comestible una muestra de clase venenosa o no recomendada. | Clasificar una configuración inaceptable como buena o muy buena. |
| **Usuario** | Estudiantes, docentes e investigadores que estudian clasificación supervisada. | Estudiantes, docentes e investigadores que desarrollan sistemas de apoyo a decisiones. |



## Localizar y comparar dos candidatos



| Criterio | Candidato A: Mushroom | Candidato B: Car Evaluation |
|---|---|---|
| **Procedencia** | Descripciones de muestras hipotéticas basadas en *The Audubon Society Field Guide to North American Mushrooms*. | Configuraciones evaluadas mediante un modelo jerárquico de decisión. |
| **Autor o fuente original** | Guía Audubon; la ficha UCI no identifica un autor individual del dataset. | Marko Bohanec. |
| **Fecha de incorporación a UCI** | 26 de abril de 1987. | 31 de mayo de 1997. |
| **Licencia institucional** | CC BY 4.0: permite uso académico con atribución. | CC BY 4.0: permite uso académico con atribución. |
| **Filas/columnas** | 8,124 filas y 23 columnas: 22 predictores y una etiqueta. | 1,728 filas y 7 columnas: seis predictores y una etiqueta. |
| **Tamaño del archivo original** | `agaricus-lepiota.data`: 373,704 bytes. | `car.data`: 51,867 bytes. |
| **Target y clases** | Etiqueta de comestibilidad: `e` = comestible; `p` = venenoso o no recomendado. | Aceptabilidad: `unacc` = inaceptable; `acc` = aceptable; `good` = bueno; `vgood` = muy bueno. |
| **Distribución de clases** | `e`: 4,208; `p`: 3,916. | `unacc`: 1,210; `acc`: 384; `good`: 69; `vgood`: 65. |
| **Ausentes** | 2,480 valores `?` en `stalk-root`. Deben interpretarse como ausentes. | Sin valores ausentes en el original auditado. |
| **Diccionario** | La ficha UCI y `agaricus-lepiota.names` explican atributos y códigos. | La ficha UCI y `car.names` explican los seis atributos y las clases. |
| **Riesgo de fuga** | Incluir la etiqueta como predictor o ajustar imputación/codificación antes de separar los datos. | Incluir la etiqueta o atributos derivados de ella; ajustar el preprocesamiento antes de separar los datos. |



### URL de documentación y descarga

| Recurso | Mushroom | Car Evaluation |
|---|---|---|
| **Ficha institucional** | [Documentación UCI](https://archive.ics.uci.edu/dataset/73/mushroom) | [Documentación UCI](https://archive.ics.uci.edu/dataset/19/car+evaluation) |
| **Descarga directa** | [ZIP de Mushroom](https://archive.ics.uci.edu/static/public/73/mushroom.zip) | [ZIP de Car Evaluation](https://archive.ics.uci.edu/static/public/19/car+evaluation.zip) |
| **Copia en Kaggle** | [Mushroom Classification](https://www.kaggle.com/datasets/uciml/mushroom-classification) | [Car Evaluation — kryusufkaya](https://www.kaggle.com/datasets/kryusufkaya/car-evaluation) |

Los enlaces directos descargan archivos ZIP. El procedimiento reproducible deberá incluir su extracción y la asignación de encabezados a los archivos originales.

## Aplicar criterios de aceptación

| Criterio | Mushroom | Car Evaluation |
|---|---|---|
| **Al menos 500 filas** | Cumple: 8,124. | Cumple: 1,728. |
| **Target observable y mínimo dos clases** | Tiene una etiqueta registrada y dos clases. Debe declararse que describe muestras hipotéticas. | Tiene una etiqueta registrada y cuatro clases. Debe declararse que la evaluación procede de un modelo de decisión. |
| **Datos permitidos para uso académico** | Cumple, con atribución conforme a CC BY 4.0 de UCI. | Cumple, con atribución conforme a CC BY 4.0 de UCI. |
| **Variables disponibles al predecir** | Cumple bajo la formulación propuesta: se predice después de observar las características requeridas. | Cumple bajo la formulación propuesta: los seis atributos se conocen antes de asignar la categoría. |
| **Compatible con CPU/Colab gratuito** | Adecuado por su tamaño; falta medir el tiempo del pipeline. | Adecuado por su tamaño; falta medir el tiempo del pipeline. |
| **No repetido por otro estudiante** | Pendiente de confirmación. | Pendiente de confirmación. |





