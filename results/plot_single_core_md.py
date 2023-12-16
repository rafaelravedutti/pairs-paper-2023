import matplotlib.pyplot as plt
import numpy as np

data = {
    'Ice Lake': {
        'P4IRS FN': {'Total': 27.2551, 'Force': 23.216, 'Neighbor': 3.59287},
        'MD-Bench FN': {'Total': 25.71, 'Force': 20.89, 'Neighbor': 4.68},
        'P4IRS HN': {'Total': 16.077, 'Force': 12.3325, 'Neighbor': 3.29793},
        'MD-Bench HN': {'Total': 16.44, 'Force': 12.25, 'Neighbor': 4.00},
    },
    'Milan': {
        'P4IRS FN': {'Total': 28.8791, 'Force': 24.366, 'Neighbor': 4.121},
        'MD-Bench FN': {'Total': 29.7, 'Force': 24.24, 'Neighbor': 5.3},
        'P4IRS HN': {'Total': 19.3626, 'Force': 15.431, 'Neighbor': 3.54197},
        'MD-Bench HN': {'Total': 19.18, 'Force': 14.77, 'Neighbor': 4.22},
    },
}

architectures = list(data.keys())
benchmarks = list(data[architectures[0]].keys())

# Prepare data for plotting
bar_width = 0.35
bar_positions_ice_lake = np.arange(len(benchmarks))
bar_positions_milan = bar_positions_ice_lake + bar_width + 0.1  # Adding a small gap between groups

fig, ax = plt.subplots(figsize=(15, 8))

for i, (architecture, bar_positions) in enumerate(zip(architectures, [bar_positions_ice_lake, bar_positions_milan])):
    bottom = np.zeros(len(benchmarks))
    for j, region in enumerate(['Force', 'Neighbor', 'Other']):
        values = [data[architecture][benchmark].get(region, 0) for benchmark in benchmarks]
        ax.bar(
            bar_positions + j * bar_width,
            values,
            bar_width,
            label=f'{architecture} - {region}',
            bottom=bottom,
        )
        bottom += np.array(values)

ax.set_xlabel('Benchmark')
ax.set_ylabel('Time (s)')
ax.set_title('Performance Comparison by Architecture and Region')
ax.set_xticks(bar_positions_ice_lake + bar_width / 2)
ax.set_xticklabels(benchmarks)
ax.legend()

plt.show()
