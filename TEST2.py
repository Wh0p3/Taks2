import cv2
input_video = cv2.VideoCapture("input_video.mp4")
width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(input_video.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter("output_video.mp4", fourcc, fps, (width, height), isColor=True)
frame_count = 0
while True:
    ret, frame = input_video.read()
    if not ret:
        break
    if frame_count % 4 == 0:
        
        output_video.write(frame)

    frame_count += 1
input_video.release()
output_video.release()
output_video = cv2.VideoCapture("output_video.mp4")
while True:
    ret, frame = output_video.read()
    if not ret:
        break
    cv2.imshow("Output Video", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
output_video.release()
cv2.destroyAllWindows()
