from __future__ import annotations

import os
from pathlib import Path

from pydantic import BaseModel, ConfigDict, field_validator

from secrets_vault import vault_root


class VaultPath(BaseModel):
    path: str
    pure_path: Path | None = None
    root_path: str = next(iter(vault_root.__path__))

    @field_validator("path")
    def validate_path_is_valid(cls: VaultPath, path_string: str) -> str:  # pylint: disable=no-self-argument
        path = Path(os.path.join(cls.model_fields["root_path"].default, path_string))  # noqa: PTH118
        if (
            path.is_file()
            or path_string.count(os.path.sep) < 1
            or not path_string.endswith(".txt")
        ):
            msg = f"""Path '{path_string}' is not valid.
            It must point to either a new or old directory and to a new .txt file"""
            raise ValueError(msg)
        path.mkdir(parents=True, exist_ok=True)
        return path_string

    def __post_init_post_parse__(self) -> None:  # pylint: disable=bad-dunder-name
        self.pure_path = Path(os.path.join(self.root_path, self.path))  # noqa: PTH118

    model_config = ConfigDict(arbitrary_types_allowed=True)
