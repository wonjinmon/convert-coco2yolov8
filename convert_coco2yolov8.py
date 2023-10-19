from converter import convert_coco  # ultralytics.data.converter 파일 수정

if __name__ == '__main__':
    convert_coco(labels_dir='./coco_data/', save_dir='./yolo_data/')
