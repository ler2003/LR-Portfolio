import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.table import Table

csv_path = "F:/Spring2025/round1_all.csv"
df = pd.read_csv(csv_path)

sns.set(style="whitegrid")
plt.rcParams.update({'figure.max_open_warning': 0})

fig, axs = plt.subplots(6, 1, figsize=(14, 36))
fig.tight_layout(pad=5.0)
fig.suptitle("Round 1", fontsize=20, y=1.02)

tests = df["Test"]
benchmarks = ["Bzip2", "mcf", "hmmer", "sjeng", "milc", "equake"]

ipc_data = df[[f"sim_IPC_{b}" for b in benchmarks]]
ipc_data.index = tests
ipc_data.plot(kind="bar", ax=axs[0])
axs[0].set_title("Sim IPC")
axs[0].set_ylabel("sim_IPC")
axs[0].legend(title="Benchmark")

cycle_data = df[[f"sim_cycle_{b}" for b in benchmarks]]
cycle_data.index = tests
cycle_data.plot(kind="bar", ax=axs[1])
axs[1].set_title("Sim cycle")
axs[1].set_ylabel("sim_cycle")
axs[1].legend(title="Benchmark")

slip_data = df[[f"avg_sim_slip_{b}" for b in benchmarks]]
slip_data.index = tests
slip_data.plot(kind="bar", ax=axs[2])
axs[2].set_title("Avg sim slip")
axs[2].set_ylabel("avg_sim_slip")
axs[2].legend(title="Benchmark")

ruu_lat_data = df[[f"ruu_latency_{b}" for b in benchmarks]]
ruu_lat_data.index = tests
ruu_lat_data.plot(kind="bar", ax=axs[3])
axs[3].set_title("RUU latency")
axs[3].set_ylabel("ruu_latency")
axs[3].legend(title="Benchmark")

ruu_full_data = df[[f"ruu_full_{b}" for b in benchmarks]]
ruu_full_data.index = tests
ruu_full_data.plot(kind="bar", ax=axs[4])
axs[4].set_title("RUU full")
axs[4].set_ylabel("ruu_full")
axs[4].legend(title="Benchmark")

axs[5].axis("off")
table = Table(axs[5], bbox=[0, 0, 1, 1])
columns = ["Test", "Type", "Width", "In-order"]
rows = [
    ["A", "Baseline", "1", "true"],
    ["B", "Static Superscalar", "2", "true"],
    ["C", "Dynamic Superscalar", "2", "false"],
    ["D", "Static Superscalar", "4", "true"],
    ["E", "Dynamic Superscalar", "4", "false"]
]

for col_index, header in enumerate(columns):
    table.add_cell(0, col_index, width=1/len(columns), height=0.15, text=header, loc='center', facecolor='#cccccc')

for row_index, row in enumerate(rows, start=1):
    for col_index, cell_value in enumerate(row):
        table.add_cell(row_index, col_index, width=1/len(columns), height=0.15, text=cell_value, loc='center')

axs[5].add_table(table)
plot_with_key_path = "Round1.png"
fig.savefig(plot_with_key_path, bbox_inches='tight')
plot_with_key_path
