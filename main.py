import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# === CONFIGURATION ===
CSV_PATH = "guests.csv"               # Path to your CSV file
IMAGE_PATH = "invitation_og.jpg"      # Path to the original image
OUTPUT_DIR = "output_invitations"     # Folder where personalized images will be saved
FONT_PATH = "fonts/font_sahadeva.ttf" # Path to a .ttf font file (can use default system font)
FONT_SIZE = 36                        # Size of the guest name text
TEXT_POSITION = (330, 382)            # (x, y) position on the image to draw the name
TEXT_COLOR = (255, 255, 255)          # RGB color of the text

# === VALIDATE FILES ===
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"CSV file not found: {CSV_PATH}")

if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"Image file not found: {IMAGE_PATH}")

print("✅ Files found. Proceeding...")

# === LOAD CSV ===
df = pd.read_csv(CSV_PATH)
print(f"📄 CSV Loaded. Total names: {len(df)}")

if 'name' not in df.columns:
    raise ValueError("CSV must contain a 'name' column.")
else:
    print("✅ 'name' column found in CSV.")

# === PREP OUTPUT FOLDER ===
os.makedirs(OUTPUT_DIR, exist_ok=True)
if not os.access(OUTPUT_DIR, os.W_OK):
    raise PermissionError(f"Cannot write to output directory: {OUTPUT_DIR}")

print(f"📂 Output directory ready: {OUTPUT_DIR}")

# === LOAD FONT ===
try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    print(f"✅ Font loaded: {FONT_PATH}")
except IOError:
    print("⚠️ Font not found. Using default font.")
    font = ImageFont.load_default()

# === GENERATE IMAGES ===
for index, row in df.iterrows():
    name = str(row['name']).strip()
    if not name:
        print(f"⚠️ Skipping empty name at row {index}")
        continue

    try:
        with Image.open(IMAGE_PATH).convert("RGB") as img:
            draw = ImageDraw.Draw(img)
            draw.text(TEXT_POSITION, name, font=font, fill=TEXT_COLOR)

            output_filename = f"{name.replace(' ', '_')}.jpg"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            img.save(output_path)
            print(f"✅ Saved: {output_path}")
    except Exception as e:
        print(f"❌ Failed to create image for '{name}': {e}")

print("🎉 All invitations processed.")
