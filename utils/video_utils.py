import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()# ret is return type
        if not ret:#when video will end 
            break
        frames.append(frame)
    return frames

# frames[0] → first frame
# .shape → gives image size
# Example shape:
# (720, 1280, 3)
# means
# height = 720
# width = 1280
# channels = 3
# So
# shape[0] = height
# Codec
# Codec = Coder + Decoder---A codec is used to compress and decompress video data so the video file size becomes smaller.
# In the code:
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# XVID is the codec used to compress the video when saving it.
# So this line means:
# Save the video using the XVID compression method.
def save_video(frames, path):

    height = frames[0].shape[0]
    width = frames[0].shape[1]

    fourcc = cv2.VideoWriter_fourcc(*'XVID')#video format

    video = cv2.VideoWriter(path, fourcc, 24, (width, height))

    for frame in frames:
        video.write(frame)

    video.release()