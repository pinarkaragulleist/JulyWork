import hug
import pandas as pd

@hug.get("/")
def hello():
    d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
    df = pd.DataFrame(data=d)
    print(df)
    return(df)

@hug.get("/bye")
def bye():
    return ("good bye")
