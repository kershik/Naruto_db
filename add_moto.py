import argparse
from interaction import add_moto


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="hero name")
    parser.add_argument("--moto", help="hero moto")
    args = parser.parse_args()

    add_moto(name=args.name, moto=args.moto)