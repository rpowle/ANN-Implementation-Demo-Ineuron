import tensorflow as tf
import os
import numpy as np
import time


def get_timestamp(name):
    timestame = time.asctime().replace(" ","_").replace(":", "_")
    unique_name= f"{name}_at_{timestame}"
    return unique_name


def get_callbacks(config,x_train):
    logs = config["logs"]
    unique_dir_name= get_timestamp("tb_logs")
    TENSORBOARD_LOG_DIR= os.path.join(logs["logs_dir"], logs["TENSORBOARD_ROOT_LOG_DIR"], unique_dir_name)

    os.makedirs(TENSORBOARD_LOG_DIR, exist_ok=True)
    tensorboard_cb= tf.keras.callbacks.TensorBoard(log_dir=TENSORBOARD_LOG_DIR)


    filewriter= tf.summary.create_file_writer(logdir=TENSORBOARD_LOG_DIR)
    with filewriter.as_default():
        images = np.reshape(x_train[10:30],(-1,28,28,1))
        tf.summary.image("20 handwritten samples", images,max_outputs=25,step=0)

        params = config["params"]

        early_stopping = tf.keras.callbacks.EarlyStopping (patience = params["patience"], 
        restore_best_weights = params["restore_best_weights"])


        artifacts = config["artifacts"]
        ckpt_dir= os.path.join(artifacts["artifacts_dir"], artifacts["CHECKPOINTS_DIR"])
        os.makedirs(ckpt_dir, exist_ok=True)


        ckpt_path = os.path.join(ckpt_dir, "model_ckpt.h5")
        checkpointing_cb= tf.keras.callbacks.ModelCheckpoint(ckpt_path, save_best_only= True)

        return [tensorboard_cb,early_stopping,checkpointing_cb  ]