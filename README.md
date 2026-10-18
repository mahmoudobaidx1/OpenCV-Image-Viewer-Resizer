# OpenCV Image Viewer & Resizer

A lightweight Python application built with **OpenCV** that enables users to display, dynamically resize, and manage image files using simple keyboard shortcuts.

---

## 🌟 Key Features

- **Interactive Image Viewing:** Display target images using OpenCV's native GUI window.
- **Keyboard Shortcut Actions:**
  - `e` — Exit the program immediately.
  - `s` — Save the loaded image to the `./saved images/` folder.
  - `r` — Trigger console prompts to resize the image using custom height and width parameters.
- **Resized Image Handling:**
  - `s` — Save the resized image to `./saved images/`.
  - `d` — Save/move the resized image to `./delete/` for archiving or deletion.
  - `e` — Close the interactive window without saving.

---

## 📁 Directory Structure

Ensure the required folders exist before running the application, or update the script to create them automatically:

```text
.
├── images/
│   └── gsd.png          # Input image file
├── saved images/        # Destination directory for saved files
├── delete/              # Destination directory for deleted/archived files
└── main.py              # Application script
```

---

## 🚀 Getting Started

### Prerequisites

You need **Python 3.x** installed along with OpenCV. You can install OpenCV using `pip`:

```bash
pip install opencv-python
```

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

---


```

---

## 📄 License

This project is licensed under the MIT License — feel free to modify and distribute.