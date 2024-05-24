import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTextEdit
import pathlib
import textwrap
import PIL.Image
import google.generativeai as genai

global keyword_input
global style_input
global story_output
global model

def generate_story():
    global model
    keywords = keyword_input.text()
    style = style_input.currentText()
    prompt = f"다음 조건을 지켜 7문장 정도의 재미있는 이야기를 지어주세요. 포함할 키워드: {keywords}, 이야기의 문체: {style}"

    # 안전성 설정
    

    # 스트리밍 응답
    response = model.generate_content(prompt, stream=False)
    response.resolve()  # 스트리밍 응답에서 필요

    story_output.setText(response.text)

def main():
    global model
    app = QApplication(sys.argv)

    # API 키 설정
    GOOGLE_API_KEY = 'AIzaSyCRBCw0iO3unukOMAlevmSXxlsQ5ClMn94'
    genai.configure(api_key=GOOGLE_API_KEY)

    # 모델 선택 (텍스트 전용 또는 이미지+텍스트)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')  # 텍스트 전용
    # model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')  # 이미지+텍스트

    window = QWidget()
    window.setWindowTitle("잼얘 생성기")

    layout = QVBoxLayout()

    keyword_label = QLabel("키워드:")
    layout.addWidget(keyword_label)

    global keyword_input
    keyword_input = QLineEdit()
    layout.addWidget(keyword_input)

    style_label = QLabel("문체:")
    layout.addWidget(style_label)

    global style_input
    style_input = QComboBox()
    style_input.addItems(["유머러스", "서정적", "모험심", "판타지", "미스터리", "공포", "로맨스", "SF", "역사"])
    layout.addWidget(style_input)

    generate_button = QPushButton("이야기 생성")
    generate_button.clicked.connect(generate_story)
    layout.addWidget(generate_button)

    global story_output
    story_output = QTextEdit()
    story_output.setReadOnly(True)
    layout.addWidget(story_output)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
