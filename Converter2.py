
import os
import pyheif
from PIL import Image

# HEIC 파일이 있는 폴더 경로
folder_path = 'path_to_your_folder'

# 폴더 내 모든 HEIC 파일을 변환
for file_name in os.listdir(folder_path):
    if file_name.lower().endswith('.heic'):
        heic_file_path = os.path.join(folder_path, file_name)
        output_file_path = os.path.join(folder_path, file_name.replace('.heic', '.jpg'))

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

        # 이미지를 JPEG 형식으로 저장
        image.save(output_file_path, "JPEG")
        print(f"{file_name} 변환 완료!")
