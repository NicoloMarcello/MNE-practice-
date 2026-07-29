import numpy as np
import mne 

print('MNE activated successfully')

sample_data_folder = mne.datasets.sample.data_path()    # get the path to the sample dataset
sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif" # get the path to the raw data file
)
raw = mne.io.read_raw_fif(sample_data_raw_file) # read the raw data file


print(raw)  # print the raw data object
print(raw.info)  # print the information about the raw data