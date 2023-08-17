"""
https://pynwb.readthedocs.io/en/stable/tutorials/general/plot_file.html
"""
from datetime import datetime

from uuid import uuid4

import numpy as np
from dateutil import tz

from pynwb import NWBHDF5IO, NWBFile, TimeSeries
from pynwb.behavior import Position, SpatialSeries
from pynwb.epoch import TimeIntervals
from pynwb.file import Subject

session_start_time = datetime(2018, 4, 25, 2, 30, 3, tzinfo=tz.gettz("US/Pacific"))

nwbfile = NWBFile(
    session_description="Mouse exploring an open field",  # required
    identifier=str(uuid4()),  # required
    session_start_time=session_start_time,  # required
    session_id="session_1234",  # optional
    experimenter=[
        "Baggins, Bilbo",
    ],  # optional
    lab="Bag End Laboratory",  # optional
    institution="University of My Institution",  # optional
    experiment_description="I went on an adventure to reclaim vast treasures.",  # optional
    related_publications="DOI:10.1016/j.neuron.2016.12.011",  # optional
)
print(nwbfile)

with NWBHDF5IO("basics_tutorial.nwb", "w") as io:
    io.write(nwbfile)
