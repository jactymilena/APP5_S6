import pandas as pd
from datetime import datetime


class Database:

    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)


    def update(self, uuid, column, new_val):
        for i in range(len(self.data)):
            if self.data.loc[i, 'uuid'] == uuid:
                self.data.loc[i, column] = new_val

        self.data.to_csv(self.filename, index=False)


    def get_by_column(self, column):
        rows = []
        for i in range(len(self.data)):
            rows.append(data.loc[i, column]) 

        return rows

        





