import hwp5

# 파일 열기
with open('example.hwp', 'rb') as hwp_file:
    hwp_document = hwp5.Document(hwp_file)

# 문서 내용 출력
for paragraph in hwp_document.body.text_paragraphs:
    print(paragraph.text)
