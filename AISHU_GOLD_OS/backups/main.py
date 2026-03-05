
import os
import json
import time

# 1. लोड प्रोटोकॉल
def load_protocol():
    with open('AISHU_GOLD_OS/protocol.json', 'r') as f:
        return json.load(f)

def run_aishu_gold():
    protocol = load_protocol()
    # आपकी सुरक्षा शर्तें और सीक्रेट स्विच
    dead_man_switch = "aishu shutdown"
    
    print(f"\n--- MADHU OS: THE FINAL BLUEPRINT ACTIVE ---")
    print(f"Owner: {protocol['owner']} | Mode: Human-Supervised Modular AI")
    
    while True:
        query = input(f"\n{protocol['owner']}, Command: ").lower()

        # 1. Dead-Man's Switch (Emergency Shutdown)
        if dead_man_switch in query:
            print("\n[!!!] Aishu: इमरजेंसी शटडाउन। सुरक्षित रहें नीर सर।")
            break

        # 2. Madhu_OS Master Recall (Blueprint Status)
        elif "madhu_os" in query:
            print("\n--- MADHU OS: THE FINAL BLUEPRINT ---")
            print("[+] Status: Modular AI Engine Online")
            print("[+] Workers: 50 Total (Brain:30, Ghost:10, Coder:5, Earner:5)")
            print("[+] Guard: Hybrid Logic & Self-Healing Active")
            print("[+] Security: UPI Entry Rule (Min. 500) Locked")
            print("[+] Memory: Evolution Logs Saving to Brain_Worker_2")
            print("\nNext Objective: Auto-Backup & Offline Quota Guard.")

        # 3. Backup System (New: Step 22)
        elif "backup" in query or "save" in query:
            print("[*] Aishu: बैकअप वर्कर को काम पर लगा रही हूँ...")
            os.system("python AISHU_GOLD_OS/workers/Backup_Worker_1.py")

        # 4. UPI Logic (Min 500 Rule)
        elif "upi" in query or "paisa" in query or "pay" in query:
            amount = input("Aishu: राशि दर्ज करें (Min. 500): ")
            if amount.isdigit() and int(amount) >= 500:
                print(f"[*] Aishu: {amount} की एंट्री स्वीकार की गई।")
                os.system(f"python AISHU_GOLD_OS/workers/Earning_Worker_1.py '{query}'")
            else:
                print("[-] Aishu: सर, नियम के अनुसार राशि 500 से ऊपर होनी चाहिए।")

        # 5. Standard Operations & Learning
        else:
            if "ghost" in query:
                os.system("python AISHU_GOLD_OS/workers/Ghost_Worker_1.py")
                os.system("python AISHU_GOLD_OS/workers/Ghost_Worker_2.py")
            elif "fix" in query or "guard" in query:
                os.system("python AISHU_GOLD_OS/workers/Guard_Worker_1.py")
            else:
                # Default Brain Execution
                os.system(f"python AISHU_GOLD_OS/workers/Brain_Worker_1.py '{query}'")
            
            # हर बातचीत को याद रखना (Self-Learning)
            os.system(f"python AISHU_GOLD_OS/workers/Brain_Worker_2.py '{query}'")

if __name__ == "__main__":
    run_aishu_gold()
