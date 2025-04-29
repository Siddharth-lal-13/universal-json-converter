# 🔄 Universal JSON Converter CLI

> Convert files to/from JSON effortlessly — with streaming support for large datasets! 🚀📈

<p align="center">
  <img src="https://raw.githubusercontent.com/Siddharth-lal-13/universal-json-converter/main/logo.png" width="250" />
</p>

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)
![File Size Limit](https://img.shields.io/badge/Max%20File%20Size-Unlimited-success)
[![PyPI version](https://badge.fury.io/py/universal-json-converter.svg)](https://badge.fury.io/py/universal-json-converter)
![Stars](https://img.shields.io/github/stars/Siddharth-lal-13/universal-json-converter?style=social)

---

## ✨ Features

✅ Supports **bi-directional conversion**:
- `.csv`, `.jsonl`, `.xml`, `.xlsx`, `.yaml`, `.parquet` ➜ `.json`
- `.json` ➜ `.csv`, `.jsonl`, `.xlsx`, `.yaml`, `.parquet`

🧠 Optimized for **large files** with:
- Streaming (for JSONL)
- Chunked processing (for CSV & Excel)

💪 **No file size limits** — convert files of **gigabytes or even terabytes** as long as your hardware supports it.

🔧 Built as a lightweight **CLI tool** — no GUI needed

📂 Easy folder management & file safety

📦 Installable via pip or GitHub repo

---

## 🔧 Installation Guide

### 📦 Option 1: Install via pip (Recommended)
```bash
pip install universal-json-converter
```
Then run it from any terminal:
```bash
ujconvert tojson yourfile.csv output_folder/
```

> 💡 Make sure your Python is version 3.7 or above.

---

### 🖥 Option 2: Run from GitHub (Developer Mode)

### 🖥 Windows / macOS / Linux

#### 1. Clone the Repository:
```bash
git clone https://github.com/your-username/universal-json-converter.git
cd universal-json-converter
```

#### 2. Install Requirements:
```bash
pip install -r requirements.txt
```

#### 3. Run from terminal:
```bash
python main.py tojson path/to/input.csv output_folder/
```

> 🧠 This mode is great for editing or contributing to the tool.

---

## 💻 CLI Usage

### 🔄 Convert TO JSON
```bash
ujconvert tojson path/to/input_file.csv output_folder/
```

### 🔁 Convert FROM JSON
```bash
ujconvert fromjson path/to/input_file.json path/to/output_file.csv csv
```

📌 Supported formats: `csv`, `jsonl`, `yaml`, `xls`, `xlsx`, `parquet`

---

## 🧠 Practical Applications

This tool is perfect for:

📊 **Data Science & Machine Learning**
- Preprocessing raw CSV/Excel/JSONL data to feed into ML models
- Generating JSON configs and structured logs

🔍 **Big Data Analytics**
- Handling multi-GB to **terabyte-scale** files using chunking or streaming

📁 **Data Engineering**
- Simplifying ingestion pipelines with standard formats

🧪 **ETL Automation**
- Format normalization in scripts and cron jobs

📈 **Visualization & Dashboards**
- Easy input conversion for tools like Plotly, Dash, and Streamlit

---

## ❤️ Support & Customization

This tool is open source and free to use, but if you'd like:
- A custom version for your organization
- A web GUI/API integration
- Help integrating it into your data pipeline

📩 **Email me at:** [siddharthlal99@gmail.com](mailto:siddharthlal99@gmail.com)

---

## 🌍 Share & Credit

If you use this project, please ⭐ it on GitHub and link to:
- [GitHub](https://github.com/Siddharth-lal-13/universal-json-converter)
- [LinkedIn](https://www.linkedin.com/in/siddharth-lal13)

```text
Built using Universal JSON Converter by Siddharth Lal
https://github.com/Siddharth-lal-13/universal-json-converter
```

---

## 📄 License

This project is licensed under the **Apache License 2.0**.

You are free to use, modify, and distribute this software, provided that proper credit is given and a copy of the NOTICE file is included with redistributions.

For full license details, see the [LICENSE](https://github.com/Siddharth-lal-13/universal-json-converter/blob/main/LICENSE) file.

> Please give credit if you use it publicly. For commercial licensing or collaboration, email me.

---

## 👤 Author

**Developed by Siddharth Lal**
- Email: [siddharthlal99@gmail.com](mailto:siddharthlal99@gmail.com)
- GitHub: [Siddharth-lal-13](https://github.com/Siddharth-lal-13)
- LinkedIn: [Siddharth Lal](https://www.linkedin.com/in/siddharth-lal13)

🤝 I'm open to collaboration, internships, remote freelance/contract and research work!

