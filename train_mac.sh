#!/bin/bash
LOG=log/train-`date +%Y-%m-%d-%H-%M-%S`.log
./build/tools/caffe train --solver models/mac/mobilenet_yolov3_lite_solver.prototxt --weights models/mac/mobilenet_iter_73000.caffemodel 2>&1 | tee $LOG
#--weights models/MobileNet/mobilenet_yolov3_lite_coco.caffemodel
#--snapshot models/yolov3/mobilenet_yolo_deploy_iter_1000.solverstate
