import model_zoo
import tensorflow as tf

experiment_name = 'unet_bn_mergeddata'

batch_size = 10
learning_rate = 0.01
data_file = 'wenjia_acdc_merged.hdf5'
model_handle = model_zoo.unet_bn
optimizer_handle = tf.train.AdamOptimizer

schedule_lr = False
warmup_training = True
weight_decay = 0.00000
momentum = None
loss_type = 'weighted_crossentropy'  # crossentropy/weighted_crossentropy/dice

# Augmentation settings
augment_batch = False
do_rotations = True
do_scaleaug = False

# Rarely used settings
use_data_fraction = False  # Should normally be False