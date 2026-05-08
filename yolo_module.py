import numpy as np
import cv2
import onnxruntime

session = None

def iou(box, BOX):
    x1, y1, x2, y2 = box[:4]
    X1, Y1, X2, Y2 = BOX[:4]
    ix1 = max(x1, X1)
    ix2 = min(x2, X2)
    iy1 = max(y1, Y1)
    iy2 = min(y2, Y2)
    iw = ix2 - ix1
    ih = iy2 - iy1
    if iw < 0 or ih < 0:
        return 0
    inter = iw * ih

    area = (x2 - x1) * (y2 - y1)
    AREA = (X2 - X1) * (Y2 - Y1)
    union = area + AREA - inter
    return inter / union

def load_model(path='yolo11n_640.onnx'):
    global session
    session = onnxruntime.InferenceSession(path)

def inference(image): #HWC, BGR
    global session
    dst = np.full((640, 640, 3), 128, np.uint8)
    H, W, _ = image.shape
    if H > W:
        h = 640
        w = W * 640 / H
        y = 0
        x = (640 - w) / 2
    else:
        w = 640
        h = H * 640 / W
        x = 0
        y = (640 - h) / 2

    resized = cv2.resize(image, (int(w), int(h)))

    x1 = int(x)
    y1 = int(y)
    x2 = x1 + int(w)
    y2 = y1 + int(h)

    pad_x = x1
    pad_y = y1

    dst[y1:y2, x1:x2] = resized

    #dst = cv2.resize(image, (640, 640))[..., ::-1]
    dst = dst[..., ::-1]

    input = (dst / 255).astype(np.float32).transpose(2, 0, 1)[None]

    # compute ONNX Runtime output prediction
    ort_inputs = {'images': input}
    outputs = session.run(None, ort_inputs) # type: ignore
    res = outputs[0][0].transpose() # type: ignore #8400, 6

    max_prob = res[:, 4:].max(axis=1) # 8400,
    max_cat = res[:, 4:].argmax(axis=1) # 8400,
    index = max_prob > 0.2
    filtered = res[index]

    cx = filtered[:, 0]
    cy = filtered[:, 1]
    w2 = filtered[:, 2] / 2
    h2 = filtered[:, 3] / 2

    x1 = cx - w2
    y1 = cy - h2
    x2 = cx + w2
    y2 = cy + h2

    # conf = filtered[:, 4:].max(axis=1)
    # cat = filtered[:, 4:].argmax(axis=1)
    conf = max_prob[index]
    cat = max_cat[index]

    boxes = np.stack([x1, y1, x2, y2, conf, cat], axis=1)

    #NMS - Non Maximum Superssion
    # np.sort(boxes, axis=0, )
    boxes = sorted(boxes, key=lambda x:x[4], reverse=True)



    H, W, C = image.shape
    rate = min(640 / H, 640 / W)

    results = []
    for box in boxes:
        for r in results:
            if iou(box, r) > 0.5:
                break
        else:
            results.append(box)
        #box와 results에 있는 모든 원소와 비교
        #겹치는 게 없으면 results에 추가
    if len(results) == 0:
        return np.zeros((0, 6))
    results = np.array(results)
    results[:, :4] = (results[:, :4] - [pad_x, pad_y, pad_x, pad_y]) / rate
    return results

def draw_boxes(image, res):
    for X1, Y1, X2, Y2, conf, cat in res:
        bx1 = int(X1)
        by1 = int(Y1)
        bx2 = int(X2)
        by2 = int(Y2)
        if cat == 0:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)
        cv2.rectangle(image, (bx1, by1), (bx2, by2), color, 3)

if __name__ == '__main__':
    image = cv2.imread('girls.jpg')
    # image = cv2.resize(image, None, fx=0.2, fy=0.2)
    load_model('yolo11n_640.onnx')
    res = inference(image)
    draw_boxes(image, res)
    print(res)
    cv2.imshow('result', image)
    cv2.waitKey(0)