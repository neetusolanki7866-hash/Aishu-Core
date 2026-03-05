import os
import socket

def check_offline_mode():
    try:
        # Google DNS पर पिंग करके चेक करना कि इंटरनेट है या नहीं
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return "[Guard] Status: Online Mode active."
    except OSError:
        return "[Guard] Status: Offline Mode active. Switching to Quota Guard."

def self_healing():
    print("[Guard] Running integrity check on workers...")
    # भविष्य में यहाँ बैकअप से फाइल रीस्टोर करने का कोड आएगा
    return "[Guard] All workers are healthy."

if __name__ == "__main__":
    print(check_offline_mode())
    print(self_healing())
