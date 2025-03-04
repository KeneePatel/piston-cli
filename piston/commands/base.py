import argparse


class Base:
    """TODO: Write a Docstring here."""

    @staticmethod
    def run() -> argparse.Namespace:
        """TODO: Write a Docstring here."""
        prog = argparse.ArgumentParser(
            prog="piston",
            description="Compile code snippets through the piston api "
            "for over 36 languages",
        )

        prog.add_argument(
            "-list",
            "--list",
            action="store_true",
            help="List all the available languages",
        )

        prog.add_argument(
            "-f",
            "--file",
            type=str,
            help="Compile a file directly, full path to the file must be provided",
            required=False,
        )

        prog.add_argument(
            "-l",
            "--link",
            action="store_true",
            help="Run code directly from a link",
        )

        prog.add_argument(
            "-t",
            "--theme",
            type=str,
            help="Change the default theme (solarized-dark) of code, to see "
            "available themes use -T or --themelist",
            required=False,
        )

        prog.add_argument(
            "-T",
            "--themelist",
            action="store_true",
            help="List all the available themes/colorschemes",
        )

        prog.add_argument(
            "-s",
            "--shell",
            type=str,
            help="Run code from within a shell environment, "
            "the passed value is the language to use",
            required=False,
        )

        prog.add_argument(
            "-c",
            "--config",
            type=str,
            help=(
                "Path to the piston-cli config file, "
                "leave blank if your config is in the system default location specified on the readme"
            ),
        )

        args = prog.parse_args()

        return args


Base = Base()
