import os
import sys
import subprocess

# Ensure required packages are installed
try:
    from PIL import Image
except ImportError:
    print("Pillow not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image  # Retry import

# Folder containing .ithmb files
SOURCE_FOLDER = "C:\\py"  # Change this to your actual folder
DEST_FOLDER = os.path.join(SOURCE_FOLDER, "converted")

# Ensure the destination folder exists
os.makedirs(DEST_FOLDER, exist_ok=True)

def convert_ithmb_to_jpeg(ithmb_file):
    """Convert .ithmb file to JPEG format."""
    try:
        with Image.open(ithmb_file) as img:
            jpeg_filename = os.path.join(DEST_FOLDER, os.path.basename(ithmb_file).replace(".ithmb", ".jpg"))
            img.convert("RGB").save(jpeg_filename, "JPEG")
            print(f"Converted: {ithmb_file} -> {jpeg_filename}")
    except Exception as e:
        print(f"Error converting {ithmb_file}: {e}")

def main():
    """Finds and converts all .ithmb files in the folder."""
    files = [f for f in os.listdir(SOURCE_FOLDER) if f.lower().endswith(".ithmb")]
    
    if not files:
        print("No .ithmb files found.")
        return

    for file in files:
        convert_ithmb_to_jpeg(os.path.join(SOURCE_FOLDER, file))

if __name__ == "__main__":
    main()
