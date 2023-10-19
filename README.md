# convert coco to yolov8 & train 

### coco dataset format

```
coco_data/
    images/
        17962/
            126524578_1.jpg
            ...
        18027/
            126499894_1.jpg
            ...
        18028/
            ...
        18030/
            ...
        18222/
            ...
    annotations.json
```

### yolo dataset format
```
yolo_data/
    images/
        ...

    labels/
        annotations/
            images/
                17962/
                    126524578_1.txt
                    ...
                18027/
                    ...
                18028/
                    ...
                18030/
                    ...
                18222/
                    ...
```


# 
<br>
가지고 있는 coco data의 형식이 조금 달라 `ultralytics.data.converter`의 내용을 수정하여 `converter.py` 작성 

<br>
convert_coco2yolov8.py >>> train_yolo.py