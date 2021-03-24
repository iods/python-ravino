import argparse


def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--developer', help='The Builder.')
    parser.add_argument('--devops', help='The Architect.')

    return parser.parse_args()


def main():
    args = arguments()

    print(args)


if __name__ == '__main__':
    main()
