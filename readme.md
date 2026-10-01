# RNA-seq Analysis of Anti-PD-1 Response

## Objective

Identify transcriptional signatures associated with response to anti-PD-1 therapy using bulk RNA-seq data from the publicly available GEO dataset **GSE78220**.

## Dataset

This analysis uses the publicly available GEO dataset:

* **GEO accession:** GSE78220
* **Title:** *mRNA expressions in pre-treatment melanomas undergoing anti-PD-1 checkpoint inhibition therapy*
* **Organism:** *Homo sapiens*
* **Samples:** 28 melanoma samples
* **Data type:** Bulk RNA-seq

The dataset is publicly available through the NCBI Gene Expression Omnibus (GEO), with raw sequencing data available through SRA and processed expression data available on the GEO series record.

The original dataset is not included in this repository. The data are downloaded programmatically using:

* `scripts/01_download_dataset.py` — downloads the required expression data
* `scripts/02_parse_metadata.py` — extracts and processes the sample metadata

## Workflow

1. Download GEO dataset
2. Parse sample metadata
3. Quality control
4. Normalization
5. PCA and clustering
6. Differential expression analysis
7. Over-representation analysis (ORA)
8. Gene set enrichment analysis (GSEA)

## Repository Structure

```text
python_immunotherapy/
│
├── scripts/
│   ├── 01_download_dataset.py
│   └── 02_parse_metadata.py
│
├── notebooks/
│   └── immunotherapy_analysis.ipynb
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── readme.md
│
├── results/
│   ├── figures/
│   └── tables/
│
├── environment.yaml
├── README.md
└── .gitignore
```

Generated data, figures, and tables are written to the `data/` and `results/` directories as described in the analysis workflow.

## Reference
The original data are available from NCBI GEO:

https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE78220

and Hugo *et al.* ([Cell, 2016](https://pubmed.ncbi.nlm.nih.gov/26997480/))

````
