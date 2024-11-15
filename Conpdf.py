from reportlab.pdfgen import canvas

def save_as_pdf(text, output_path):
    c = canvas.Canvas(output_path)
    c.drawString(100, 750, text)
    c.save()

# 변환 예시
parsed_text = "추출된 HWP 텍스트 예시"
save_as_pdf(parsed_text, "output.pdf")
