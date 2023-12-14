"""Testing module for cli of rt."""

from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from rt import cli


@pytest.mark.parametrize(
    "fn",
    [("load"), ("run")],
)
def test_json_cli(fn):
    with patch(f"rt.json_helper.JsonToRichTable.{fn}") as mocker:
        cli.main(is_json=True)
        mocker.assert_called_once()


@pytest.mark.parametrize(
    "fn",
    [("load"), ("run")],
)
def test_yaml_cli(fn):
    with patch(f"rt.yaml_helper.YamlToRichTable.{fn}") as mocker:
        cli.main(is_yaml=True)
        mocker.assert_called_once()


@pytest.mark.parametrize(
    "fn",
    [("load"), ("run")],
)
def test_csv_cli(fn):
    with patch(f"rt.csv_helper.CsvToRichTable.{fn}") as mocker:
        cli.main(is_csv=True)
        mocker.assert_called_once()


@pytest.mark.parametrize(
    "fn",
    [("load"), ("run")],
)
def test_file_cli(fn):
    with patch(f"rt.file_helper.FileToRichTable.{fn}") as mocker:
        cli.main(file="tests/resources/test.csv")
        mocker.assert_called_once()


def test_plain_cli():
    runner = CliRunner()
    result = runner.invoke(cli.cli)
    assert result.exit_code == 1
    assert "No file nor any one of json, yaml or csv chosen!" in result.stdout
