'''
################ ByteTrack ##########################
python tools/demo_track.py -f exps/example/mot/yolox_x_mix_mot20_ch.py -c pretrained/bytetrack_x_mot20.tar --fuse --save_result --path train_part7/07_University_Campus --conf 0.25 --nms 0.45 --tsize 5120
#####################################################

################ StrongSort #########################
python track_v7.py --yolo-weights weights/yolov7-e6e.pt --source train_part7/07_University_Campus --img-size 5120 --classes 0 --save-txt --save-img

################ DeepSort ###########################
python deep_track_v7.py --yolo-weights weights/yolov7-e6e.pt --source train_part7/07_University_Campus --img-size 5120 --classes 0 --save-txt --save-img
#####################################################
'''
