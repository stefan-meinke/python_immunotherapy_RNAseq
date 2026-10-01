from pathlib import Path
import GEOparse
import requests

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Downloading GEO dataset...")

# -----------------------------
# Download GEO metadata (SOFT)
# -----------------------------
print("Downloading SOFT metadata...")

gse = GEOparse.get_GEO(
    geo="GSE78220",
    destdir=str(DATA_DIR)
)

print("SOFT downloaded.")

# -----------------------------
# Download NCBI raw count matrix
# -----------------------------
url = (
    "https://www.ncbi.nlm.nih.gov/geo/download/"
    "?type=rnaseq_counts"
    "&acc=GSE78220"
    "&format=file"
    "&file=GSE78220_raw_counts_GRCh38.p13_NCBI.tsv.gz"
)

outfile = DATA_DIR / "GSE78220_raw_counts_GRCh38.p13_NCBI.tsv.gz"

if not outfile.exists():
    print("Downloading raw count matrix...")
    r = requests.get(url, stream=True)
    r.raise_for_status()

    with open(outfile, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    print("Count matrix downloaded.")
else:
    print("Count matrix already exists.")
