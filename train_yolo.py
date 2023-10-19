from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('yolov8n.pt')
    results = model.train(data='infant1.yaml', epochs=7, imgsz=640)
