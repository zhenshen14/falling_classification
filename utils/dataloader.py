import pandas as pd
import numpy as np
import re



class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    # apply regex
    def get_title(self, name):
        pattern = ' ([A-Za-z]+)\.'
        title_search = re.search(pattern, name)
        # If the title exists, extract and return it.
        if title_search:
            return title_search.group(1)
        return ""

    def load_data(self):

        # drop columns
        self.dataset = self.dataset.drop(['SL', 'EEG'], axis=1)

        return self.dataset
