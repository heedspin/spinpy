from ipdb import set_trace as st
from urllib.request import urlretrieve 
import pandas as pd
import matplotlib
# matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/MolSSI-Education/molssicheminfo/refs/heads/master/data/PubChemElements_all.csv"
filename = "data/PubChemElements_all.csv"
urlretrieve(url, filename)
print(f"Downloaded data to {filename}")
df = pd.read_csv(filename)

subplot = df.hist(figsize=(8, 8), edgecolor="black", grid=False)
plt.savefig('data/histogram.png', dpi=300, bbox_inches='tight')
print("Histogram saved as data/histogram.png")
plt.close()  # Close the plot to free memory
exit(0)