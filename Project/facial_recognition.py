import face_recognition
import cv2
import pickle
import numpy as np

class FacialRecognition:
    def __init__(self, camera_frame):
        self.known_face_encodings = []
        self.known_face_names = []
        self.known_face_images = {}  # Store registered images for comparison
        self.camera_frame = camera_frame
        self.load_registered_faces()

    def load_registered_faces(self):
        try:
            with open("registered_faces.pkl", "rb") as file:
                data = pickle.load(file)
                self.known_face_encodings = data["encodings"]
                self.known_face_names = data["names"]
                self.known_face_images = data["images"]  # Load stored images
        except FileNotFoundError:
            pass

    def save_registered_faces(self):
        data = {"encodings": self.known_face_encodings, "names": self.known_face_names, "images": self.known_face_images}
        with open("registered_faces.pkl", "wb") as file:
            pickle.dump(data, file)

    def draw_contours(self, frame, face_location):
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    def register_face(self, name):
        video_capture = cv2.VideoCapture(0)
        registered = False

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            rgb_frame = frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_frame)

            for face_location in face_locations:
                self.draw_contours(frame, face_location)
                face_encodings = face_recognition.face_encodings(rgb_frame, [face_location])
                
                if face_encodings:
                    # Save encoding, name, and image for later
                    self.known_face_encodings.append(face_encodings[0])
                    self.known_face_names.append(name)
                    self.known_face_images[name] = frame  # Save the registration image
                    self.save_registered_faces()
                    registered = True
                    break

            cv2.imshow("Register Face", frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or registered:
                break

        video_capture.release()
        cv2.destroyAllWindows()
        return registered

    def login(self, name):
        if name not in self.known_face_names:
            return 0

        video_capture = cv2.VideoCapture(0)
        match_percentage = 0
        login_frame = None

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            rgb_frame = frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_frame)

            for face_location in face_locations:
                self.draw_contours(frame, face_location)
                face_encodings = face_recognition.face_encodings(rgb_frame, [face_location])

                if face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encodings[0])
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encodings[0])

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index] and self.known_face_names[best_match_index] == name:
                        match_percentage = (1 - face_distances[best_match_index]) * 100
                        login_frame = frame  # Save the login image for display
                        break

            cv2.imshow("Login", frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or match_percentage > 0:
                break

        video_capture.release()
        cv2.destroyAllWindows()
        
        # Display registered and login images side-by-side if login attempt was made
        if login_frame is not None and name in self.known_face_images:
            self.display_comparison(self.known_face_images[name], login_frame, match_percentage)

        return match_percentage

    def display_comparison(self, registered_image, login_image, match_percentage):
        # Resize images to fit in the comparison window
        registered_image = cv2.resize(registered_image, (300, 300))
        login_image = cv2.resize(login_image, (300, 300))

        comparison_frame = np.hstack((registered_image, login_image))
        cv2.putText(comparison_frame, f"Match: {match_percentage:.2f}%", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if match_percentage >= 50 else (0, 0, 255), 2)

        # Show the side-by-side comparison
        cv2.imshow("Registered vs. Login Comparison", comparison_frame)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
