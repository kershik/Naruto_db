import argparse
from interaction import delete_hero


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="hero name")
    args = parser.parse_args()

    delete_hero(name=args.name)