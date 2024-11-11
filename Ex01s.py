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
            shutil.move(file_path, os.path.join(target_folder, file))

print("파일 재분류가 완료되었습니다.")







# 이 Python 파일이 있는 폴더를 기준 폴더로 설정 & 실행 



# 1. 명령 프롬프트/터미널 열기:

# Windows: Win + R → cmd 입력 → Enter.
# Mac/Linux: Cmd + Space → Terminal 입력 → Enter.

# 2. 코드가 있는 디렉터리로 이동: cd 명령어를 사용하여 Ex01s.py 파일이 있는 폴더로 이동

# Ex)
# cd C:\Users\username\Documents  # Windows
# cd /Users/username/Documents    # Mac/Linux

# 3. 명령 프롬프트나 터미널에 다음과 같이 입력 후 Enter
# C:\Users\username\Documents> python Ex01s.py
