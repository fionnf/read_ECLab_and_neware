import import_data
import numpy as np
import matplotlib.pyplot as plt


def plot_combined_capacity(dataframes, labels, min_cycle=None, max_cycle=None, styles=None, save_image=False, save_path='combined_cap.png'):
    if styles is None:
        styles = {
            'figure_size': (10, 8),
            'scatter_size': 10,
            'axis_label_fontsize': 14,
            'tick_label_fontsize': 12,
            'legend_fontsize': 12
        }

    fig, ax = plt.subplots(figsize=styles.get('figure_size', (10, 8)))
    ax.set_xlabel('Cycle Number', fontsize=styles.get('axis_label_fontsize', 14))
    y_label = 'Capacity (%)'
    ax.set_ylabel(y_label, fontsize=styles.get('axis_label_fontsize', 14))

    # Define max and min cycle across all dataframes for consistent axis scaling
    global_max_cycle = 0
    global_min_cycle = float('inf')

    # Filter and process each DataFrame
    filtered_data = []
    for df in dataframes:
        if min_cycle is not None:
            df = df[df['Cycle_Number'] >= min_cycle]
        if max_cycle is not None:
            df = df[df['Cycle_Number'] <= max_cycle]

        filtered_data.append(df)
        global_max_cycle = max(global_max_cycle, df['Cycle_Number'].max())
        global_min_cycle = min(global_min_cycle, df['Cycle_Number'].min())

    # Plotting the filtered data
    for df, label in zip(filtered_data, labels):
        ax.scatter(df['Cycle_Number'], df['Charge_Capacity'], label=label, s=styles.get('scatter_size', 10))

    ax.set_ylim(0, max(df['Charge_Capacity'].max() for df in filtered_data) * 1.1)
    ax.set_xlim(global_min_cycle, global_max_cycle)

    ax.legend(loc='best', fontsize=styles.get('legend_fontsize', 12))
    plt.tight_layout()

    if save_image:
        plt.savefig(save_path, dpi=600)

    plt.show()

    return fig

df1 = import_data.process_eclab_mpr(r"G:\.shortcut-targets-by-id\1gpf-XKVVvMHbMGqpyQS5Amwp9fh8r96B\RUG shared\Master Project\Thesis\Data Figures\Fig_MM_performance\FF068_nmr_a_C06.mpr",theoretical_capacity=1.8)
df2 = import_data.process_neware_data(r"G:\.shortcut-targets-by-id\1gpf-XKVVvMHbMGqpyQS5Amwp9fh8r96B\RUG shared\Master Project\Thesis\Data Figures\Fig_MM_performance\FF042batt_a.ndax", theoretical_capacity=0.7)
df3 = import_data.process_neware_data(r"G:\.shortcut-targets-by-id\1gpf-XKVVvMHbMGqpyQS5Amwp9fh8r96B\RUG shared\Master Project\Thesis\Data Figures\Fig_MM_performance\FF054Batta.ndax",theoretical_capacity=0.68)
plot_combined_capacity([df1, df2,df3], ['Neware Data','clab','boi'], min_cycle=1, max_cycle=50)