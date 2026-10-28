"""Executa cada notebook em kernel e pasta temporária independentes."""
from pathlib import Path
from tempfile import TemporaryDirectory

import nbformat
from nbclient import NotebookClient


def main():
    root = Path(__file__).resolve().parents[2]
    for name in ("WorkshopPandas.ipynb", "WorkshopPandas_gabarito.ipynb"):
        notebook = nbformat.read(root / name, as_version=4)
        nbformat.validate(notebook)
        with TemporaryDirectory(prefix="minicurso-ci-") as folder:
            NotebookClient(
                notebook,
                timeout=120,
                kernel_name="python3",
                allow_errors=False,
                resources={"metadata": {"path": folder}},
            ).execute()
        code_cells = sum(cell.cell_type == "code" for cell in notebook.cells)
        print(f"{name}: {code_cells} células executadas sem erro")


if __name__ == "__main__":
    main()
