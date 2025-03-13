# Face Recognition Attendance Application - Using PyQt6

### Features
- Class Entry and End Time Recording
- Face Registration
- Daily Attendance Management

### Tools
- Programming Language: **Python 3.12 (PyCharm Community 2024)**
- File Processing: **CSV**
- User Interface: **Qt6**

## Installing Dependencies for Facial Recognition

### Required Resources:
1. **Visual Studio**: [Download here](https://visualstudio.microsoft.com/fr/)  
   _(During Installation: Select "Desktop Development with C++" workload)_

2. **CMake**: [Download here](https://cmake.org/download/)

### Install Libraries:
Run the following commands in the terminal:
```bash
pip install cmake
pip install dlib==19.24.99
pip install opencv-python
pip install face-recognition
pip install numpy
```
### Typical error:
**Cannot install dlib**
1. MAKE SURE you have a SINGLE and proper version of Python
2. Make sure you have latest pip version
```bash
pip --version
python -m pip install --upgrade pip
```
3. Python version < 3.12 is more recommended while installing dlib, but if you use Python 3.12, it's still okay ^^
4. Download [dlib-19.24.99-cp312-cp312-win_amd64.whl](https://github.com/z-mahmud22/Dlib_Windows_Python3.x/blob/main/dlib-19.24.99-cp312-cp312-win_amd64.whl) (for Python 3.12 version)
```bash
pip install dlib-19.24.99-cp39-cp39-win_amd64.whl
```
5. During the download of packages(dlib, etc.) ur antivirus is turned off, or takes those packages as exceptions
