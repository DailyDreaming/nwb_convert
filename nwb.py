"""Exploring an NWB file for some basic verification of its contents.  I may clean this up later."""

import matplotlib.pyplot as plt
import numpy as np

from pynwb import NWBHDF5IO

with NWBHDF5IO('final.nwb', mode='r', load_namespaces=True) as f:
    nwbfile = f.read()
    #print(dir(nwbfile))
    #print(nwbfile)
    print(nwbfile.fields)
    print('\n\n')
    #print(nwbfile.electrodes.gain_to_uV[()])
    print(nwbfile.electrodes.to_dataframe()[:5])
    print(nwbfile.acquisition["ElectricalSeries"].data[:5])
#    print(dir(nwbfile.acquisition["ElectricalSeries"]))
    print(nwbfile.acquisition["ElectricalSeries"].fields)
    print(nwbfile.acquisition["ElectricalSeries"].DEFAULT_CONVERSION)
    print(nwbfile.acquisition["ElectricalSeries"].data.dtype)
    #print(nwbfile.processing["ecephys"]["LFP"]["ElectricalSeries"].data[:])
    #units = nwbfile.units
    #print(units["spike_times"][0])
    #units_df = units.to_dataframe()
    #print(units_df.head())
    #print(units_df.tail())
