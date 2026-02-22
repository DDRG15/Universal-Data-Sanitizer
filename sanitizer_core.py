"""
UNIVERSAL DATA SANITIZER CORE
Author: Diego Alonso Del Río García
Description: Logic engine to clean, sanitize, and structure raw/garbage text from OCR outputs.
Applies Zero-Trust principles and tolerance to AI/OCR hallucinations.
"""
import re

class DataSanitizer:
    def __init__(self):
        # 1. EXTRACTION TRIGGERS (Tolerance to OCR errors: 0 vs O confusion)
        self.tolerant_id_regex = r'^([0-9O]{4,14})\s+'
        
        # 2. VALUE CAPTURE (Finds isolated prices/amounts at the end of the line)
        self.trailing_amount_regex = r'(?<!\S)(\d{1,5}[.,]\d{2})\s*[A-Za-z]?\s*$'
        
        # 3. NOISE FILTER (Blacklist)
        self.blacklist = [
            "TOTAL", "SUBTOTAL", "TAX", "CASH", "CARD", 
            "DATE:", "TIME:", "CUSTOMER", "ID:", "CASHIER"
        ]

    def is_noise(self, line):
        """Checks if the line contains garbage data that should be discarded."""
        line_upper = line.upper()
        return any(word in line_upper for word in self.blacklist)

    def extract_data(self, line):
        """Attempts to extract an ID and an amount from a raw/dirty line."""
        if self.is_noise(line):
            return None

        result = {"id": None, "amount": None, "status": "REJECTED"}

        # Search for ID (e.g., product code or transaction ID)
        match_id = re.search(self.tolerant_id_regex, line)
        if match_id:
            # Fix OCR hallucination (Replace 'O' with '0')
            result["id"] = match_id.group(1).replace('O', '0')

        # Search for Trailing Amount
        match_amount = re.search(self.trailing_amount_regex, line)
        if match_amount:
            result["amount"] = match_amount.group(1).replace(',', '.')

        if result["id"] and result["amount"]:
            result["status"] = "APPROVED"

        return result

# Mock Test
if __name__ == "__main__":
    engine = DataSanitizer()
    raw_ocr_text = "O01234 DUSTY PRODUCT NAME 14.50"
    print(f"Input: {raw_ocr_text}")
    print(f"Structured Output: {engine.extract_data(raw_ocr_text)}")
