#  Ransomware Simulation and Defense

A **Python-based ransomware simulation and defense system** that demonstrates how ransomware works and how to defend against it.

---

##  Features

### **Ransomware Simulation:**
-  Encrypts files using **AES encryption**
-  Generates a **ransom note**

### **Defense System:**
-  **Monitors file activity** to detect ransomware behavior
-  **Creates automatic backups** of files
-  Provides **decryption** with a saved encryption key

---

## ⚙️ Installation

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/themunisharma/Ransomeware-simulation-and-defence-system
cd Ransomeware-simulation-and-defence-system
```

### **Step 2: Install Dependencies**
```bash
pip install cryptography watchdog
```

---

## 🛠️ Usage

### **1. Run Ransomware Simulation**
```bash
python encryptor.py
```
- Encrypts files in `test_folder`
- Generates `encryption_key.key` for decryption
- Creates a ransom note

### **2. Run the Defense System (before attack)**
```bash
python defender.py
```
- Monitors `test_folder` for suspicious encryption activity
- Creates automatic file backups

### **3. Run Decryption (if key is available)**
```bash
python decryptor.py
```
- Restores encrypted files using `encryption_key.key`

---

## 🔒 Project Files

| File         | Description                              |
|-------------|----------------------------------|
| `encryptor.py` | Encrypts files (simulating ransomware) |
| `decryptor.py` | Decrypts files using saved key        |
| `defender.py`  | Detects ransomware activity & backs up files |
| `README.md`    | Project documentation                |

---

## ⚠️ Disclaimer
This project is for **educational and ethical hacking purposes only**. **Do not use this for malicious activities.**


---

## 💻 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

