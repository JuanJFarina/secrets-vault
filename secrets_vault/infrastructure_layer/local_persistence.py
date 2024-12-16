import os
from pathlib import Path
from typing import Any


def is_valid_path(cls: Any, path_string: str) -> Path:
    path = Path(os.path.join(cls.model_fields["root_path"].default, path_string))  # noqa: PTH118
    if (
        path.is_file()
        or path_string.count(os.path.sep) < 1
        or not path_string.endswith(".txt")
    ):
        msg = f"""Path '{path_string}' is not valid.
        It must point to either a new or old directory and to a new .txt file"""
        raise ValueError(msg)
    return path


def create_vault_path(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
