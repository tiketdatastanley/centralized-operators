import argparse

from kfp.components import create_component_from_func
from src import sum_op


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    args = parser.parse_args()

    create_component_from_func(sum_op, output_component_file=args.path)
