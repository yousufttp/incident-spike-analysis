# 🚀 Incident Clustering Improvement Prompts (GitHub Copilot)

## 📌 Context (Read Once)

You are improving an incident clustering system.

### Current Problem

* Clusters are too broad
* One cluster contains multiple functional groups
* Example: activation + billing + provisioning grouped together

### Goal

* Group incidents by **operational / functional category**
* Each cluster should map to **one clear business function**
* If a cluster is mixed → it must be **split further**

---

# 🧠 PROMPT 1 — FULL PIPELINE REDESIGN

```
I have an incident clustering pipeline that is currently producing very coarse clusters. 
Each cluster contains multiple functional groups, which is not useful for operations.

I want you to redesign this pipeline so that incidents are grouped by operational function, not just semantic similarity.

Requirements:
1. Use both short description and detailed description as input
2. Perform strong preprocessing:
   - lowercase
   - remove noise words (issue, error, unable, customer, etc.)
   - normalize domain-specific synonyms
3. Add a configurable synonym dictionary (e.g. activation, billing, provisioning, network, port, access, device)
4. Use a hybrid feature approach:
   - TF-IDF or similar keyword-based features
   - optional embeddings if needed
5. Replace one-step clustering with a two-stage approach:
   - Stage 1: broad clustering (high-level themes)
   - Stage 2: sub-clustering within each group
6. Add logic to detect mixed clusters and split them further
7. Generate human-readable labels for each final cluster using top keywords
8. Output:
   - cluster id
   - label
   - incident count
   - top keywords
   - 5 sample incidents
9. Keep implementation practical and explainable (no overly academic solutions)

Explain the design before showing code.
Then provide clean Python implementation.
```

---

# 🧠 PROMPT 2 — IMPROVE EXISTING TF-IDF + KMEANS

```
My current implementation uses TF-IDF and KMeans clustering on incident descriptions.

Problem:
Clusters are too broad and mix different functional issues together.

Please improve the existing approach without completely rewriting it:

1. Enhance preprocessing:
   - remove generic telecom noise words
   - normalize synonyms using a dictionary
2. Improve feature quality:
   - adjust TF-IDF parameters (ngram range, min_df, max_df)
3. Improve clustering:
   - increase granularity
   - avoid forcing small number of clusters
4. Add second-stage clustering:
   - re-cluster large clusters into smaller functional groups
5. Add cluster labeling:
   - use top TF-IDF terms
6. Print representative samples per cluster

Explain each improvement and why it helps functional grouping.
```

---

# 🧠 PROMPT 3 — DOMAIN NORMALIZATION LAYER

```
Add domain-specific normalization to my incident processing pipeline.

Implement:
1. A synonym dictionary like:
   - esim, e-sim → esim
   - activate, activation → activation
   - bill, billing, charged → billing
   - provision, provisioning → provisioning
   - port, port-in → port
   - no signal, no service → network
   - login issue, cannot login → access

2. A preprocessing function that:
   - replaces synonyms
   - standardizes vocabulary
   - removes noise words

3. Make the dictionary easily extendable

Show how this integrates before feature extraction.
```

---

# 🧠 PROMPT 4 — DETECT & SPLIT MIXED CLUSTERS

```
I need to detect clusters that are too broad or mixed.

Add logic to:
1. Measure cluster quality using:
   - keyword diversity
   - intra-cluster similarity
   - cluster size
2. Flag clusters that are too mixed
3. Automatically re-cluster those clusters into smaller subgroups

Keep logic simple and explainable.

Also print before/after comparison of cluster quality.
```

---

# 🧠 PROMPT 5 — BUSINESS-FRIENDLY OUTPUT

```
Improve the output format of the clustering system for business users.

For each cluster, show:
- Cluster ID
- Cluster Label
- Incident Count
- Top Keywords
- 5 Representative Incidents
- Optional cohesion score

Output should be readable as a pandas DataFrame or structured report.

Make it easy for a manager to validate clusters quickly.
```

---

# 🧠 PROMPT 6 — ARCHITECTURE REVIEW (SMART MODE)

```
Act as a senior ML engineer reviewing my clustering pipeline.

Problem:
Clusters are too broad and not aligned with operational categories.

Context:
- Input is messy incident text
- Categories are unreliable
- Need business-aligned grouping
- Simplicity + explainability required

Evaluate these approaches:
- TF-IDF + KMeans
- hierarchical clustering
- hybrid (rules + ML)
- LLM-assisted labeling

Recommend the best approach and update the code accordingly.

Focus on practical implementation.
```

---

# 🧠 PROMPT 7 — LABEL GENERATION IMPROVEMENT

```
My cluster labels are too generic.

Improve labeling logic so labels reflect:
- actual operational function
- not generic words like issue, error

Use:
- top TF-IDF keywords
- or simple rule-based naming

Ensure labels are meaningful like:
- "eSIM activation failure"
- "billing charge dispute"
- "network signal loss"

Show implementation.
```

---

# 🧠 PROMPT 8 — GRANULARITY CONTROL

```
My clustering is too coarse.

Improve granularity by:
- increasing number of clusters
- avoiding merging unrelated issues
- balancing cohesion vs separation

Suggest parameter tuning and logic changes.

Goal:
Each cluster should represent a single functional issue type.
```

---

# 🧠 PROMPT 9 — VALIDATION HELPER

```
Add validation support to the clustering pipeline.

For each cluster:
- randomly sample 5–10 incidents
- print them clearly

This helps manual verification of cluster quality.

Implement helper function.
```

---

# 🔥 FINAL REMINDER (VERY IMPORTANT)

Always optimize for:

"Operational/function-level grouping, not broad semantic similarity."

And:

"A good cluster should map to one functional team/process."

---
