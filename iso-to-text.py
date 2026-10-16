import os

iso_filename = "Whatever.iso" #please change this to your iso name :)
output_filename = "iso_raw_dump.txt" #you can rename this to whatever txt you want just keep the name in mind

if not os.path.exists(iso_filename):
    print(f"Error: Could not find '{iso_filename}' in this folder.")
else:
    print(f"Streaming {iso_filename} directly to {output_filename} in chunks...")
    
    with open(iso_filename, "rb") as infile, open(output_filename, "w", encoding="utf-8") as outfile:
        chunk_size = 10 * 1024 * 1024 
        
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break
                
            text_chunk = chunk.decode('utf-8', errors='backslashreplace')
            outfile.write(text_chunk)
            
    print("Done! The conversion finished successfully without running out of memory.")
