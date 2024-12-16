from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, field_validator

from secrets_vault import vault_root
from secrets_vault.infrastructure_layer import (
    create_vault_path,
    is_valid_path,
)


class VaultPath(BaseModel):
    path: str
    pure_path: Path | None = None
    root_path: str = next(iter(vault_root.__path__))

    @field_validator("path")
    def validate_path_is_valid(cls: VaultPath, path_string: str) -> str:  # pylint: disable=no-self-argument, no-self-use
        path = is_valid_path(cls, path_string)
        create_vault_path(path)
        return path_string

    def model_post_init(self, __context: Any) -> None:
        self.pure_path = Path(os.path.join(self.root_path, self.path))  # noqa: PTH118

    model_config = ConfigDict(arbitrary_types_allowed=True)
