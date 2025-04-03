import import_data
import numpy as np
import matplotlib.pyplot as plt


def plot_combined_capacity(dataframes, labels, min_cycle=None, max_cycle=None, styles=None, save_image=False, save_path='combined_cap.png'):
    if styles is None:
        styles = {
            'figure_size': (10, 8),
            'scatter_size': 18,
            'axis_label_fontsize': 20,
            'tick_label_fontsize': 20,
            'legend_fontsize': 20
        }

    fig, ax = plt.subplots(figsize=styles.get('figure_size', (10, 8)))
    ax.set_xlabel('Cycle Number', fontsize=styles.get('axis_label_fontsize', 20))
    y_label = 'Normalized Capacity (%)'
    ax.set_ylabel(y_label, fontsize=styles.get('axis_label_fontsize', 20))
    ax.tick_params(axis='x', labelsize=styles['tick_label_fontsize'], top=True, direction='in')
    ax.tick_params(axis='y', labelsize=styles['tick_label_fontsize'], right=True, direction='in')

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

    ax.set_ylim(0, max(df['Charge_Capacity'].max() for df in filtered_data) * 1.05)
    ax.set_xlim(global_min_cycle, global_max_cycle)

    ax.legend(loc='best', fontsize=styles.get('legend_fontsize', 20))
    plt.tight_layout()

    if save_image:
        plt.savefig(save_path, dpi=600)

    plt.show()

    return fig

df1 = import_data.process_eclab_mpr('/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/.shortcut-targets-by-id/1crKxRhkNlojWYYDvrhlOSLdwhg3iId2A/manuscript Blatter-OCF3 in-situ NMR/battery cycling/H-cell/JSS296 - BlatterCF3 - 3a - Long/EC-LAB-Files/JSS296_20201215_GCPLa.mpr', theoretical_capacity=1.5)
df2 = import_data.process_neware_data('/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/.shortcut-targets-by-id/1crKxRhkNlojWYYDvrhlOSLdwhg3iId2A/manuscript Blatter-OCF3 in-situ NMR/battery cycling/H-cell/MS020c.ndax', theoretical_capacity=0.52)
df3 = import_data.process_neware_data('/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/.shortcut-targets-by-id/1crKxRhkNlojWYYDvrhlOSLdwhg3iId2A/manuscript Blatter-OCF3 in-situ NMR/battery cycling/H-cell/MS019c.ndax', theoretical_capacity=0.53)
df4 = import_data.process_neware_data('/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/.shortcut-targets-by-id/1crKxRhkNlojWYYDvrhlOSLdwhg3iId2A/manuscript Blatter-OCF3 in-situ NMR/battery cycling/H-cell/MS022b.ndax', theoretical_capacity=0.53)

plot_combined_capacity([df1, df2, df3, df4], ['Unsubstituted', 'p-OCF3', 'o-ocf3', "m-ocf3"], min_cycle=1, max_cycle=250, save_image=True, save_path='/Users/fionnferreira/PycharmProjects/read_ECLab_and_neware/combined_cap.png')