import sys
sys.path.insert(0, '../src')
from utils.common import read_config
import argparse
from utils.data_management import get_data


def training(config_path):
    config = read_config(config_path)

    validation_datasize = config["params"]["validation_datasize"]
    (x_train, y_train), (x_valid, y_valid), (x_test, y_test) = get_data(validation_datasize)
    

if __name__== '__main__':
    args=argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config.yaml")

    parsed_args = args.parse_args()


    
    training(config_path = parsed_args.config)
