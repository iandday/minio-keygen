import argparse
import minio_keygen


def parse_args(args: list) -> argparse.Namespace:
    """parse command line arguments

    Args:
        args (list): command line arguments sys.argv[1:]

    Returns:
        argparse.Namespace: parsed arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose',
                        action='count',
                        default=0,
                        help="Verbosity (-v, -vv, etc)"
                        )
    parser.add_argument('--version',
                        action='version',
                        version="%(prog)s (version {ver})".format(ver=minio_keygen.__version__) # noqa
                        )

    return parser.parse_args(args)
