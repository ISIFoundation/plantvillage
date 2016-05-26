#!/bin/bash

CAFFE_HOME="/home/ubuntu/caffe"
LMDB_PATH="/home/ubuntu/PlantVillage/plantvillage/lmdb"

# python create_distribution.py 

$CAFFE_HOME/build/tools/convert_imageset \
   --resize_height 256 \
   --resize_width 256 \
   --shuffle \
   / \
   $LMDB_PATH/train.txt \
   $LMDB_PATH/train_lmdb

$CAFFE_HOME/build/tools/convert_imageset \
    --resize_height 256 \
    --resize_width 256 \
    --shuffle \
    / \
    $LMDB_PATH/val.txt \
    $LMDB_PATH/val_lmdb

$CAFFE_HOME/build/tools/compute_image_mean lmdb/train_lmdb lmdb/mean.binaryproto
