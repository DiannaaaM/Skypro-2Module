import os
from unittest.mock import Mock, patch

import pytest

from src.utils import read_json_file


@pytest.fixture()
def path_to_json_file() -> str:
    file = os.path.abspath(os.path.join("..", "data", "operations.json"))
    return file


def test_read_json_file(path_to_json_file: str) -> None:
    assert len(read_json_file(path_to_json_file)) == 101
