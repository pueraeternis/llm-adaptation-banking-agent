import json
from pathlib import Path


def clean_notebook(path: Path) -> None:
    nb = json.loads(path.read_text(encoding="utf-8"))

    # Remove noisy/brittle widget state that breaks GitHub rendering.
    nb.get("metadata", {}).pop("widgets", None)

    for cell in nb.get("cells", []):
        # Clear execution artifacts so the notebook stays diff-friendly.
        if cell.get("cell_type") == "code":
            cell["execution_count"] = None
            cell["outputs"] = []

        # Drop per-cell execution metadata that Colab can add.
        meta = cell.get("metadata", {})
        for k in ["execution", "outputId", "collapsed", "scrolled"]:
            meta.pop(k, None)
        if meta == {}:
            cell["metadata"] = {}

    path.write_text(
        json.dumps(nb, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    clean_notebook(Path("notebooks/banking_agent.ipynb"))
