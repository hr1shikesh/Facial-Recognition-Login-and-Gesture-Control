import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from facial_recognition import FacialRecognition
from gesture_recognition import GestureRecognition

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HCI System: Gesture and Facial Recognition Login")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")  # Dark background for a sleek look
        self.root.resizable(False, False)

        self.camera_frame = tk.Label(self.root, bg="#1e1e1e")
        self.camera_frame.pack(pady=20)

        self.face_recog = FacialRecognition(self.camera_frame)
        self.gesture_recog = GestureRecognition(self.camera_frame)

        self.create_widgets()

    def create_widgets(self):
        # Title Card
        title_label = tk.Label(self.root, text="HCI System\nGesture and Facial Recognition Login", 
                               font=("Helvetica", 24, "bold"), fg="#4CAF50", bg="#1e1e1e")
        title_label.pack(pady=20)

        # Buttons with glowing effect on hover and click
        self.create_glowing_button("Login with Face", self.face_login)
        self.create_glowing_button("Control System with Gestures", self.control_system)
        self.create_glowing_button("Register Face and Gestures", self.register_user)

    def create_glowing_button(self, text, command):
        # Create a button with a glow effect
        button = tk.Button(self.root, text=text, font=("Helvetica", 14, "bold"), fg="white", bg="#333333", 
                           relief="flat", padx=20, pady=10, command=command)
        button.pack(pady=10)
        
        # Add hover effect for glow
        button.bind("<Enter>", lambda e: button.config(bg="#4CAF50"))
        button.bind("<Leave>", lambda e: button.config(bg="#333333"))
        
        # Add click effect
        button.bind("<ButtonPress-1>", lambda e: button.config(bg="#66bb6a"))
        button.bind("<ButtonRelease-1>", lambda e: button.config(bg="#4CAF50"))

    def face_login(self):
        name = self.prompt_for_name("Enter your name for login:")
        if name:
            match_percentage = self.face_recog.login(name)
            self.handle_login_result(match_percentage)

    def control_system(self):
        self.gesture_recog.start_gesture_control()

    def register_user(self):
        name = self.prompt_for_name("Enter your name for registration:")
        if name:
            registered = self.face_recog.register_face(name)
            if registered:
                messagebox.showinfo("Registration Success", f"Face registered successfully for {name}!")
            else:
                messagebox.showerror("Registration Failed", "Face registration failed. Please try again.")

    def prompt_for_name(self, prompt_text):
        # Prompt to enter name
        name_window = tk.Toplevel(self.root)
        name_window.title("Enter Name")
        name_window.geometry("300x150")
        name_window.configure(bg="#1e1e1e")

        label = tk.Label(name_window, text=prompt_text, font=("Helvetica", 12), fg="white", bg="#1e1e1e")
        label.pack(pady=10)

        name_entry = tk.Entry(name_window, font=("Helvetica", 14), fg="black", bg="#e0e0e0", bd=2, relief="solid")
        name_entry.pack(pady=5)
        name_entry.focus_set()

        def submit_name():
            name = name_entry.get()
            if name:
                name_window.destroy()
                return name
            else:
                messagebox.showerror("Error", "Name cannot be empty!")

        submit_button = tk.Button(name_window, text="Submit", font=("Helvetica", 12), fg="white", bg="#4CAF50", 
                                  command=submit_name)
        submit_button.pack(pady=10)

        name_window.wait_window(name_window)
        return name_entry.get()

    def handle_login_result(self, match_percentage):
        if match_percentage > 50:
            messagebox.showinfo("Login Success", f"Welcome back! Match: {match_percentage:.2f}%")
        else:
            messagebox.showerror("Login Failed", f"Login failed. Match: {match_percentage:.2f}%")

    def run(self):
        self.root.mainloop()
