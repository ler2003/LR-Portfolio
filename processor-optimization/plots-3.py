import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from matplotlib.table import Table

csv_path = "F:/Spring2025/round3.csv"
df = pd.read_csv(csv_path)

sns.set(style="whitegrid")
plt.rcParams.update({'figure.max_open_warning': 0})

tests = df["Test"].unique()
benchmarks = df["Benchmark"].unique()
test_labels = df.drop_duplicates("Test").set_index("Test")["Predictor"].to_dict()
exclude = {"Test", "Predictor", "BTB", "BimodalTable", "Benchmark"}
metric_cols = [col for col in df.columns if col not in exclude and pd.api.types.is_numeric_dtype(df[col])]

num_metrics = len(metric_cols)
cols = 2
rows = math.ceil((num_metrics + 1) / cols)
fig, axs = plt.subplots(rows, cols, figsize=(16, 5 * rows))
axs = axs.flatten()
fig.suptitle("Round 3", fontsize=20, y=1.01)

for i, metric in enumerate(metric_cols):
    pivot = df.pivot(index="Test", columns="Benchmark", values=metric)
    pivot = pivot.loc[tests]
    pivot.plot(kind="bar", ax=axs[i])
    axs[i].set_title(metric.replace("_", " ").title(), fontsize=12)
    axs[i].set_ylabel(metric, fontsize=10)
    axs[i].tick_params(axis='x', labelsize=9)
    axs[i].tick_params(axis='y', labelsize=9)
    axs[i].set_xticklabels(pivot.index, rotation=0, fontsize=9)
    axs[i].legend(title="Benchmark", fontsize=8, title_fontsize=9)

key_ax = axs[num_metrics]
key_ax.axis("off")
table = Table(key_ax, bbox=[0, 0, 1, 1])

columns = ["Test", "Predictor", "BTB", "BimodalTable"]
rows = [
    ["A", "PredictNotTaken", "none", "none"],
    ["B", "Bimodal", "512entries", "512x4way"],
    ["C", "Perfect", "infinite", "infinite"],
]

for col_index, header in enumerate(columns):
    cell = table.add_cell(0, col_index, width=1/len(columns), height=0.2, text=header, loc='center', facecolor='#cccccc')
    cell.get_text().set_fontsize(12)

for row_index, row in enumerate(rows, start=1):
    for col_index, value in enumerate(row):
        cell = table.add_cell(row_index, col_index, width=1/len(columns), height=0.2,text=value, loc='center')
        cell.get_text().set_fontsize(12)

key_ax.add_table(table)

for j in range(num_metrics + 1, len(axs)):
    axs[j].axis("off")

plot_path = "Round3.png"
fig.tight_layout(pad=4.0)
plt.subplots_adjust(hspace=0.4)
fig.savefig(plot_path, bbox_inches="tight")


