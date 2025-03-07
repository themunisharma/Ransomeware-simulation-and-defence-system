import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Backup folder path
backup_folder = "backup"

# Function to create a backup of files
def create_backup(folder_path):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        backup_path = os.path.join(backup_folder, file)

        if os.path.isfile(file_path):
            shutil.copy(file_path, backup_path)
    print(" Backup Created!")

# Detect suspicious file changes (potential ransomware activity)
class RansomwareDetector(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".txt") or event.src_path.endswith(".docx"):
            print(f" Warning: Possible ransomware activity detected! {event.src_path} modified.")
            create_backup("test_folder")

# Monitor folder for suspicious activity
def monitor_folder(folder_path):
    event_handler = RansomwareDetector()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Start monitoring
if __name__ == "__main__":
    print("🔍 Monitoring for ransomware activity...")
    monitor_folder("test_folder")
