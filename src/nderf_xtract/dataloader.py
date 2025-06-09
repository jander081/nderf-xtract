# src/nderf_xtract/dataloader.py

import os

def load_nde_files(data_dir='data/raw'):
    nde_texts = {}
    for fname in os.listdir(data_dir):
        if fname.endswith('.txt'):
            with open(os.path.join(data_dir, fname), 'r', encoding='utf-8') as f:
                nde_texts[fname] = f.read()
    return nde_texts

if __name__ == '__main__':
    texts = load_nde_files()
    print(f"Loaded {len(texts)} files. Sample keys: {list(texts.keys())[:3]}")
    print("\nSample text:\n", texts[list(texts.keys())[0]][:500])  # Show first 500 chars of one