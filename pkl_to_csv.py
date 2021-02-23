import pickle
import pandas as pd


with open("data/ffpp_videos.pkl", "rb") as ffpp:
    ffpp_data = pickle.load(ffpp)

pd.set_option('display.width',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',None)

inf=str(ffpp_data)
ft = open('test1.csv', 'w')
ft.write(inf)