from pathlib import Path
import pandas as pd

TARGET = "class"
REQUIRED = {TARGET, "odor"}

# Este archivo de pruebas debe ubicarse en la carpeta tests/
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "dataset.csv"


def load_data():
    return pd.read_csv(DATA_PATH, na_values=["?"])


def test_dataset_is_not_empty():
    assert not load_data().empty, "El dataset está vacío."


def test_required_columns_exist():
    columns = set(load_data().columns)
    missing = REQUIRED - columns
    assert not missing, f"Faltan columnas requeridas: {missing}"


def test_target_has_no_missing_and_two_classes():
    y = load_data()[TARGET]
    assert y.notna().all(), "El target contiene valores ausentes."
    assert set(y.unique()) == {"e", "p"}, (
        "El target debe contener exactamente las clases 'e' y 'p'."
    )