import onnx

def change_input_dim(model):
    sym_batch_dim = "N"  # Symbolic name for the batch dimension
    actual_batch_dim = 4  # The desired batch size

    inputs = model.graph.input
    for input in inputs:
        input.type.tensor_type.shape.dim[0].dim_param = sym_batch_dim
        input.type.tensor_type.shape.dim[0].dim_value = actual_batch_dim

# Usage example
model = onnx.load("path/to/your/model.onnx")
change_input_dim(model)
