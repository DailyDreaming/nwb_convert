import os
from datetime import datetime
from dateutil import tz
from pathlib import Path
from neuroconv.datainterfaces import MaxOneRecordingInterface

file_path = '/home/ubuntu/2023-04-02-e-hc328_unperturbed/original/data/hc3.28_hckcr1_chip16835_plated34.2_rec4.2.raw.h5'
interface = MaxOneRecordingInterface(file_path=file_path, verbose=False)

metadata = interface.get_metadata()
# 2023-04-02T13:45:23
session_start_time = datetime(2023, 4, 2, 13, 45, 23, tzinfo=tz.gettz("US/Pacific"))
metadata["NWBFile"].update(session_start_time=session_start_time)

# Choose a path for saving the nwb file and run the conversion
nwbfile_path = 'final.nwb'
interface.run_conversion(nwbfile_path=nwbfile_path, metadata=metadata)
