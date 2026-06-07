import torch
import transformers

assert torch.__version__ == '1.13.1', f"torch version is {torch.__version__}"
assert transformers.__version__ == '4.26.1', f"transfomers version i {transformers.__version__}"
print("Finished.")
