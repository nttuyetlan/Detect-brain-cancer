# Install the ultralytics package from GitHub
!pip install git+https://github.com/ultralytics/ultralytics.git@main

import ultralytics
from ultralytics import YOLO
import wandb

## File data.yaml
text = """
path: /kaggle/working/brain_tumor_object_detection

train:
  - axial/train
  - coronal/train
  - sagittal/train
val:
  - axial/val
  - coronal/val
  - sagittal/val

# Classes
nc: 6
names:
  0: 'axial_negative'
  1: 'axial_positive'
  2: 'coronal_negative'
  3: 'coronal_positive'
  4: 'sagittal_negative'
  5: 'sagittal_positive'
"""
with open("/kaggle/working/brain_tumor_object_detection/data.yaml", 'w') as file:
    file.write(text)

# Build a YOLOv9c model from pretrained weight
model = YOLO("yolov9c.pt")

# Display model information (optional)
model.info()

# Train the model on the data.yaml example dataset for 300 epochs
results = model.train(
    data="/kaggle/working/brain_tumor_object_detection/data.yaml",
    epochs=300,
    batch=32,
    imgsz=640,
    device=[0,1],
    plots=True,
    project="Trained_model_YOLOv9"
)
