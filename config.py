import argparse


parser = argparse.ArgumentParser(
    description="Python Network Scanner"
)

parser.add_argument(
    "--target",
    default="scanme.nmap.org",
    help="Target host or IP"
)

parser.add_argument(
    "--start",
    type=int,
    default=20,
    help="Starting port"
)

parser.add_argument(
    "--end",
    type=int,
    default=100,
    help="Ending port"
)


args = parser.parse_args()


TARGET = args.target
START_PORT = args.start
END_PORT = args.end