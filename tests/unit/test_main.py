"""Testing module for main entrypoint into rt cli."""

import runpy
from unittest import mock


@mock.patch("rt.cli.entrypoint")
def test_cli_init(cli):
    runpy.run_path("rt/__main__.py", run_name="__main__")
    cli.assert_called_once_with()
