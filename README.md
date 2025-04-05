
# 🎯 Real-Time Face Recognition using OpenCV & DeepFace

A real-time facial recognition system powered by [OpenCV](https://opencv.org/) and [DeepFace](https://github.com/serengil/deepface).  
This application captures webcam frames, detects faces, and matches them with known faces stored in a local directory.

---

## 🧠 How It Works

- 📷 Captures webcam feed in real-time
- 🧍 Detects faces using OpenCV backend
- 🧠 Compares detected faces with images in `known_faces/` using DeepFace
- ✅ Displays name if match found / ❌ "No Match Found" otherwise

---

## 🗂️ Project Structure

```
face-recognition-deep/
├── known_faces/
│   ├── abby.jpg
│   └── someone.jpg
├── face_recognition.py
├── requirements.txt
└── README.md
```

---

## 🔧 Dependencies

Install these Python packages:

- `opencv-python`
- `deepface`
- `tensorflow`
- `tf-keras` (for RetinaFace compatibility)

All listed in `requirements.txt`

---

## 🚀 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/Abhijeetsingh0022/face-recognition-deep.git
cd face-recognition-deep
```

### 2. Create Virtual Environment (Recommended)
```bash
python3 -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt

# If tf-keras error occurs:
pip install tf-keras
```

### 4. Add Known Faces
Add clear front-facing images to `known_faces/` folder.  
Filename (without extension) will be used as display name.

---

## 🧪 Running the App
```bash
python face_recognition.py
```
**✅ Press ESC** to exit

---

## 📋 Notes

- Default face detection uses OpenCV backend
- Switch backends: `DeepFace.find(..., detector_backend='mtcnn')`
- Use high-quality, well-lit images in `known_faces/`
- `venv/` already ignored in `.gitignore`

---

## ❓ Troubleshooting

**Face Not Detected?**
- Check webcam functionality
- Ensure good lighting and visibility
- Try different detector backend:
```python
DeepFace.find(..., detector_backend='mtcnn')  # or 'retinaface', 'ssd'
```

**tf-keras Error?**
```bash
pip install tf-keras
# OR downgrade TensorFlow
pip install tensorflow==2.12.0
```

---

## 🙋‍♂️ Author
**Abhijeet Singh**  
GitHub: [@Abhijeetsingh0022](https://github.com/Abhijeetsingh0022)  
*"Code. Debug. Repeat."*

---

## 🪪 License
MIT License

---

## ⭐️ Support & Contributions
- ⭐ Star the repo
- 🍴 Fork & improve
- 🐛 Submit issues/ideas

---

## 🔮 Coming Soon
- WhatsApp Notifications
- Location Tracking
- Mobile App Interface
- Multi-Face Support
```
