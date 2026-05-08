import streamlit as st
from PIL import Image
import yolo_module

yolo_module.load_model()

import json
import os

import numpy as np
import cv2
import datetime

import coco_labels


image = None
def home():
    
    st.title("📸 YOLO HOME")

    uploaded_file = st.file_uploader("이미지 파일 선택", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.session_state.image = image
    else:
        st.session_state.image = None

    # 3. 이미지 처리 및 결과 표시
    if st.session_state.image:
        st.image(st.session_state.image, caption="입력된 이미지", use_container_width=True)
        # 여기에 추가 처리 (예: YOLO 등) 삽입 가능

        but = st.button('결과 확인')
        if but:
            filename_first = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
            image = np.array(st.session_state.image)[..., [2, 1, 0]]
            res = yolo_module.inference(image)

            labels = []
            for cat in res[:, 5]:
                label_txt = coco_labels.labels[int(cat)]
                labels.append(label_txt)

            #write json
            json_path = os.path.join('outputs', filename_first + '.json')
            result = {'rects':res[:, :4].tolist(), 'labels':labels, 'scores':res[:, 4].tolist()}
            json.dump(result, open(json_path, 'w'))
            
            #write image
            #drawing...
            dst = image.copy()
            yolo_module.draw_boxes(dst, res)
            dst_path = os.path.join('outputs', filename_first + '.jpg')
            cv2.imwrite(dst_path, dst)
            return filename_first
    return 'home'