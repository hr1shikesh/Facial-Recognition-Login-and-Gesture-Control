import tkinter as tk
from tkinter import ttk, messagebox
from facial_recognition import FacialRecognition
from gesture_recognition import GestureRecognition
from system_controls import SYSTEM_CONTROLS  # A dictionary of system controls

class SignInApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HCI System: Sign In/Sign Up")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Sign In or Sign Up", font=("Helvetica", 24, "bold"), fg="#4CAF50", bg="#1e1e1e")
        title_label.pack(pady=20)

        tk.Button(self.root, text="Sign In", font=("Helvetica", 14), command=self.sign_in).pack(pady=10)
        tk.Button(self.root, text="Sign Up", font=("Helvetica", 14), command=self.sign_up).pack(pady=10)

    def sign_in(self):
        messagebox.showinfo("Sign In", "Sign In Successful!")
        self.open_main_gui()

    def sign_up(self):
        messagebox.showinfo("Sign Up", "Sign Up Successful!")
        self.open_main_gui()

    def open_main_gui(self):
        self.root.destroy()
        new_root = tk.Tk()
        MainApp(new_root).run()

    def run(self):
        self.root.mainloop()


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HCI System: Main Page")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.face_recog = FacialRecognition(None)  # Camera frame not needed here
        self.gesture_recog = GestureRecognition(None)

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="HCI System: Main Page", font=("Helvetica", 24, "bold"), fg="#4CAF50", bg="#1e1e1e")
        title_label.pack(pady=20)

        tk.Button(self.root, text="Register Face Profile", font=("Helvetica", 14), command=self.register_face).pack(pady=10)
        tk.Button(self.root, text="Register Gestures", font=("Helvetica", 14), command=self.register_gestures).pack(pady=10)
        tk.Button(self.root, text="Control System with Gestures", font=("Helvetica", 14), command=self.control_system).pack(pady=10)

    def register_face(self):
        self.face_recog.register_face("New User")

    def register_gestures(self):
        self.root.destroy()
        new_root = tk.Tk()
        GestureRegistrationApp(new_root).run()

    def control_system(self):
        self.gesture_recog.start_gesture_control()

    def run(self):
        self.root.mainloop()


class GestureRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HCI System: Gesture Registration")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.gesture_recog = GestureRecognition(None)
        self.selected_control = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Register Gestures", font=("Helvetica", 24, "bold"), fg="#4CAF50", bg="#1e1e1e")
        title_label.pack(pady=20)

        control_label = tk.Label(self.root, text="Select System Control:", font=("Helvetica", 14), fg="white", bg="#1e1e1e")
        control_label.pack(pady=10)

        control_dropdown = ttk.Combobox(self.root, textvariable=self.selected_control, values=list(SYSTEM_CONTROLS.keys()), font=("Helvetica", 12))
        control_dropdown.pack(pady=10)

        tk.Button(self.root, text="Open Camera for Gesture Input", font=("Helvetica", 14), command=self.open_camera).pack(pady=10)

    def open_camera(self):
        selected_control = self.selected_control.get()
        if not selected_control:
            messagebox.showerror("Error", "Please select a system control.")
        else:
            self.gesture_recog.register_gestures(SYSTEM_CONTROLS[selected_control])

    def run(self):
        self.root.mainloop()
