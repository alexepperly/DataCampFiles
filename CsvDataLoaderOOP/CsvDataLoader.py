
## This is my attempt to replicate the same csv loader I had on my dev computer, but instead make an OOP thing out of it

import pandas as pd
import sqlalchemy as sa

## Noun, so good here
class CsvLoader:
    def __init__(self, filepath, target_database, target_table):
        self.filepath = filepath  # ? How do I ensure that these are specific datatypes 
        self.target_database = target_database
        self.target_table = target_table
        
    def get_csv(self):
        self.df = pd.read_csv(self.filepath) # ? How do I make sure this is accessible outside the function
        print(self.df.head())
        
    ## Need to count datatypes and lengths, etc. 
        
    def send_to_sql(self):
        self.df.to_sql()
            
        
            
            

# TODO - Maybe I should make a StringBuilder class for the connection string? Not even sure.

# ! Maybe have another function that's callable to decide which database to put the csv into?

# TODO - I need to honestly think about the entire way I would make this whole thing. 


df.to_sql()


