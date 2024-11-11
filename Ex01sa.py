import os
import shutil

# 이 Python 파일이 있는 폴더를 기준 폴더로 설정
base_folder = os.path.dirname(os.path.abspath(__file__))

# 폴더 내 모든 파일 탐색
for root, dirs, files in os.walk(base_folder):
    for file in files:
        # 현재 파일(ex01.py) 제외
        if file == os.path.basename(__file__):
            continue
        
        file_path = os.path.join(root, file)
        # 파일의 확장자 확인
        file_extension = os.path.splitext(file)[1].lower().strip('.')

        if file_extension:  # 확장자가 있는 경우
            # 재분류할 폴더 이름 설정 (예: 1_jpg, 1_png 등)
            target_folder = os.path.join(base_folder, f"1_{file_extension}")
            
            # 폴더가 없다면 생성
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # 파일을 새로운 폴더로 이동
            new_file_path = os.path.join(target_folder, file)
            
            # 파일 이름 충돌 처리 (중복 파일 방지)
            if os.path.exists(new_file_path):
                base_name, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(new_file_path):
                    new_file_path = os.path.join(target_folder, f"{base_name}_{counter}{ext}")
                    counter += 1

            # 파일 이동
            shutil.move(file_path, new_file_path)

print("파일 재분류가 완료되었습니다.")
