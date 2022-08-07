#  Copyright (c) ZenML GmbH 2020. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Utility functions to help with YAML files and data."""

import json
from pathlib import Path
from typing import Any, Dict, Optional, Type
from uuid import UUID

import yaml

from zenml.io import fileio
from zenml.utils import io_utils


def write_yaml(
    file_path: str, contents: Dict[Any, Any], sort_keys: bool = True
) -> None:
    """Write contents as YAML format to file_path.

    Args:
        file_path: Path to YAML file.
        contents: Contents of YAML file as dict.
        sort_keys: If `True`, keys are sorted alphabetically. If `False`,
            the order in which the keys were inserted into the dict will
            be preserved.

    Raises:
        FileNotFoundError: if directory does not exist.
    """
    if not io_utils.is_remote(file_path):
        dir_ = str(Path(file_path).parent)
        if not fileio.isdir(dir_):
            raise FileNotFoundError(f"Directory {dir_} does not exist.")
    io_utils.write_file_contents_as_string(
        file_path, yaml.dump(contents, sort_keys=sort_keys)
    )


def append_yaml(file_path: str, contents: Dict[Any, Any]) -> None:
    """Append contents to a YAML file at file_path.

    Args:
        file_path: Path to YAML file.
        contents: Contents of YAML file as dict.

    Raises:
        FileNotFoundError: if directory does not exist.
    """
    file_contents = read_yaml(file_path) or {}
    file_contents.update(contents)
    if not io_utils.is_remote(file_path):
        dir_ = str(Path(file_path).parent)
        if not fileio.isdir(dir_):
            raise FileNotFoundError(f"Directory {dir_} does not exist.")
    io_utils.write_file_contents_as_string(file_path, yaml.dump(file_contents))


def read_yaml(file_path: str) -> Any:
    """Read YAML on file path and returns contents as dict.

    Args:
        file_path: Path to YAML file.

    Returns:
        Contents of the file in a dict.

    Raises:
        FileNotFoundError: if file does not exist.
    """
    if fileio.exists(file_path):
        contents = io_utils.read_file_contents_as_string(file_path)
        # TODO: [LOW] consider adding a default empty dict to be returned
        #   instead of None
        return yaml.safe_load(contents)
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")


def is_yaml(file_path: str) -> bool:
    """Returns True if file_path is YAML, else False.

    Args:
        file_path: Path to YAML file.

    Returns:
        True if is yaml, else False.
    """
    if file_path.endswith("yaml") or file_path.endswith("yml"):
        return True
    return False


def write_json(
    file_path: str,
    contents: Dict[str, Any],
    encoder: Optional[Type[json.JSONEncoder]] = None,
) -> None:
    """Write contents as JSON format to file_path.

    Args:
        file_path: Path to JSON file.
        contents: Contents of JSON file as dict.
        encoder: Custom JSON encoder to use when saving json.

    Raises:
        FileNotFoundError: if directory does not exist.
    """
    if not io_utils.is_remote(file_path):
        dir_ = str(Path(file_path).parent)
        if not fileio.isdir(dir_):
            # Check if it is a local path, if it doesn't exist, raise Exception.
            raise FileNotFoundError(f"Directory {dir_} does not exist.")
    io_utils.write_file_contents_as_string(
        file_path,
        json.dumps(
            contents,
            cls=encoder,
        ),
    )


def read_json(file_path: str) -> Any:
    """Read JSON on file path and returns contents as dict.

    Args:
        file_path: Path to JSON file.

    Returns:
        Contents of the file in a dict.

    Raises:
        FileNotFoundError: if file does not exist.
    """
    if fileio.exists(file_path):
        contents = io_utils.read_file_contents_as_string(file_path)
        return json.loads(contents)
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")


def write_json_string(
    file_path: str,
    contents: str,
) -> None:
    """Write contents as JSON format to file_path.

    Args:
        file_path: Path to JSON file.
        contents: Contents of JSON file as str.

    Raises:
        FileNotFoundError: if directory does not exist.
    """
    if not io_utils.is_remote(file_path):
        dir_ = str(Path(file_path).parent)
        if not fileio.isdir(dir_):
            # Check if it is a local path, if it doesn't exist, raise Exception.
            raise FileNotFoundError(f"Directory {dir_} does not exist.")
    io_utils.write_file_contents_as_string(file_path, contents)


def read_json_string(file_path: str) -> Any:
    """Read JSON on file path and returns contents as json string.

    Args:
        file_path: Path to JSON file.

    Returns:
        Contents of the file in a string.

    Raises:
        FileNotFoundError: if file does not exist.
    """
    if fileio.exists(file_path):
        return io_utils.read_file_contents_as_string(file_path)
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")


class UUIDEncoder(json.JSONEncoder):
    """JSON encoder for UUID objects."""

    def default(self, obj: Any) -> Any:
        """Default UUID encoder for JSON.

        Args:
            obj: Object to encode.

        Returns:
            Encoded object.
        """
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)