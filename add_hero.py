import argparse
from interaction import add_hero


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="hero name")
    parser.add_argument("--side", help="hero side (Шиноби/Акацуки)")
    parser.add_argument("--birthday", help="hero birthday yyyy-mm-dd")
    args = parser.parse_args()

    add_hero(name=args.name, side=args.side, birthday=args.birthday)