import pdb
import os
import gzip
from urllib.request import urlretrieve

arc_mmcif_url = "https://wwpdb.org/pdb?download=https://files.wwpdb.org/pub/pdb/data/structures/divided/mmCIF/ta/6tap.cif.gz"

# Create tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Download the file
filename = './tmp/6tap.cif.gz'
print(f"Downloading {arc_mmcif_url} to {filename}")
urlretrieve(arc_mmcif_url, filename)

# Unzip the file
output_filename = './data/6tap.cif'
print(f"Unzipping {filename} to {output_filename}")
with gzip.open(filename, 'rb') as f_in:
    with open(output_filename, 'wb') as f_out:
        f_out.write(f_in.read())

print(f"File downloaded and extracted to {output_filename}")

