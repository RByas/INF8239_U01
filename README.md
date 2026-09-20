# U01.LAB00 — Preparación y validación del entorno profesional

**Estudiante:** Roberto Byas de la Cruz  
**Asignatura:** INF-8239 Ciencia de Datos II  
**Unidad:** 01 - Modelos avanzados, reducción dimensional y Green AI  
**Código:** U01.LAB00  
**Sistema operativo utilizado:** Windows 11  
**Terminal:** Windows PowerShell o PowerShell integrado en Visual Studio Code

> **Resultado esperado:** Python, VS Code, Git y Jupyter comprobados; proyecto reproducible; entorno virtual activo; prueba unitaria aprobada y primer commit.

Este documento reúne los comandos del laboratorio adaptados a Windows 11. Los resultados señalados son esperados: deben confirmarse mediante ejecución en el equipo. Puede guardarse como `README.md` en la raíz de `INF8239_U01`.

## 1. Antes de comenzar

- Contar con permisos para instalar aplicaciones e internet para descargar dependencias.
- Usar una carpeta local; Google Drive no es una ruta obligatoria.
- Tener una cuenta de GitHub únicamente si se publicará el repositorio.
- Ejecutar los bloques `powershell` en PowerShell, en el orden indicado. Los bloques `python`, `text` y `gitignore` son contenido de archivos o celdas, no comandos de PowerShell.
- Si el proyecto ya existe, abrir su carpeta y continuar desde el paso pendiente. No sobrescribir archivos que ya contengan trabajo.

## 2. Instalar y verificar Python

Descargar Python de 64 bits desde [Python para Windows](https://www.python.org/downloads/windows/). En el instalador clásico marcar **Add python.exe to PATH**. La guía requiere Python 3.11 o superior. Abrir una terminal nueva después de instalar.

```powershell
python --version
python -m pip --version
python -c "import sys, struct; print(sys.executable); print('Arquitectura:', struct.calcsize('P') * 8, 'bits')"
```

**Verificación:** versión requerida, arquitectura de 64 bits e intérprete identificado. Después de activar `.venv`, volver a verificar que Python y pip correspondan a ese entorno.

## 3. Instalar y configurar Git

Instalar desde [Git para Windows](https://git-scm.com/downloads/win). Abrir una terminal nueva. El siguiente bloque solicita el correo real para evitar registrar un correo de ejemplo.

```powershell
git --version
git config --global user.name "Roberto Byas de la Cruz"
git config --global user.email "robertobyas6@gmail.com"
git config --global --list
```

La configuración global se aplica también a otros repositorios del usuario. Revisar el nombre y correo antes del primer commit.

## 4. Preparar Visual Studio Code

Instalar [Visual Studio Code](https://code.visualstudio.com/). Abrir **Extensions** con `Ctrl+Shift+X` e instalar:

- **Python**, **Jupyter** y **Pylance**, publicadas por Microsoft.
- **Ruff**, publicada por Astral.

Abrir **Terminal > New Terminal** y seleccionar PowerShell.

## 5. Crear la estructura del proyecto

Abrir PowerShell en la carpeta donde se guardará el curso. Ejecutar este bloque si aún no se ha creado el proyecto:

```powershell
New-Item -ItemType Directory -Path "INF8239_U01" -Force
Set-Location "INF8239_U01"
New-Item -ItemType Directory -Path "data", "notebooks", "reports", "src", "tests" -Force
```

Abrir esta carpeta mediante **File > Open Folder**. Ejecutar los comandos siguientes desde la raíz `INF8239_U01`. Comprobar la ubicación con:

```powershell
Get-Location
```

Se usa `New-Item` con una lista separada por comas para crear carpetas correctamente en PowerShell.

## 6. Crear y activar el entorno virtual

Crear el entorno solo si no existe:

```powershell
python -m venv .venv
```

Activarlo:

```powershell
.\.venv\Scripts\Activate.ps1
```

**Solo si aparece “la ejecución de scripts está deshabilitada”**, permitir la activación para la sesión actual y repetirla:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
```

El cambio de política termina al cerrar esa sesión de PowerShell. Si el equipo tiene una política institucional que lo impide, consultar con su administrador.

Verificar el intérprete y pip:

```powershell
python -c "import sys; print(sys.executable); assert sys.prefix != sys.base_prefix, 'El entorno virtual no esta activo'"
python -m pip --version
```

**Resultado esperado:** indicador `(.venv)` en la terminal y rutas que contengan `.venv`.

## 7. Crear e instalar las dependencias

En VS Code, crear `requirements.txt` en la raíz con el siguiente contenido:

```text
numpy>=1.26
pandas>=2.2
scikit-learn>=1.4
matplotlib>=3.8
seaborn>=0.13
joblib>=1.3
pytest>=8.0
ipykernel>=6.29
```

Se añade `ipykernel` para ejecutar el notebook con el Python del entorno desde VS Code.

Con `.venv` activo:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
```

**Resultado esperado:** instalación sin errores y `No broken requirements found.`

Guardar las versiones efectivamente instaladas para facilitar la reproducción en un entorno compatible:

```powershell
python -m pip freeze | Set-Content -Encoding UTF8 requirements-lock.txt
```

Los límites `>=` de `requirements.txt` no fijan versiones exactas. `requirements-lock.txt` registra las versiones instaladas; también deben conservarse la versión de Python y el sistema operativo.

## 8. Crear el módulo y la primera prueba

Crear un archivo vacío llamado `src/inf8239_u01/__init__.py`.

Crear `src/inf8239_u01/environment.py` con este contenido Python:

```python
def environment_message() -> str:
    return "Entorno INF-8239 listo"
```

Crear `tests/test_environment.py` con este contenido Python:

```python
from inf8239_u01.environment import environment_message


def test_environment_message():
    assert environment_message() == "Entorno INF-8239 listo"
```

Ejecutar desde la raíz del proyecto:

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location).Path "src")
python -m pytest -q
```

**Resultado esperado:** `1 passed` y un tiempo de ejecución variable. `PYTHONPATH` se establece para esta sesión; repetir la asignación si se abre otra terminal.

## 9. Verificar Jupyter en VS Code

1. Abrir la paleta con `Ctrl+Shift+P`.
2. Ejecutar **Python: Select Interpreter** y elegir `.venv\Scripts\python.exe`.
3. Ejecutar **Jupyter: Create New Jupyter Notebook** y guardar como `notebooks/00_verificacion.ipynb`.
4. En **Select Kernel**, elegir **Python Environments** y el entorno `.venv` del proyecto.
5. Ejecutar esta celda Python y guardar el notebook con su salida:

```python
import sys
import platform

print("Interprete:", sys.executable)
print("Python:", sys.version)
print("Sistema:", platform.platform())
assert ".venv" in sys.executable.lower()
assert sys.prefix != sys.base_prefix
```

**Resultado esperado:** ruta del intérprete dentro de `.venv`, versión de Python y sistema Windows, sin error en las comprobaciones. Para registrar la edición exacta de Windows desde PowerShell:

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, OSArchitecture
```

La versión interna del sistema puede comenzar con `10.0` aunque la edición sea Windows 11; revisar `Caption`.

## 10. Preparar Git y realizar el primer commit

Guardar este documento como `README.md` en la raíz **antes** del commit. Crear `.gitignore` con el siguiente contenido:

```gitignore
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/
.ipynb_checkpoints/
*.joblib
data/raw/*
!data/raw/.gitkeep
```

Para conservar las carpetas vacías en Git, crear sus archivos marcadores:

```powershell
New-Item -ItemType File -Path "data\raw\.gitkeep", "notebooks\.gitkeep", "reports\.gitkeep" -Force
```

Inicializar el repositorio y preparar los archivos:

```powershell
git init
git add .
git status
```

Revisar que `.venv` no aparezca entre los archivos preparados y que sí estén los archivos del laboratorio. Luego ejecutar:

```powershell
git commit -m "chore: create INF-8239 reproducible environment"
git status
git log --oneline
```

**Resultado esperado:** `working tree clean` y primer commit visible. Este paso crea un repositorio local; publicar en GitHub es una operación posterior.

## 11. Comprobar la estructura y retomar el trabajo

Mostrar las carpetas del proyecto y los archivos principales, evitando listar las dependencias de `.venv`:

```powershell
Get-ChildItem -Directory | Where-Object { $_.Name -ne '.venv' } | Select-Object Name
Get-ChildItem -File | Select-Object Name
Get-ChildItem -Path src, tests, notebooks, reports, data -Recurse | Select-Object FullName
```

Al volver a abrir PowerShell en la raíz del proyecto:

```powershell
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH = (Join-Path (Get-Location).Path "src")
python -m pytest -q
git status
```

Si vuelve a bloquearse la activación, aplicar la solución temporal del apartado 6. Para salir del entorno al finalizar:

```powershell
deactivate
```

## 12. Errores frecuentes

| Situación | Corrección |
| --- | --- |
| `python` no se reconoce | Abrir una terminal nueva y verificar la instalación y PATH. |
| PowerShell bloquea `Activate.ps1` | Aplicar la política de alcance `Process` indicada en el apartado 6 y activar de nuevo. |
| `pytest` no se reconoce | Usar `python -m pytest -q` con `.venv` activo y las dependencias instaladas. |
| `No module named ipykernel` | Con `.venv` activo, repetir `python -m pip install -r requirements.txt`. |
| El notebook usa otro Python | Seleccionar el kernel `.venv` del proyecto y reiniciar el kernel. |
| `ModuleNotFoundError: inf8239_u01` | Establecer `PYTHONPATH` como en el apartado 8 y comprobar la ubicación de `src/inf8239_u01`. |
| Git rechaza el commit por identidad desconocida | Configurar `user.name` y `user.email` como en el apartado 3. |
| `nothing to commit` | Revisar `git log --oneline`; puede existir ya un commit y no haber cambios nuevos. |
| Las carpetas no se crean con `mkdir data notebooks ...` | Usar el bloque `New-Item` del apartado 5, adaptado a PowerShell. |
