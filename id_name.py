import pandas as pd
import numpy as np

def login_table(id_name_verified, id_password):
    # in place makes sure that changes are made in a current dataframe 
    # id_name_verified.drop('Verified', axis=1, inplace= True)
    id_name_verified.rename(columns={'Verified':'V'}, inplace= True) 
    # id_password[:,1] -> : selects all rows and 1 selects only second column
    id_name_verified['Password'] = id_password[:,1]


id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)
login_table(id_name_verified, id_password)
print(id_name_verified)