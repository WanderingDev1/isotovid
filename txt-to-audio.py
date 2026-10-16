import os
import numpy as np
import time

txt_filename = "iso_raw_dump.txt" # or whatever it is named as
audio_filename = "kali_cyber_noise.raw"  # or whatever you want it to be called
sample_rate = 44100  


chunk_size = 1024 * 1024

if not os.path.exists(txt_filename):
    print(f"Error: Could not find '{txt_filename}'")
else:
    print("done with step 1")
    
    with open(txt_filename, "rb") as infile, open(audio_filename, "wb") as outfile:
        
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break 
                

            audio_samples = np.frombuffer(chunk, dtype=np.uint8)
            

            audio_samples = ((audio_samples.astype(np.float32) / 255.0) * 2.0 - 1.0) * 16000
            audio_samples = audio_samples.astype(np.int16)
            
            outfile.write(audio_samples.tobytes())
            
            time.sleep(0.001)
            
    print(f"\n✅ SUCCESS! Your massive raw audio track is saved: '{audio_filename}'")
