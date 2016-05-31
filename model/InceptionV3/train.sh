#!/bin/bash

CAFFE_HOME=/home/ubuntu/caffe
PLANTVILLAGE_PATH=/home/ubuntu/PlantVillage/plantvillage
LMDB_PATH=$PLANTVILLAGE_PATH/lmdb
MODEL_PATH=$PLANTVILLAGE_PATH/model/InceptionV3

cd $PLANTVILLAGE_PATH

$CAFFE_HOME/build/tools/caffe train -solver $MODEL_PATH/solver.prototxt