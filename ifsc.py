# ----------------------------------------------------------------------------
# Copyright (c) 2023 Mohamed Rizad
# All rights reserved.
#
# This code is licensed under the MIT License.
# You may use, distribute, and modify this code under the terms of the
# MIT License.
# ----------------------------------------------------------------------------


import pandas as pd

bank_dataset = pd.read_csv('dataset/IFSC.csv', low_memory=False)
def ifsc_module(ifsc_query):
    ifsc_query=str(ifsc_query).upper()
    ifsc_dataset=bank_dataset['IFSC']
    ifsc_search=bank_dataset[(ifsc_dataset) == ifsc_query]
    fetched_res = ifsc_search.to_dict(orient='records')[0]
    fetched = {key: str(value).replace('.0','').replace('nan',"None") for key, value in fetched_res.items()}
    return fetched

