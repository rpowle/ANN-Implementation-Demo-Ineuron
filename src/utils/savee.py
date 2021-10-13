import os
import time

def unique_model(filename):
    unique_filename = time.strftime(f"%Y-%m-%d_%H%M%S_{filename}")
    return unique_filename



def save_model(model,model_name,model_dir):
    unique_filename = unique_model(model_name)
    path_to_model = os.path.join(model_dir, unique_filename)
    model.save(path_to_model)

