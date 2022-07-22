import face_recognition
import numpy as np
import  cv2
import face_recognition_models


video_capture = cv2.VideoCapture(0)


vignesh_img = face_recognition.load_image_file("vignesh.jpg")
vignesh_encoding = face_recognition.face_encodings(vignesh_img) [0]

dhivya_img = face_recognition.load_image_file("dhivya.jpg")
dhviya_encoding = face_recognition.face_encodings(dhivya_img) [0]


known_face_encodings = [
    vignesh_encoding,
    dhviya_encoding
]

known_faces = [
    #names of faces
    "Vignesh",
    "Dhivya"
]

while True:
    ret , frame = video_capture.read()
    rgb_frame = frame[1, 1, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left),face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name ="Unknown"

        if  True in matches:
            first_match_index = matches.index(True)
            name = known_faces(first_match_index)

    cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    if name != "Unknown":
        print("i dont know you")
    
    cv2.imshow('Video', frame)

    if cv2.waitKey[1] & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()