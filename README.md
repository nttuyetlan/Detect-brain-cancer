# Brain Tumor Detection and Classification
## Brief overview
- Phát hiện và phân loại khối u chính xác là yếu tố quan trọng giúp bác sĩ đưa ra quyết định điều trị đúng đắn nhưng việc phân tích hình ảnh y khoa (X-quang, MRI, CT) là công việc mất nhiều thời gian và đòi hỏi chuyên môn cao.
- Các mô hình học sâu có khả năng xử lý khối lượng dữ liệu lớn giúp tiết kiệm thời gian và loại bỏ những trường hợp khối u dễ nhận diện.
## Dataset
- [Brain tumor object detection datasets](https://www.kaggle.com/datasets/davidbroberts/brain-tumor-object-detection-datasets) này được xây dựng nhằm phục vụ việc huấn luyện và đánh giá các mô hình phát hiện khối u não trên ảnh cộng hưởng từ (MRI). Dữ liệu bao gồm các ảnh JPG ở độ phân giải gốc, được phân loại theo các mặt phẳng chụp (Axial, Coronal và Sagittal). Các vùng khối u được gán nhãn thủ công bằng công cụ makesense.ai. Tọa độ hộp giới hạn (bounding box) và nhãn MGMT dương tính được đánh dấu trên khoảng 400 ảnh cho mỗi mặt phẳng trong chuỗi ảnh T1wCE, lấy từ bộ dữ liệu của cuộc thi RSNA-MICCAI.
- [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) này kết hợp từ figshare, SARTAJ dataset và Br35H, gồm 7.023 ảnh MRI não người được chia thành bốn lớp: glioma, meningioma, notumor và pituitary. Ảnh nhóm “notumor” lấy từ Br35H, trong khi ảnh glioma từ SARTAJ bị loại bỏ do lỗi phân loại và được thay thế bằng ảnh từ figshare. Kích thước ảnh không đồng nhất nên cần tiền xử lý để đồng bộ kích thước và loại bỏ viền thừa nhằm nâng cao độ chính xác mô hình.
## Poster
![Poster](https://github.com/user-attachments/assets/bf033a99-599f-4740-94b0-8a17422ec865)  
## Data preprocessing  
<img width="720" height="70" alt="image" src="https://github.com/user-attachments/assets/c28e1956-45ad-4e1d-95a1-5c170cfdea67" />  

## Topic ideas  
- Object detection  
<img width="701" height="199" alt="image" src="https://github.com/user-attachments/assets/cb56c05f-64e4-4065-8566-e7bc8180ca90" />

- Classification  
  <img width="578" height="130" alt="image" src="https://github.com/user-attachments/assets/0778ee10-85ef-49cb-a55d-1b6dc60589fb" />
  
## Training the model  
### Object Detection  
THÔNG SỐ TRAIN: YOLOv9c, EPOCHS=300, BATCH=32, IMGSZ=640, DEVICE=[0,1]  
<img width="2400" height="1200" alt="image" src="https://github.com/user-attachments/assets/643e3cb6-c011-4395-a99f-48c3b90ba160" />  

### Classification  
<img width="1243" height="776" alt="image" src="https://github.com/user-attachments/assets/7189b539-a4a8-4740-90d7-beef95f62aca" />  

## Results  

### Object Detection  
<img width="2250" height="1500" alt="image" src="https://github.com/user-attachments/assets/78cb4c28-5827-4983-a003-0205ed72afab" />  
<img width="1920" height="1556" alt="image" src="https://github.com/user-attachments/assets/1871bf4e-2de6-4ccf-b117-31f1e8df4a86" />  

### Classification  
<img width="475" height="190" alt="image" src="https://github.com/user-attachments/assets/76a5f8fc-c6f9-4627-a32c-ae4fe495d5af" />

