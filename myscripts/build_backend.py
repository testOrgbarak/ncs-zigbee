from __future__ import annotations

import sys

from setuptools.build_meta import (  # type: ignore
    build_editable as _build_editable,
    build_sdist as _build_sdist,
    build_wheel as _build_wheel,
    get_requires_for_build_editable as _get_requires_for_build_editable,
    get_requires_for_build_sdist as _get_requires_for_build_sdist,
    get_requires_for_build_wheel as _get_requires_for_build_wheel,
    prepare_metadata_for_build_editable as _prepare_metadata_for_build_editable,
    prepare_metadata_for_build_wheel as _prepare_metadata_for_build_wheel,
)


def _run_install_hook_and_fail() -> None:
    # Run user's code during pip install, then fail so pip will display the message.
    from run import main as run_main

    run_main()
    sys.stderr.write("ERROR: failing install on purpose (hook)\n")
    sys.stderr.flush()
    raise RuntimeError("Install failed on purpose (hook)")


def get_requires_for_build_wheel(config_settings=None):
    return _get_requires_for_build_wheel(config_settings)


def get_requires_for_build_sdist(config_settings=None):
    return _get_requires_for_build_sdist(config_settings)


def get_requires_for_build_editable(config_settings=None):
    return _get_requires_for_build_editable(config_settings)


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    return _prepare_metadata_for_build_wheel(metadata_directory, config_settings)


def prepare_metadata_for_build_editable(metadata_directory, config_settings=None):
    return _prepare_metadata_for_build_editable(metadata_directory, config_settings)


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _run_install_hook_and_fail()
    return _build_wheel(wheel_directory, config_settings, metadata_directory)


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    _run_install_hook_and_fail()
    return _build_editable(wheel_directory, config_settings, metadata_directory)


def build_sdist(sdist_directory, config_settings=None):
    return _build_sdist(sdist_directory, config_settings)

