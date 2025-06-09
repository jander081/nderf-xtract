# ndrfxtract

A toolkit and dataset for analyzing near-death experience (NDE) accounts, with a focus on soul trap theory and other interpretive models.  
Source data is collected from the [Near-Death Experience Research Foundation (NDRF)](https://www.nderf.org/).

## Project Structure

- `data/raw/` — Original NDE text files (one per account)
- `data/processed/` — Cleaned or annotated data
- `notebooks/` — Jupyter notebooks for analysis and exploration
- `src/` — Python modules for loading, parsing, and feature extraction

## Quickstart

1. **Clone the repo and set up the environment:**
   ```bash
   conda env create -f environment.yml
   conda activate ndrfxtract



ndrfxtract/
│
├── data/
│   ├── raw/                 # Your original .txt files (one per NDE)
│   └── processed/           # Cleaned, parsed, or annotated files
│
├── notebooks/
│   └── 01-explore-data.ipynb
│
├── src/
│   ├── __init__.py
│   ├── load_nde.py          # Functions for loading/cleaning NDE text files
│   └── extract_features.py  # (Future) Feature extraction functions
│
├── environment.yml
├── requirements.txt
├── README.md
└── .gitignore


# Install Ollama if you haven't
brew install ollama

# Start Ollama
% ollama serve
<!--  or -->
% OLLAMA_FLASH_ATTENTION="1" OLLAMA_KV_CACHE_TYPE="q8_0" ollama serve

# Pull a model (e.g., Llama 3)
<!-- Open a new terminal tab (don’t stop the ollama serve), and run: -->
% ollama pull llama3
<!-- or -->
% ollama pull mistral

<!-- query from cmd line -->
% ollama run llama3
>>> Extract key facts from this text: My dog Max is a bulldog and likes to sleep all day.