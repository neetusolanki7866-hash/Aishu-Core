
import os
import json

def load_protocol():
    with open('AISHU_GOLD_OS/protocol.json', 'r') as f:
        return json.load(f)

def run_aishu_gold():
    protocol = load_protocol()
    print(f"\n--- MADHU OS: ADVANCED ACCESS ACTIVE ---")
    
    while True:
        query = input(f"\n{protocol['owner']}, Command: ").lower()

        if "aishu shutdown" in query:
            print("\n[!!!] Aishu: सुरक्षित शटडाउन।")
            break

        # Advanced Ghost Mode
        elif "madhu access granted" in query:
            print("\n[!] GHOST MODE: एक्टिवेटेड। नीर सर, अब आप सिस्टम की गहराइयों में जा सकते हैं।")
            os.system("python AISHU_GOLD_OS/workers/Ghost_Worker_1.py")

        # Voice Module
        elif "voice" in query:
            os.system("python AISHU_GOLD_OS/workers/Voice_Worker_1.py")

        # Regular Blueprint
        elif "madhu_os" in query:
            print("\n--- MADHU OS: FINAL BLUEPRINT STATUS ---")
            print("[+] Voice Core: Synced | Advanced Access: Open")
            print("[+] Memory: Learning Active | Quota Guard: Restricted Mode Ready")

        else:
            # Learning & Regular Brain
            os.system(f"python AISHU_GOLD_OS/workers/Brain_Worker_1.py '{query}'")
            os.system(f"python AISHU_GOLD_OS/workers/Brain_Worker_2.py '{query}'")

if __name__ == "__main__":
    run_aishu_gold()
