# Brain Tumor Detection and Classification
## Brief overview
- Phát hiện và phân loại khối u chính xác là yếu tố quan trọng giúp bác sĩ đưa ra quyết định điều trị đúng đắn nhưng việc phân tích hình ảnh y khoa (X-quang, MRI, CT) là công việc mất nhiều thời gian và đòi hỏi chuyên môn cao.
- Các mô hình học sâu có khả năng xử lý khối lượng dữ liệu lớn giúp tiết kiệm thời gian và loại bỏ những trường hợp khối u dễ nhận diện.
## Dataset
- [Brain tumor object detection datasets](https://www.kaggle.com/datasets/davidbroberts/brain-tumor-object-detection-datasets) này được xây dựng nhằm phục vụ việc huấn luyện và đánh giá các mô hình phát hiện khối u não trên ảnh cộng hưởng từ (MRI). Dữ liệu bao gồm các ảnh JPG ở độ phân giải gốc, được phân loại theo các mặt phẳng chụp (Axial, Coronal và Sagittal). Các vùng khối u được gán nhãn thủ công bằng công cụ makesense.ai. Tọa độ hộp giới hạn (bounding box) và nhãn MGMT dương tính được đánh dấu trên khoảng 400 ảnh cho mỗi mặt phẳng trong chuỗi ảnh T1wCE, lấy từ bộ dữ liệu của cuộc thi RSNA-MICCAI.
- [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) này kết hợp từ figshare, SARTAJ dataset và Br35H, gồm 7.023 ảnh MRI não người được chia thành bốn lớp: glioma, meningioma, không có khối u và u tuyến yên. Ảnh nhóm “không có khối u” lấy từ Br35H, trong khi ảnh glioma từ SARTAJ bị loại bỏ do lỗi phân loại và được thay thế bằng ảnh từ figshare. Kích thước ảnh không đồng nhất nên cần tiền xử lý để đồng bộ kích thước và loại bỏ viền thừa nhằm nâng cao độ chính xác mô hình.



![image](https://github.com/user-attachments/assets/bf033a99-599f-4740-94b0-8a17422ec865)
