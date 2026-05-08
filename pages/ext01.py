import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

import yolo_module

yolo_module.load_model()


class VideoProcessor(VideoTransformerBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")
        res = yolo_module.inference(img)
        yolo_module.draw_boxes(img, res)

        return av.VideoFrame.from_ndarray(img, format='bgr24')

webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": False},
    # async_processing=False
)