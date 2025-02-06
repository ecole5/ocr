# Document Processing with Cloudera Private AI

This repository demonstrates how to extract text from PDFs using both classical OCR techniques (Tesseract) and locally running vision-based LLMs (Ollama) on Cloudera AI. It provides ready-to-use runtime images for deployment in the Cloudera AI Workbench.

## 🚀 Quick Start

### 1. Import Runtime Images
Two runtime images are available for use in Cloudera AI Workbench:

- **Ollama Runtime:** `docker.io/ecole5/ollama:v1`
- **Tesseract Runtime:** `docker.io/ecole5/tesseract:v1`

Alternatively, you can build the Tesseract image yourself using the provided `Dockerfile` in this repository.

For Ollama, if you want to build yourself use the Cloudera Community ML Runtime files available here:  
🔗 [Cloudera Community ML Runtime - Ollama](https://github.com/cloudera/community-ml-runtimes/tree/main/ollama)

### 2. Running the Scripts
Each runtime is optimized for a specific script:

- **Ollama Runtime** → Run `tesseract.py`
- **Tesseract Runtime** → Run `ocr.py`

### 3. Using a Commercial LLM for Text Extraction
For those interested in extracting text using a commercial LLM, you can import the community AMP:

🔗 [Cloudera AMP - Image Analysis with Anthropic Claude](https://github.com/cloudera/CML_AMP_Image-Analysis-with-Anthropic-Claude)

---

## 📌 Installation & Usage

1. Clone the repository into your workbench:
   ```sh
   git clone https://github.com/ecole5/ocr
   ```
2. Build the Tesseract image (if not using the prebuilt one):
   ```sh
   docker build -t tesseract:v1 -f Dockerfile .
   ```
3. Run the appropriate script within its respective runtime in workbench.

## 🛠 Requirements
- **Docker** (if building locally)
- **Cloudera AI Workbench**

## 📖 Additional Resources
- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract)
- [Ollama - Cloudera ML Runtime](https://github.com/cloudera/community-ml-runtimes/tree/main/ollama)
- [Cloudera AI Workbench](https://docs.cloudera.com/machine-learning/1.5.4/index.html)

---
