
iso_filename = "kali-linux.iso" # replace with your ISO path :)
output_filename = "iso_raw_dump.txt" # replace this with whatever txt file you want please note this could get really big

print(f" your {iso_filename} and converting to text...")

with open(iso_filename, "rb") as iso_file:
    raw_bytes = iso_file.read() 



raw_text_content = raw_bytes.decode('utf-8', errors='backslashreplace')

with open(output_filename, "w", encoding="utf-8") as text_file:
    text_file.write(raw_text_content)

print(f"Done converting")
