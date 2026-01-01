
# ⏳ Chronos: The Trinity Architecture

> **A full-stack Version Control System built from first principles.**
> *Now available as a standalone executable (No Python Required).*

---

## 📖 Overview
Chronos is a distributed system architecture exploring the fundamentals of software tools. It implements the "Trinity" of modern computing:

1.  **Storage Engine (Chronos):** A content-addressable storage system using SHA-1 hashing.
2.  **Network Layer (Setu):** A custom multi-threaded HTTP Web Server built on raw TCP sockets.
3.  **Client Interface (Sarathi):** A remote Command Line Interface (CLI).

---

## 🚀 How to Download & Run (Easiest Way)

**You do NOT need Python installed.**

1.  Go to the [**Releases Page**](../../releases) of this repository.
2.  Download **`Chronos.exe`**.
3.  Open your terminal in the folder where you downloaded it.
4.  Run it directly:

```powershell
# Initialize a repository
.\Chronos.exe init

# Save a snapshot
.\Chronos.exe commit "My first backup"

```

---

## 🛠️ For Developers (Source Code)

If you want to modify the engine yourself, you need Python 3.x.

### Installation

```bash
git clone [https://github.com/anshu-builds/Chronos.git](https://github.com/anshu-builds/Chronos.git)
cd Chronos

```

### Build your own EXE

If you modify the code, you can rebuild the executable:

```bash
pip install pyinstaller
pyinstaller --onefile --name "Chronos" chronos.py

```

---

## 🏗️ Architecture Highlights

* **Sockets:** Manual implementation of `socket.AF_INET` and `socket.SOCK_STREAM`.
* **Database:** Custom binary object storage (Blobs and Trees).
* **Compiling:** Built into a static binary using PyInstaller.

---

*Built by Anshu Jaiswal as part of his AI Engineering Roadmap.*
