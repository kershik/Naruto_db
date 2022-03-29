import argparse
from interaction import add_story


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="hero name")
    parser.add_argument("--story", help="hero story")
    args = parser.parse_args()

    add_story(name=args.name, story=args.story)