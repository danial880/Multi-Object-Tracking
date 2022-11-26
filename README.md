# Multi-Object tracking using all variants of deepsort

## Download Models
- Download [Yolov7-E6E](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt) and put it under [weigths folder](https://github.com/danial880/Multi-Object-Tracking/tree/main/StrongSORT/weights)
- Download [bytetrack_x_mot20](https://drive.google.com/file/d/1HX2_JpMOjOIj1Z9rJjoet9XNy_cCAs5U/view?usp=sharing) and put it under [pretrained folder](https://github.com/danial880/Multi-Object-Tracking/tree/main/ByteTrack/pretrained)

## Inference
### DeepSort
```
cd StrongSORT
python deep_track_v7.py --yolo-weights weights/yolov7-e6e.pt --source train_part7/07_University_Campus --img-size 5120 --classes 0 --save-txt --save-img
```
### StronSORT
```
cd StrongSORT
python track_v7.py --yolo-weights weights/yolov7-e6e.pt --source train_part7/07_University_Campus --img-size 5120 --classes 0 --save-txt --save-img
```
### ByteTrack
```
cd ByteTrack
python tools/demo_track.py -f exps/example/mot/yolox_x_mix_mot20_ch.py -c pretrained/bytetrack_x_mot20.tar --fuse --save_result --path train_part7/07_University_Campus --conf 0.25 --nms 0.45 --tsize 5120
```
