import pandas as pd
from datetime import datetime


class Database:

    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)



    def update(self, uuid, columnm, new_val):
        print("test")
        for i in len(data):
            if data.loc[i, 'uuid'] == uuid:
                data.loc[i, column] = new_val

        df.to_csv(self.filename, index=False)
        





