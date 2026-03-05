import json
import datetime
import os

LOG_FILE = "AISHU_GOLD_OS/brain_logs/evolution_data.json"

def save_learning(query, response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "time": timestamp,
        "input": query,
        "learned_pattern": response
    }
    
    # Logs folder check
    if not os.path.exists("AISHU_GOLD_OS/brain_logs"):
        os.makedirs("AISHU_GOLD_OS/brain_logs")

    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(data) + "\n")
        return f"[Brain_Worker_2] Pattern saved: Aishu is now 0.1% smarter."
    except Exception as e:
        return f"[-] Learning Error: {e}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(save_learning(sys.argv[1], "User Preference Recorded"))
