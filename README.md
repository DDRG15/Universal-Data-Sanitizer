# 🛡️ Universal Data Sanitizer & Recon Toolkit

Welcome to my data engineering arsenal. This repository contains a suite of Python-based logic engines designed for two main purposes: **Reconnaissance** (mapping the battlefield) and **Deterministic Sanitization** (cleaning and extracting the data with zero-error tolerance).

Below is the documentation for the two core modules in this toolkit.

---

## 🕵️‍♂️ MODULE 1: Seer V3 (The Strategist Probe)

*Look Mom, I'm the Robin Hood of data! But more polite, compliant, and with better documentation.*

This is a lightweight Python Proof of Concept (PoC) designed to probe target websites, identify their underlying architecture (Next.js, React, VTEX, Static HTML), and recommend the optimal data extraction strategy before sending in the heavy artillery.

### 🎯 Where It Works Perfectly
- **Static HTML Sites:** E-commerce platforms built on legacy or server-rendered architectures.
- **Unprotected APIs:** Sites that carelessly leave their `application/json` endpoints exposed in the open.
- **Initial Reconnaissance:** Great for getting a quick map of the terrain before spending compute resources.

### 🛑 Where It Breaks (And Why)
I am an auditor. I don't hide my code's flaws; I document them. Here is the Red Team analysis of this PoC:

1. **The Akamai / Cloudflare Wall:** This script uses the standard `requests` library. Enterprise WAFs analyze the JA3 TLS fingerprint. They instantly recognize a Python script and block the connection. *(Fix: Swap to `curl_cffi` or use proxy networks).*
2. **The Ghost DOM (SPA):** The DOM density scanner relies on HTML tags. Modern React/Next.js sites send an empty `<div id="root"></div>`. Because `requests` cannot execute JS, the script sees an empty room. *(Fix: Headless Playwright grid).*
3. **The "Russian Roulette" Sampling Flaw:** The script picks *one* random URL to determine the tech stack. If it picks "Terms & Conditions", it falsely assumes the site is static HTML. *(Fix: Triangulate by sampling 3-5 distinct URLs).*
4. **The Pokemon Exception ("Gotta catch 'em all"):** A bare `try/except:` block can mask critical underlying system errors. *(Fix: Catch explicit exceptions like `KeyError`).*

---

## 🧠 MODULE 2: The Deterministic Sanitizer (OCR Extraction Engine)

**Extraction and Sanitization Architecture for Unstructured Data**

This is the actual heavy artillery. A Python-based logic engine designed to process, sanitize, and structure "dirty" or corrupted text streams coming from Optical Character Recognition (OCR) engines.

### ⚠️ The Problem
OCR tools (like Google ML Kit or Tesseract) frequently suffer from "hallucinations" (e.g., confusing the number `0` with the letter `O`) and capture garbage text from physical document margins. Standard extraction algorithms fail when facing this level of inconsistency.

### 🛠️ The Solution (Zero-Trust Logic)
I developed this engine based on **Zero-Trust** principles (never trust the raw data input). It uses advanced regular expressions (Regex) and exclusion dictionaries to achieve:

1. **Fault Tolerance:** Usage of *Lookaheads/Lookbehinds* to capture specific structures while ignoring surrounding noise.
2. **Hallucination Correction:** Proactive cleaning of mutated characters during runtime.
3. **White-Noise Filtering:** Implementation of dynamic *Blacklists* to discard headers, footers, and irrelevant metadata.

### 🚀 Impact
This logic serves as the core for larger financial data extraction and physical document auditing projects, ensuring that databases only receive clean, structured JSON payloads, effectively preventing system crashes due to corrupted data injection.

---

## 💼 The Tech Lead Disclaimer
*"Obviously, the Seer V3 is a lightweight 100-line PoC designed to be dependency-free. If we fire this at Akamai, our JA3 footprint gives us away in milliseconds. In production, we deploy the Swarm Protocol: stealth-plugin Playwright clusters and residential proxy rotation. But I'm not going to burn a $5/GB residential proxy just to push a clean demo to GitHub. We are data engineers, not vandals."*

**P.S.** To the recruiter or Tech Lead reading this until the very end: Keep in mind the probe (Module 1) is *just* how I map the battlefield. The actual heavy lifting—the deterministic parsing, OCR extraction, and data sanitization engines (Module 2) I use to clean, audit, and enforce 100% data integrity—is what makes this toolkit a complete, bulletproof data extraction pipeline.
