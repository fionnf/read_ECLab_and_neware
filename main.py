import pandas as pd
import matplotlib as plt
import os
import NewareNDA as nda
from galvani import BioLogic
from datetime import timedelta
import datetime


def read_neware_data(ndax_file_path, theoretical_capacity):
    data = nda.read(ndax_file_path)
    cycle_numbers = data['Cycle'].unique()
    time_utc = pd.to_datetime(data['Timestamp'])
    min_time = time_utc.min()
    time_in_seconds = (time_utc - min_time).dt.total_seconds()

    grouped = data.groupby('Cycle')
    max_charge = grouped['Charge_Capacity(mAh)'].max()
    max_discharge = grouped['Discharge_Capacity(mAh)'].max()

    charge_capacity = (max_charge / theoretical_capacity) * 100
    discharge_capacity = (max_discharge / theoretical_capacity) * 100
    coulombic_efficiency = (max_discharge / max_charge) * 100

    processed_cycle_df = pd.DataFrame({
        'Cycle_Number': cycle_numbers,
        'Charge_Capacity': charge_capacity.reindex(cycle_numbers, fill_value=0),
        'Discharge_Capacity': discharge_capacity.reindex(cycle_numbers, fill_value=0),
        'Coulombic_Efficiency': coulombic_efficiency.reindex(cycle_numbers, fill_value=100),
        'Time': time_in_seconds.reindex(cycle_numbers, fill_value=0)
    })

    return processed_cycle_df


def process_eclab_mpr(mpr_file_path, theoretical_capacity):
    mpr_file = BioLogic.MPRfile(mpr_file_path)
    df = pd.DataFrame(mpr_file.data)
    df['Abs_Q_charge_discharge'] = df['Q charge/discharge/mA.h'].abs()
    df['Full_Cycle_Number'] = ((df['half cycle'] // 2) + 1).astype(int)

    is_charge = df['half cycle'] % 2 == 0
    is_discharge = ~is_charge

    max_charge = df[is_charge].groupby('Full_Cycle_Number')['Abs_Q_charge_discharge'].max()
    max_discharge = df[is_discharge].groupby('Full_Cycle_Number')['Abs_Q_charge_discharge'].max()
    charge_capacity = (max_charge / theoretical_capacity) * 100
    discharge_capacity = (max_discharge / theoretical_capacity) * 100
    coulombic_efficiency = (discharge_capacity / charge_capacity) * 100

    cycle_numbers = charge_capacity.index.union(discharge_capacity.index)

    time = df.groupby('Full_Cycle_Number')['time/s'].max()

    processed_cycle_df = pd.DataFrame({
        'Cycle_Number': cycle_numbers,
        'Charge_Capacity': charge_capacity.reindex(cycle_numbers, fill_value=0),
        'Discharge_Capacity': discharge_capacity.reindex(cycle_numbers, fill_value=0),
        'Coulombic_Efficiency': coulombic_efficiency.reindex(cycle_numbers),
        'Time': time.reindex(cycle_numbers, fill_value=0),
    })

    return processed_cycle_df


ndax_file_path = r"G:\.shortcut-targets-by-id\1gpf-XKVVvMHbMGqpyQS5Amwp9fh8r96B\RUG shared\Master Project\Thesis\Data Figures\Fig_MM_performance\FF042batt_a.ndax"
mpr_file_path = r"G:\.shortcut-targets-by-id\1gpf-XKVVvMHbMGqpyQS5Amwp9fh8r96B\RUG shared\Master Project\Thesis\Data Figures\Fig_MM_performance\FF068_nmr_a_C06.mpr"

neware_df = read_neware_data(ndax_file_path, theoretical_capacity=100)
eclab_df = process_eclab_mpr(mpr_file_path, theoretical_capacity=100)

print("Neware Data:")
print(neware_df)
print("\nEClab Data:")
print(eclab_df)