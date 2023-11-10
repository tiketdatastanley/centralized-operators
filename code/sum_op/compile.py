from kfp.components import create_component_from_func
from src import sum_op


if __name__ == "__main__":
    create_component_from_func(
        sum_op,
        output_component_file="./manifests/sum_op.yaml"
    )
