"""Autograding script."""

import homework.myclitool as myclitool


def test_c1_s1(capsys):

    args = type("Args", (), {"a": "1"})

    myclitool.command_1_subcommand_1(args)

    captured = capsys.readouterr()
    assert "---> Ejecutando command 1 subcommand 1: a = 1" in captured.out


def test_c1_s2(capsys):

    args = type("Args", (), {"b": "2"})

    myclitool.command_1_subcommand_2(args)

    captured = capsys.readouterr()
    assert "---> Ejecutando command 1 subcommand 2: b = 2" in captured.out


def test_c2_s1(capsys):

    args = type("Args", (), {"c": "3"})

    myclitool.command_2_subcommand_1(args)

    captured = capsys.readouterr()
    assert "---> Ejecutando command 2 subcommand 1: c = 3" in captured.out


def test_c2_s2(capsys):

    args = type("Args", (), {"d": "4"})

    myclitool.command_2_subcommand_2(args)

    captured = capsys.readouterr()
    assert "---> Ejecutando command 2 subcommand 2: d = 4" in captured.out
