"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        
    def load_inflammation_data(data_dir):
        data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation csv's found in path {data_dir}")
        data = map(models.load_csv, data_file_paths)
        return data
    
class JSONDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        
    def load_inflammation_data(data_dir):
        data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation csv's found in path {data_dir}")
        data = map(models.load_json, data_file_paths)
        return data

def load_inflammation_data(dir_path):
  data_file_paths = glob.glob(os.path.join(dir_path, 'inflammation*.csv'))
  if len(data_file_paths) == 0:
      raise ValueError(f"No inflammation csv's found in path {dir_path}")
  data = map(models.load_csv, data_file_paths)
  return list(data)

def compute_standard_deviartion_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0) # Calculate Standard Deviation by day
    return daily_standard_deviation # Return Standard deviation

def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets
    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
       
    data = CSVDataSource.load_inflammation_data(data_dir)
    daily_standard_deviation = compute_standard_deviartion_by_day(data)
    return daily_standard_deviation


