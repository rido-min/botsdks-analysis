#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.join(os.getcwd(), 'reports', 'metrics')
OUT = os.path.join(os.getcwd(), 'reports', 'charts')
os.makedirs(OUT, exist_ok=True)

cloc_files = {
    'botbuilder': os.path.join(BASE, 'cloc_botbuilder.csv'),
    'agents': os.path.join(BASE, 'cloc_agents.csv'),
    'teamsnet': os.path.join(BASE, 'cloc_teamsnet.csv'),
    'coreteams': os.path.join(BASE, 'cloc_coreteams.csv'),
}

public_files = {
    'botbuilder': os.path.join(BASE, 'botbuilder_public_types.txt'),
    'agents': os.path.join(BASE, 'agents_public_types.txt'),
    'teamsnet': os.path.join(BASE, 'teams_public_types.txt'),
    'coreteams': os.path.join(BASE, 'core_teams_public_types.txt'),
}

def read_cloc_code(path):
    if not os.path.exists(path):
        return 0
    df = pd.read_csv(path)
    # sum C# rows (including generated)
    mask = df['language'].isin(['C#', 'C# Generated'])
    if mask.any():
        return int(df.loc[mask, 'code'].sum())
    # fallback: try to find first numeric code cell
    for v in df['code']:
        try:
            return int(v)
        except Exception:
            continue
    return 0

def count_public_types(path):
    if not os.path.exists(path):
        return 0
    with open(path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

codes = {k: read_cloc_code(p) for k, p in cloc_files.items()}
types = {k: count_public_types(public_files[k]) for k in public_files}

labels = ['botbuilder', 'agents', 'teamsnet', 'coreteams']
loc_values = [codes[l] for l in labels]
type_values = [types[l] for l in labels]

# LOC bar chart
plt.figure(figsize=(8,5))
plt.bar(labels, loc_values, color=['#2b7cff', '#2bbf7c', '#ffb74d', '#9e9e9e'])
plt.ylabel('Lines of Code (C#)')
plt.title('LOC by SDK')
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'loc_by_sdk.png'))
plt.close()

# Public types bar chart
plt.figure(figsize=(8,5))
plt.bar(labels, type_values, color=['#2b7cff', '#2bbf7c', '#ffb74d', '#9e9e9e'])
plt.ylabel('Public types (class/interface/struct/enum)')
plt.title('Public API Surface by SDK')
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'public_types_by_sdk.png'))
plt.close()

# Types per KLOC
types_per_kloc = []
for l in labels:
    loc = codes[l]
    t = types[l]
    if loc > 0:
        types_per_kloc.append(t / (loc/1000.0))
    else:
        types_per_kloc.append(0)

plt.figure(figsize=(8,5))
plt.bar(labels, types_per_kloc, color=['#2b7cff', '#2bbf7c', '#ffb74d', '#9e9e9e'])
plt.ylabel('Public types per KLOC')
plt.title('Public types density')
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'types_per_kloc.png'))
plt.close()

print('Charts written to:', OUT)
print('LOC:', codes)
print('Public types:', types)
