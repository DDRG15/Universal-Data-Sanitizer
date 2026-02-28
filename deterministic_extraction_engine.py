import re
import json
import psutil
import time
import gc  # Summoning the Garbage Collector because someone has to clean up this mess.

def bulletproof_processor(input_file, output_file, pause_threshold=80.0, disk_threshold=95.0):
    # The holy grail of our parsing logic. 
    # Stock is optional because we naturally assume the data source will disappoint us.
    pattern = re.compile(
        r"ID:\s*(?P<id>[A-Z0-9-]+).*?"
        r"PRODUCT:\s*(?P<name>[^|]+).*?"
        r"(?:PRICE:\s*S/\s*(?P<price>[\d.]+))?.*?"
        r"(?:Stock\s*(?P<stock>\d+))?",   
        re.IGNORECASE
    )

    print(f"--- 🕵️‍♂️ Initiating Deterministic Audit on {input_file} | Let's see what fresh hell this data brings ---")
    
    # 1. PRE-FLIGHT CHECK
    # We don't start the engine if the garage is full. 
    initial_disk = psutil.disk_usage('/').percent
    if initial_disk > disk_threshold:
        print(f"🛑 CRITICAL: Disk space at {initial_disk}%. I'm an auditor, not a hoarder. Aborting mission.")
        return

    with open(input_file, "r", encoding="utf-8") as f_in, \
         open(output_file, "w", encoding="utf-8") as f_out:
        
        for i, line in enumerate(f_in):
            match = pattern.search(line)
            if not match:
                continue # Not worth our time. Ignore and move on.
            
            data = match.groupdict()
            
            # Deterministic Sanitization
            # Because an 'O' is not a '0', and a '3' is not an 'e'. 
            # Honestly, who writes this stuff? We fix it anyway.
            result = {
                "ID": re.sub(r"^O", "0", data['id']),
                "Name": data['name'].strip().replace("3", "e"),
                "Price": float(data['price']) if data['price'] else None,
                "Stock": int(data['stock']) if data['stock'] else 0 # No stock listed? You get a 0. Deal with it.
            }

            # Streaming mode. We keep the memory footprint flat because we have manners.
            f_out.write(json.dumps(result, ensure_ascii=False) + "\n")

            # 2. REAL-TIME HARDWARE AUDIT
            # Checking vitals every 10,000 lines. I refuse to be the reason the server catches fire. (It's not me, it's you).
            if i > 0 and i % 10000 == 0:
                mem = psutil.virtual_memory().percent
                disk = psutil.disk_usage('/').percent
                
                # Kill Switch
                if disk > disk_threshold:
                    print(f"🛑 RED ALERT: Disk at {disk}%. Hitting the brakes before we corrupt everything.")
                    break 

                # Memory Management
                if mem > pause_threshold:
                    print(f"🚨 Memory at {mem}%. Python is hoarding RAM again. Forcing garbage collection...")
                    gc.collect()  # Taking out the trash.
                    time.sleep(2) # Shh... let the CPU take a breather.

    print(f"--- ✅ Process Complete. Data is now bulletproof in {output_file}. You're welcome. ---")