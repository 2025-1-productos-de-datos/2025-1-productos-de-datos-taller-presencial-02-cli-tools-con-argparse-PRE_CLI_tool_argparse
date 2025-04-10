"""Command line interface (CLI) tool"""

import argparse

#
# Estructura:
#
# mycli +--- command_1
#       |    +--- subcommand_1
#       |    \--- subcommand_2
#       |
#       +--- command_2
#       |    +--- subcommand_1
#       |    \--- subcommand_2
#


def command_1_subcommand_1(args):
    print(f"\n---> Ejecutando command 1 subcommand 1: a = {args.a}\n")


def command_1_subcommand_2(args):
    print(f"\n---> Ejecutando command 1 subcommand 2: b = {args.b}\n")


def command_2_subcommand_1(args):
    print(f"\n---> Ejecutando command 2 subcommand 1: c = {args.c}\n")


def command_2_subcommand_2(args):
    print(f"\n---> Ejecutando command 2 subcommand 2: d = {args.d}\n")


def main():

    # =========================================================================
    # Crear el parser principal
    parser = argparse.ArgumentParser(
        prog="mycli",
        description="Herramienta de linea de comandos",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Comandos principales",
    )

    # =========================================================================
    #
    # Commando 1
    #
    command_1_parser = subparsers.add_parser(
        "COMMAND1",
        help="Comandos relacionados con COMMAND1",
    )
    command_1_subparsers = command_1_parser.add_subparsers(
        dest="subcommand",
        help="Esta es la ayuda del COMMAND1",
    )

    #
    # Subcomando: 1-1
    #
    command_1_subcommand_1_parser = command_1_subparsers.add_parser(
        "run",
        help="Ejecuta un subcomando 1-1",
    )
    command_1_subcommand_1_parser.add_argument(
        "--a",
        required=True,
        help="Valor del parametro a",
    )
    command_1_subcommand_1_parser.set_defaults(
        func=command_1_subcommand_1,
    )

    #
    # Subcomando: 1-2
    #
    command_1_subcommand_2_parser = command_1_subparsers.add_parser(
        "stop",
        help="Ejecuta un subcomando 1-2",
    )
    command_1_subcommand_2_parser.add_argument(
        "--b",
        required=True,
        help="Valor del parametro b",
    )
    command_1_subcommand_2_parser.set_defaults(
        func=command_1_subcommand_2,
    )

    # =========================================================================
    #
    # Commando 2
    #
    command_2_parser = subparsers.add_parser(
        "COMMAND2",
        help="Comandos relacionados con COMMAND2",
    )
    command_2_subparsers = command_2_parser.add_subparsers(
        dest="subcommand",
        help="Acciones con imágenes",
    )

    #
    # Subcomando: 1-2
    #
    command_2_subcommand_1_parser = command_2_subparsers.add_parser(
        "jump",
        help="Ejecuta un subcomando 2-1",
    )
    command_2_subcommand_1_parser.add_argument(
        "--c",
        required=True,
        help="Valor del parametro c",
    )
    command_2_subcommand_1_parser.set_defaults(
        func=command_2_subcommand_1,
    )

    #
    # Subcomando: 2-2
    #
    command_2_subcommand_2_parser = command_2_subparsers.add_parser(
        "cry",
        help="Ejecuta un subcomando 2-2",
    )
    command_2_subcommand_2_parser.add_argument(
        "--d",
        required=True,
        help="Valor del parametro d",
    )
    command_2_subcommand_2_parser.set_defaults(
        func=command_2_subcommand_2,
    )

    # =========================================================================
    # Parsea  argumentos y ejecuta la función asociada
    #
    args = parser.parse_args()

    # Ejecutar la función asociada
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
