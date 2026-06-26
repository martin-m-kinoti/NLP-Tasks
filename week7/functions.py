class DataCheck():
    def __init__(self, df):
        self.data = df
    
    def miss_data(self):
        self.missing_data = self.data.isna().sum()
        return print("Missing data: ", self.missing_data)

    def dup_data(self):
        self.dup = self.data.duplicated().sum()
        return print("Duplicates: ", self.dup)