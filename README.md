# ⏳ Chronos: The Trinity Architecture

> **A full-stack Version Control System built from first principles.**
> *No Frameworks. No Libraries. Just raw Python.*

---

## 📖 Overview
Chronos is not just a version control system; it is a distributed system architecture exploring the fundamentals of how software tools work under the hood. 

It implements the "Trinity" of modern computing:
1.  **Storage Engine (Chronos):** A content-addressable storage system using SHA-1 hashing (inspired by Git).
2.  **Network Layer (Setu):** A custom multi-threaded HTTP Web Server built on raw TCP sockets.
3.  **Client Interface (Sarathi):** A remote Command Line Interface (CLI) that controls the system via API.

## 🏗️ Architecture

### 1. Chronos (The Core)
The heart of the system. It manages the `.chronos` database.
* **Mechanism:** Snapshot-based versioning.
* **Hashing:** SHA-1 algorithm to ensure data integrity.
* **Storage:** Content-Addressable Storage (CAS) pattern.

### 2. Setu (The Bridge) 🌉
A custom-built Web Server and API.
* **Protocol:** HTTP/1.1 implemented manually on top of TCP `socket`.
* **Role:** Exposes the internal state of Chronos to the web.
* **Endpoints:**
    * `GET /`: System Status & Health.
    * `GET /log`: Real-time inventory of committed objects.

### 3. Sarathi (The Driver) 🏎️
The client-side terminal application.
* **Role:** Acts as the remote controller for the system.
* **Communication:** Connects to Setu via RESTful API calls.
* **Features:** Remote status checking and log retrieval.

---

## 🚀 How to Run

### Prerequisites
* Python 3.x
* No external pip packages required for the core engine.

### Installation
```bash
git clone [https://github.com/your-username/Chronos.git](https://github.com/your-username/Chronos.git)
cd Chronos
