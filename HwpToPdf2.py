import os
from tkinter import Tk, filedialog
from reportlab.pdfgen import canvas
import pyhwp  # pyhwp 사용

def save_as_pdf(text, output_path):
    """PDF로 텍스트 저장하는 함수"""
    c = canvas.Canvas(output_path)
    text_object = c.beginText(100, 750)
    text_object.setFont("Helvetica", 12)
    lines = text.split("\n")
    
    for line in lines:
        text_object.textLine(line)
    
    c.drawText(text_object)
    c.save()

def parse_hwp(file_path):
    """HWP 파일을 파싱하여 텍스트를 반환하는 함수"""
    with open(file_path, 'rb') as f:
        document = pyhwp.HWPDocument(f)
        text = ''
        for para in document.bodytext:
            text += para.text + "\n"
        return text

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

            # HWP 파일 파싱
            try:
                parsed_text = parse_hwp(input_file_path)
                if parsed_text.strip():  # 텍스트가 비어있지 않으면
                    save_as_pdf(parsed_text, output_file_path)
                    print(f"{filename} 변환 성공!")
                else:
                    print(f"{filename} 파싱된 텍스트가 없습니다.")
            except Exception as e:
                print(f"{filename} 파싱 실패: {e}")

    print("모든 변환 완료!")

if __name__ == "__main__":
    main()
