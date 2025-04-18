# Gesture and Facial Recognition Based HCI System

A touch-free Human-Computer Interaction (HCI) system that combines facial recognition for secure authentication and gesture-based controls for managing system functions, designed to enhance accessibility and usability for all users.

## 💡 Overview

With the rise in demand for contactless computing, this project introduces an innovative HCI system using:
- **Facial Recognition** (via Dlib) for secure, passwordless login
- **Gesture Recognition** (via OpenCV) for controlling brightness, volume, applications, and media playback

It is designed to aid both general users and differently-abled individuals, offering an intuitive and hands-free way to interact with computers.

## 🎯 Features

- 🔒 **Facial Recognition Login**  
  Secure user authentication using real-time face detection

- 👋 **Custom Gesture Profiles**  
  User-specific gestures for personalized control

- 💻 **System Control**  
  Adjust brightness, volume, and control cursor movement with hand gestures

- 📂 **Application Control**  
  Launch, close, and switch between applications with ease

- 🎞️ **Media & Screen Navigation**  
  Gesture support for media control, scrolling, and zooming

- 🔐 **Auto Lock/Unlock**  
  Locks screen when the user leaves and unlocks upon return

- 🔔 **Notification Management**  
  Dismiss or view notifications using gestures

## ⚙️ Technologies Used

- [OpenCV](https://docs.opencv.org/) – Real-time computer vision for gesture recognition
- [Dlib](http://dlib.net/) – Machine learning toolkit for facial recognition
- Python

## 🚀 How It Works

1. **Face Recognition**: Authenticates the user during login
2. **Gesture Detection**: Detects and maps predefined gestures to system actions
3. **Execution**: Executes mapped function (like changing volume, opening an app, etc.)

## 📌 Use Cases

- Hands-free system interaction for differently-abled users
- Touchless computing in hygiene-sensitive environments
- Efficient multitasking without a mouse or keyboard

## 📊 Related Projects Comparison

| System/Project      | Features                                                | Advantages of This System                                        |
|---------------------|----------------------------------------------------------|------------------------------------------------------------------|
| Microsoft Kinect     | Gesture control for gaming and apps                     | Desktop-oriented, with facial login and custom gestures          |
| Leap Motion          | VR/AR hand tracking                                     | Adds facial recognition and full system gesture control          |
| Apple Face ID        | Facial recognition only                                 | Integrated with gesture-based desktop interaction                |
| Google Soli          | Radar-based gestures (mobile-focused)                  | Broader application scope, PC-specific multi-user profiles       |
| Intel RealSense      | 3D sensing, facial detection                            | Prioritized accessibility, with personalized gesture workflows   |

## 📚 References

- [OpenCV Documentation](https://docs.opencv.org/)
- [Dlib Documentation](http://dlib.net/)
- ResearchGate: *Real-Time HCI Based on Face and Hand Gesture Recognition*
- Nadiapub: *Gesture Recognition in HCI* – [View Article](https://article.nadiapub.com)

## 🤝 Contributions

Contributions are welcome! Feel free to fork this repo and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

---

### 👁️‍🗨️ Future Enhancements

- AI-driven gesture learning
- Voice-gesture hybrid interaction
- Cross-platform support (Linux/macOS)
