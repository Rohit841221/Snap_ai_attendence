# import cv2
# import dlib
# import face_recognition
# import streamlit
# import supabase

# print("OpenCV:", cv2.__version__)
# print("Dlib: Working")
# print("Face Recognition: Working")
# print("Streamlit: Working")
# print("Supabase: Working")


import cv2

# Open MacBook camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not detected!")
    exit()

print("Camera started successfully!")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame")
        break

    cv2.imshow("Face Recognition Attendance", frame)

    # Press q to close camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()