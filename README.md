# C.Q.B.v2

## 📦 Installation Guide

Follow these steps to set up the project locally.

## ⚠️ Python Version Requirement

This project is built specifically for **Python 3.11.x**.

> ❗ Using newer versions (e.g., Python 3.12 or later) may result in errors such as:
> ```
> _tkinter.TclError: Can't find a usable tk.tcl
> ```
> or similar issues due to `tkinter` not being properly configured in the newer Python distributions.

---

### ✅ Check Your Version:

```bash
python --version
```
If you are not on Python 3.11, download and install it from the official site:

[Download Python 3.11](https://www.python.org/downloads/release/python-3110/)

On Windows, make sure to check the box “Add Python to PATH” during installation.

### 1. Clone the Repository

To get started, clone the repository to your local machine using the following command:
```bash
git clone https://github.com/Abeltodoanything/cqbv2.git 
```
Then navigate into the project directory:
```bash
cd cqbv2
```
### 2. (Optional but Recommended) Create a Virtual Environment

Using a virtual environment helps you avoid dependency conflicts.

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

### 4. Run the Application

You can now run the main script to launch the application.

On macOS/Linux:
```bash
python3 main.py
```
On Windows:
```bash
python main.py
```
