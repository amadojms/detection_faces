import cv2
#https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


class VideoCamera(object):

    def __init__(self):
        # self.video = cv2.VideoCapture('http://192.168.2.214:8080/video')
        self.video = cv2.VideoCapture('yo.mp4')
        self.frame_counter = 0
        # self.video = cv2.VideoCapture('rtsp://192.168.2.214:8080/h264_aac.sdp')
        # self.video = cv2.VideoCapture('rtsp://192.168.2.214:8080/h264_pcm.sdp')
        
        

    def __del__(self):
        self.video.release()

    def get_frame(self):
        self.frame_counter += 1
        if self.frame_counter == self.video.get(cv2.CAP_PROP_FRAME_COUNT):
            self.frame_counter = 0 #Or whatever as long as it is the same as next line
            self.video = cv2.VideoCapture('yo.mp4')
            # self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)

        ret, frame = self.video.read()
        # frame_counter += 1
        

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for(x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
            break

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
    