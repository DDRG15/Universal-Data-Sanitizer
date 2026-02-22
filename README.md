# 🛡️ Universal Data Sanitizer

**Extraction and Sanitization Architecture for Unstructured Data (OCR)**

This repository contains a Python-based logic engine designed to process, sanitize, and structure "dirty" or corrupted text streams coming from Optical Character Recognition (OCR) engines.

## 🧠 The Problem
OCR tools (like Google ML Kit or Tesseract) frequently suffer from "hallucinations" (e.g., confusing the number `0` with the letter `O`) and capture garbage text from physical document margins. Standard extraction algorithms fail when facing this level of inconsistency.

## 🛠️ The Solution (Zero-Trust Logic)
I developed this engine based on **Zero-Trust** principles (never trust the raw data input). It uses advanced regular expressions (Regex) and exclusion dictionaries to achieve:

1. **Fault Tolerance:** Usage of *Lookaheads/Lookbehinds* to capture specific structures while ignoring surrounding noise.
2. **Hallucination Correction:** Proactive cleaning of mutated characters during runtime.
3. **White-Noise Filtering:** Implementation of dynamic *Blacklists* to discard headers, footers, and irrelevant metadata.

## 🚀 Impact
This logic serves as the core for larger financial data extraction and physical document auditing projects, ensuring that databases only receive clean, structured JSON payloads, effectively preventing system crashes due to corrupted data injection.

---
*Profile focused on QA Automation, Edge Cases, and Data Extraction.*
