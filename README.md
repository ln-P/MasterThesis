# Research Master Thesis Project

Maastricht University research thesis project aiming to quantify differences in the banking competition publications, between **central bank** and **university** economists.

Current dataset consists of 69 economic articles, of which:
 - **15** are affiliated to various **central banks** (authors are employed by CB)
 - **54** are written by **university or public organisations** researchers

### Methods used:
- `Natural Language Processing`
    - `Cosine similarity`
    - `Hierarchical clustering`
    - Topic models: `Latent Semantic Indexing`
    - `K-means` clustering on LSA components


- `Reported statistics analysis`
    - reviewing reported `p-values` and `t-statistics` to determine if Central Bank researcher show tendency to commit `Type II Error` more frequently


### Competition models covered:
- `Panzar-Rosse:` H-static

### Intermediate Results:


#### `K-means` on LSA components
- `∇` correspond to central bank paper
- Colours show corresponding class

![Kmeans LSA](/Analysis/Graphs/kmeans_10.png)

#### `Heatmap` using cosine similarity on tfidf vector pairs

![Cosine similarity](/Analysis/Graphs/heatmap.png)

### Reported statistics analysis

#### Statistics distributions

![P-values distribution](/Analysis/Graphs/dist_pvalue.png)
![T-statistics distribution](/Analysis/Graphs/dist_tstat.png)

#### H-statistics overview
