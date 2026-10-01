from pathlib import Path
import pandas as pd
import GEOparse

RAW = Path("data/raw")
# PROCESSED = Path("data/processed")
# PROCESSED.mkdir(parents=True, exist_ok=True)

gse = GEOparse.get_GEO(filepath=str(RAW / "GSE78220_family.soft.gz"))

rows = []

for gsm_id, gsm in gse.gsms.items():
    row = {"sample": gsm_id}

    # Flatten GEO metadata dictionary
    for key, value in gsm.metadata.items():
        if isinstance(value, list):
            row[key] = " | ".join(value)
        else:
            row[key] = value

    rows.append(row)

metadata = pd.DataFrame(rows)

metadata.to_csv(RAW / "metadata_raw.csv", index=False)

print(metadata.shape)
print(metadata.columns.tolist())