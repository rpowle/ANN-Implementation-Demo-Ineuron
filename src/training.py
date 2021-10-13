import sys
sys.path.insert(0, '../src')
from utils.common import read_config
import argparse
from utils.data_management import get_data
#from utils.model import create_model, save_model
from utils.model import create_model
from utils.savee import save_model
import os


def training(config_path):
    config = read_config(config_path)

    validation_datasize = config["params"]["validation_datasize"]
    (x_train, y_train), (x_valid, y_valid), (x_test, y_test) = get_data(validation_datasize)

    LOSS_FUNCTION = config['params']["LOSS_FUNCTION"]
    OPTIMIZER = config['params']["OPTIMIZER"]
    METRICS = config['params']["METRICS"]
    no_classes = config['params']["no_classes"]
    model = create_model(LOSS_FUNCTION,OPTIMIZER,METRICS,no_classes)

    EPOCHS = config["params"]["epochs"]
    VALIDATION = (x_valid, y_valid)
    history = model.fit(x_train, y_train, epochs=EPOCHS, validation_data=VALIDATION)


    artifacts_dir = config["artifacts"]["artifacts_dir"]
    model_name = config["artifacts"]["model_name"]

    model_dir = config["artifacts"]["model_dir"]

    model_dir_path = os.path.join(artifacts_dir, model_dir)
    os.makedirs(model_dir_path, exist_ok=True)

    save_model(model, model_name, model_dir_path)


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config.yaml")

    parsed_args = args.parse_args()
    training(config_path=parsed_args.config)
