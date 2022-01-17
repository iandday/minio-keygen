import sys
import minio_keygen


def main():
    """main function
    """

    # parse args
    parsed_args = minio_keygen.parse_args(sys.argv[1:])

    key_length = 14
    secret_length = 30

    if parsed_args.verbose > 0:
        print('Generating key and secret')
    key, secret = minio_keygen.compute_keys(key_length, secret_length)

    print(F'Key: {key}')
    print(F'Secret: {secret}')


if __name__ == "__main__":
    sys.exit(main())
