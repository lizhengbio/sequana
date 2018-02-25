import pandas as pd
from pylab import plot


class CNVnator(object):
    """Reader of the CNVnator output file.



    """
    def __init__(self, filename):

        self.filename = filename


        self.df = pd.read_csv(filename, sep="\t", header=None)
        self.df.columns = ["type", "label", "size", "3","4","5","6","7","8"]
        name = self.df['label'].apply(lambda x: x.rsplit(":",1)[0])
        start = self.df['label'].apply(lambda x: x.rsplit(":",1)[1].split("-")[0])
        end = self.df['label'].apply(lambda x: x.rsplit(":",1)[1].split("-")[1])
        self.df['start'] = start.astype(int)
        self.df['end'] = end.astype(int)
        self.df['name'] = name


    def plot(self, chr_name, x1=None, x2=None, Y=20):

        df = self.df.query("name == @chr_name")
        for _, item in df.iterrows():
            if item['type'] == "deletion":
                plot([item.start, item.end], [-1,-1], "m-")
            else:
                plot([item.start, item.end], [Y, Y], "m-")


