from datetime import datetime
from dateutil import tz
from pathlib import Path

from neuroconv.datainterfaces import KiloSortSortingInterface

folder_path = f"2023-04-02-e-hc328_unperturbed/derived/kilosort2/curated_s1"
# Change the folder_path to the location of the data in your system
interface = KiloSortSortingInterface(folder_path=folder_path, verbose=False)

metadata = interface.get_metadata()
session_start_time = datetime(2020, 1, 1, 12, 30, 0, tzinfo=tz.gettz("US/Pacific"))
metadata["NWBFile"].update(session_start_time=session_start_time)
nwbfile_path = "kilosort.nwb"  # This should be something like: "./saved_file.nwb"
interface.run_conversion(nwbfile_path=nwbfile_path, metadata=metadata)
