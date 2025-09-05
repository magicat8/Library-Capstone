import csv
from datetime import datetime

CSV_FILE = "scanned_barcodes.csv"

# Function to classify barcode type
def classify_barcode(code: str) -> str:
    code = code.strip()
    if not code.isdigit():
        return "Invalid"

    length = len(code)
    if length == 12:
        return "UPC-A"
    elif length == 13:
        if code.startswith(("978", "979")):
            return "ISBN-13"
        else:
            return "EAN-13"
    elif length == 10:
        return "ISBN-10"
    else:
        return "Unknown"

# Function to log barcode to CSV
def log_barcode(code: str, code_type: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, code, code_type])
    print(f"Logged: {code} ({code_type}) at {timestamp}")

# Initialize CSV file with header if it doesn't exist
try:
    with open(CSV_FILE, "x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Barcode", "Type"])
except FileExistsError:
    pass  # file already exists

# Main loop to read barcodes
print("Ready to scan barcodes (press Ctrl+C to exit)...")
try:
    while True:
        barcode = input().strip()
        if not barcode:
            continue
        barcode_type = classify_barcode(barcode)
        log_barcode(barcode, barcode_type)
except KeyboardInterrupt:
    print("\nExiting. Goodbye!")
