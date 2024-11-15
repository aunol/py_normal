import os
import pyheif
from PIL import Image

# 원본 HEIC 파일들이 있는 폴더
input_folder = r"D:\일반폴더\BackUp_IPhone\1_heic"
# 변환된 이미지 파일들을 저장할 폴더
output_folder = r"D:\일반폴더\BackUp_IPhone\2_heic"

# output_folder가 존재하지 않으면 새로 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# input_folder 내의 모든 .heic 파일 처리
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith('.heic'):  # HEIC 파일인 경우
            heic_file_path = os.path.join(root, file)
            
            # HEIC 파일 읽기
            heif_file = pyheif.read(heic_file_path)
            
            # HEIC 파일을 Pillow 이미지 객체로 변환
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data, 
                "raw", 
                heif_file.mode, 
                heif_file.stride
            )
            
            # 저장할 파일 경로 (변환된 이미지 파일 경로)
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.jpg")
            
            # 이미지를 JPEG 형식으로 저장
            image.save(output_file_path, "JPEG")
            
            print(f"파일이 {output_file_path}로 저장되었습니다.")
