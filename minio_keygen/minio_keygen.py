#!/usr/bin/env python3
"""
MinIO Key Generator
"""

__author__ = "Ian Day"
__version__ = "0.1.0"
__license__ = "GNU GPL"

import argparse
import secrets
from typing import Tuple
import sys


def compute_keys(key_l: int, secret_l: int) -> Tuple[str, str]:
    """compute access key and token value

    Args:
        key_l (int): byte length for the key value
        secret_l (int): byte length for the secret value

    Returns:
        Tuple[str, str]: key and secret value
    """

    if not isinstance(key_l, int):
        try:
            key_l = int(key_l)
        except ValueError as value_error:
            print('Invalid input for key length')
            raise SystemExit(1) from value_error

    if not isinstance(secret_l, int):
        try:
            secret_l = int(secret_l)
        except ValueError as value_error:
            print('Invalid input for secret length')
            raise SystemExit(1) from value_error

    key = secrets.token_urlsafe(nbytes=key_l)
    secret = secrets.token_urlsafe(nbytes=secret_l)

    return(key, secret)


def parse_args(args: list) -> argparse.Namespace:
    """parse command line arguments

    Args:
        args (list): command line arguments sys.argv[1:]

    Returns:
        argparse.Namespace: parsed arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0, help="Verbosity (-v, -vv, etc)")
    parser.add_argument('--version', action='version', version="%(prog)s (version {version})".format(version=__version__))

    return parser.parse_args(args)


def main():
    """main function
    """

    # parse args
    parsed_args = parse_args(sys.argv[1:])

    key_length = 14
    secret_length = 30

    if parsed_args.verbose > 0:
        print('Generating key and secret')
    key, secret = compute_keys(key_length, secret_length)

    print(F'Key: {key}')
    print(F'Secret: {secret}')


if __name__ == "__main__":
    main()
