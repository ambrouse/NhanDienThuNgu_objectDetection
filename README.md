## XÂY DỰNG ỨNG DỤNG MẠNG XÃ HỘI BẰNG THƯ VIỆN FLUTTER
<img src="assets_readme/mau.png" alt="!!err image loading." width="700"/>

## Thành viên thực hiện 
- Nguyễn Lê Quốc Bảo - tham gia đóng góp 50% (bản thân)(code và cài đặc web, code lấy data, đóng góp trong báo cáo).
- Phương - tham gia đóng góp 50%.(cấu hình và train mô hình, viết báo cáo, lấy data)

## Lời mở đầu 
- Trong bối cảnh xã hội ngày nay, việc giao tiếp với người khiếm thính trở thành một yếu tố quan trọng để hòa nhập cộng đồng và đảm bảo sự bình đẳng trong việc tiếp cận thông tin. Thủ ngữ, hay ngôn ngữ ký hiệu, là phương thức giao tiếp chính của người khiếm thính, và việc nhận diện thủ ngữ tự động đang ngày càng trở thành một công nghệ hữu ích và cần thiết.
- Dự án "Nhận diện thủ ngữ với YOLO v8" ra đời với mục tiêu phát triển một hệ thống nhận diện thủ ngữ chính xác và hiệu quả, ứng dụng công nghệ học sâu, đặc biệt là mô hình YOLO v8 (You Only Look Once), để nhận diện và phân loại các cử chỉ thủ ngữ trong thời gian thực. YOLO v8, với khả năng nhận diện đối tượng nhanh chóng và hiệu quả, sẽ giúp tối ưu hóa quá trình phát triển hệ thống nhận diện thủ ngữ, từ đó hỗ trợ người khiếm thính giao tiếp dễ dàng hơn.
- Thông qua việc áp dụng mô hình YOLO v8, dự án không chỉ giúp nâng cao khả năng giao tiếp mà còn mở ra cơ hội cải thiện các hệ thống trợ giúp cho người khiếm thính trong nhiều lĩnh vực khác nhau như giáo dục, y tế và dịch vụ công cộng. Dự án kỳ vọng sẽ đóng góp vào việc giảm bớt những rào cản giao tiếp và tạo ra một xã hội hòa nhập hơn cho tất cả mọi người.

## Mô hình sử dụng 
- YOLO v8 (You Only Look Once version 8) là một trong những phiên bản mới nhất trong dòng mô hình YOLO, được thiết kế để nhận diện và phân loại đối tượng trong ảnh hoặc video với tốc độ nhanh và độ chính xác cao. Được phát triển bởi Ultralytics, YOLO v8 không chỉ nâng cao hiệu suất mà còn tích hợp nhiều tính năng tiên tiến giúp tối ưu hóa quá trình nhận diện đối tượng, đặc biệt trong các ứng dụng yêu cầu tốc độ xử lý nhanh và độ chính xác cao.

## Cơ sở về yoloV8
- Kiến trúc mạng: YOLO v8 tiếp tục phát huy thế mạnh của các phiên bản trước đó với một kiến trúc mạng nơ-ron sâu (Deep Neural Network - DNN) tối ưu. Mô hình này sử dụng các mạng CNN (Convolutional Neural Networks) để trích xuất đặc trưng từ hình ảnh và sau đó phân loại các đối tượng trong ảnh. YOLO v8 cải thiện đáng kể khả năng nhận diện các đối tượng có kích thước nhỏ và lớn trong một cảnh.
- Tốc độ và độ chính xác: YOLO v8 tiếp tục duy trì ưu thế về tốc độ xử lý nhanh, giúp nhận diện đối tượng trong thời gian thực. Điều này làm cho YOLO v8 rất phù hợp với các ứng dụng yêu cầu xử lý hình ảnh trực tiếp như giám sát video, lái xe tự động, và nhận diện thủ ngữ trong thời gian thực. Mô hình cải tiến độ chính xác và giảm thiểu số lượng sai sót trong các trường hợp nhận diện đối tượng.
- Kỹ thuật cải tiến: YOLO v8 sử dụng nhiều kỹ thuật cải tiến so với các phiên bản trước đó, bao gồm:
- Sử dụng transformer: Cải thiện khả năng nhận diện trong các cảnh phức tạp, có sự tương tác giữa các đối tượng.
Cải tiến trong học sâu (Deep Learning): Tăng cường khả năng học đặc trưng từ dữ liệu và giảm thiểu sai số trong quá trình huấn luyện.
Kỹ thuật augmentation dữ liệu: Giúp mô hình hoạt động tốt hơn khi có ít dữ liệu hoặc trong những điều kiện môi trường thay đổi.

### Ứng dụng thực tiễn: YOLO v8 có thể được ứng dụng rộng rãi trong nhiều lĩnh vực, bao gồm:
- Nhận diện đối tượng trong video và hình ảnh: Giám sát an ninh, phân tích hành vi, giao thông thông minh.
Nhận diện thủ ngữ: Trong các dự án nhận diện ngôn ngữ ký hiệu, YOLO v8 có thể nhận diện các cử chỉ và động tác tay của người sử dụng thủ ngữ.
- Y tế: Chẩn đoán hình ảnh, nhận diện các bất thường trong các xét nghiệm hình ảnh.
- Môi trường triển khai: YOLO v8 có thể được triển khai trên nhiều nền tảng khác nhau, từ máy tính cá nhân đến các thiết bị di động, với yêu cầu về phần cứng không quá cao nhưng vẫn đảm bảo hiệu suất cao. Việc triển khai YOLO v8 có thể thực hiện dễ dàng nhờ vào việc sử dụng các thư viện mã nguồn mở như PyTorch và TensorFlow.

### Ưu điểm của YOLO v8:
- Nhanh chóng và chính xác: Phù hợp với các ứng dụng yêu cầu xử lý thời gian thực.
- Dễ dàng triển khai: Được hỗ trợ bởi cộng đồng mã nguồn mở lớn, YOLO v8 dễ dàng tích hợp vào các hệ thống hiện tại.
- Khả năng mở rộng: Mô hình có thể dễ dàng mở rộng và điều chỉnh cho các ứng dụng cụ thể như nhận diện thủ ngữ.


## Các công cụ sử dụng trong dự án
- Google-colab hỗ trợ trong quá trình training
- Vscode trong quá trình code lấy data, lấy data, và code web

## Ảnh demo cho dữ liệu trainning

## Thông số các hàm loss, acc và một vài độ đo khác

## Video Demo cho dự án
[![Watch video](https://img.youtube.com/vi/vBhYvOIoWmc/0.jpg)](https://www.youtube.com/watch?v=vBhYvOIoWmc&autoplay=1)

## Tài liệu
<!-- [Báo cáo chi tiết dự án](report/chat_app_chuyen_de_chuyen_sau_1_nguyen_le_quoc_bao_2100004053.docx) -->

