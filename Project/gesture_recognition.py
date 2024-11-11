import mediapipe as mp
import cv2
import pickle

class GestureRecognition:
    def __init__(self, camera_frame):
        self.camera_frame = camera_frame
        self.hands = mp.solutions.hands.Hands()
        self.registered_gestures = {}
        self.load_registered_gestures()

    def load_registered_gestures(self):
        try:
            with open("registered_gestures.pkl", "rb") as file:
                self.registered_gestures = pickle.load(file)
        except FileNotFoundError:
            pass

    def save_registered_gestures(self):
        with open("registered_gestures.pkl", "wb") as file:
            pickle.dump(self.registered_gestures, file)

    def register_gestures(self):
        print("Registering gestures: Perform a gesture and assign a function.")
        cap = cv2.VideoCapture(0)
        
        while True:
            success, image = cap.read()
            if not success:
                continue

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.hands.process(image)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    gesture_name = input("Enter gesture name or action (e.g., 'volume up', 'brightness down'): ")
                    self.registered_gestures[gesture_name] = hand_landmarks.landmark
                    print(f"Gesture '{gesture_name}' registered.")
                    self.save_registered_gestures()
                    break

            cv2.imshow("Register Gesture", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def start_gesture_control(self):
        cap = cv2.VideoCapture(0)
        
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                continue

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.hands.process(image)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for gesture, landmarks in self.registered_gestures.items():
                        if self.is_gesture_match(hand_landmarks.landmark, landmarks):
                            print(f"Gesture '{gesture}' detected! Executing action...")

            cv2.imshow("Gesture Control", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def is_gesture_match(self, current_landmarks, registered_landmarks):
        threshold = 0.1  # Matching threshold
        for i in range(len(current_landmarks)):
            dist = ((current_landmarks[i].x - registered_landmarks[i].x) ** 2 +
                    (current_landmarks[i].y - registered_landmarks[i].y) ** 2) ** 0.5
            if dist > threshold:
                return False
        return True
