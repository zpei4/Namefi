import cv2
from pathlib import Path

# Load pre-trained YOLOv3 model
net = cv2.dnn.readNet('yolov3-custom_last.weights', 'yolov3-custom.cfg')

# Get the output layer names from YOLO
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

def detect_billboard(image_path):
    
    # Load input image
    image = cv2.imread(image_path)
    height, width, channel = image.shape

    # Prepare the image for YOLOv3 by converting it into a blob
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # Perform forward pass to get the YOLO predictions
    outs = net.forward(output_layers)

    # Initialize lists to hold detection data
    confidences = []
    boxes = []

    # Process the output from YOLO
    for out in outs:
        for detection in out:
            confidence = detection[5]  # YOLO returns confidence directly for single-class models
            
            # Only consider detections with high confidence
            if confidence > 0.7:  
                # Scale the bounding box back to the size of the image
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                # Calculate the coordinates for the bounding box
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))

    # Apply non-maxima suppression to reduce overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    detected_billboards = []
    
    # Extract all detected billboard coordinates
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            detected_billboards.append((x, y, w, h))
    
    # Return the list of all detected billboards
    return detected_billboards if detected_billboards else None