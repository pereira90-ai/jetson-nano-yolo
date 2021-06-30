import cv2
import numpy as np
import requests
import argparse
from glob import glob
from elements.yolo import OBJ_DETECTION as Person_Detection

parser = argparse.ArgumentParser()
parser.add_argument('--cam', type = int, default = 1 , help = 'camera number 0 - 910.')
args = parser.parse_args()


Object_classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
                'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
                'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
                'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
                'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
                'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
                'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
                'hair drier', 'toothbrush' ]
                
Person_Detector = Person_Detection('weights/car_model.pt', Object_classes)

################################ image request ##################################################
# url = 'https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/' + '00001.06621' + '.jpg'
# resp = requests.get(url, stream=True).raw
# image = np.asarray(bytearray(resp.read()), dtype="uint8")
# image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#################################################################################################

################################ camera list ##################################################

with open("camera_list.txt", "r") as f:
  cameras = f.read().split()

#################################################################################################

################################ video request ##################################################

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/' + cameras[args.cam] + '.mp4')

while(True):
    ret, frame = cap.read()
    if ret:
        # detection process
        Persons = Person_Detector.detect(frame)

        # plotting
        for Person in Persons:
            print(Person)
            label = Person['label']
            score = Person['score']
            [(xmin,ymin),(xmax,ymax)] = Person['bbox']
            frame = cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), [0,255,255] , 2) 
            frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin,ymin), cv2.FONT_HERSHEY_SIMPLEX , 0.75, [0,255,255], 2, cv2.LINE_AA)
        
        cv2.imshow('image',frame)
        cv2.waitKey(10)
    else:
        break
    
cap.release()
cv2.destroyAllWindows()

#################################################################################################
