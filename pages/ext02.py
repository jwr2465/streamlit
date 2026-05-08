import streamlit as st
from PIL import Image

st.title("📸 이미지 입력 테스트")

# 1. 입력 방식 선택
option = st.radio("이미지를 어떻게 불러올까요?", ["카메라로 찍기", "파일 업로드"])

image = None

# 2. 버튼 눌러서 카메라 or 파일 입력 받기
if option == "카메라로 찍기":
    camera_file = st.camera_input("카메라로 사진 찍기")
    if camera_file:
        image = Image.open(camera_file)

elif option == "파일 업로드":
    uploaded_file = st.file_uploader("이미지 파일 선택", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)

# 3. 이미지 처리 및 결과 표시
if image:
    st.image(image, caption="입력된 이미지", use_column_width=True)
    # 여기에 추가 처리 (예: YOLO 등) 삽입 가능