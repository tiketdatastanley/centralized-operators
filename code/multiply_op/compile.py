from kfp.components import create_component_from_func
from src import multiply_op


if __name__ == "__main__":
    create_component_from_func(
        multiply_op,
        output_component_file="./manifests/multiply_op.yaml"
    )
