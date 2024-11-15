import os
import shutil
from tkinter import Tk, filedialog
import subprocess

def main():
    # Tkinter를 사용해 폴더 선택 창 띄우기
    Tk().withdraw()  # Tkinter 기본 창 숨기기
    input_folder_path = filedialog.askdirectory(title="폴더를 선택하세요")

    if not input_folder_path:
        print("폴더가 선택되지 않았습니다.")
        return

    # 출력 폴더 설정 (선택된 폴더 내에 'converted_pdfs' 폴더 생성)
    output_folder_path = os.path.join(input_folder_path, 'converted_pdfs')
    os.makedirs(output_folder_path, exist_ok=True)

    # 입력 폴더 내의 파일 탐색
    for filename in os.listdir(input_folder_path):
        if filename.lower().endswith('.hwp'):
            input_file_path = os.path.join(input_folder_path, filename)
            file_stem = os.path.splitext(filename)[0]
            output_file_path = os.path.join(output_folder_path, f"{file_stem}.pdf")

            # Conhwp.py 실행 (파싱 단계)
            parse_result = subprocess.run(["python", "Conhwp.py", input_file_path], capture_output=True, text=True)

            if parse_result.returncode != 0:
                print(f"{filename} 파싱 실패: {parse_result.stderr}")
                continue

            # Conpdf.py 실행 (변환 단계)
            convert_result = subprocess.run(["python", "Conpdf.py", input_file_path, output_file_path], capture_output=True, text=True)

            if convert_result.returncode == 0:
                print(f"{filename} 변환 성공!")
            else:
                print(f"{filename} 변환 실패: {convert_result.stderr}")

    print("모든 변환 완료!")

if __name__ == "__main__":
    main()
