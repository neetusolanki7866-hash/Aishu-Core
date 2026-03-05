import os
import shutil
from datetime import datetime

def create_backup():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"Madhu_OS_Backup_{now}"
    source_dir = "/data/data/com.termux/files/home" # Home directory
    backup_dir = "/data/data/com.termux/files/home/AISHU_GOLD_OS/backups"

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    print(f"\n[Backup_Worker_1] Backing up Madhu OS...")
    try:
        # Pura project zip karna
        shutil.make_archive(os.path.join(backup_dir, backup_name), 'zip', source_dir, 'AISHU_GOLD_OS')
        shutil.copy("/data/data/com.termux/files/home/main.py", backup_dir)
        return f"[+] Backup Successful: {backup_name}.zip saved in AISHU_GOLD_OS/backups/"
    except Exception as e:
        return f"[-] Backup Failed: {e}"

if __name__ == "__main__":
    print(create_backup())
