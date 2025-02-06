#!/usr/bin/env python
# coding: utf-8

# ## unzip_file
# 
# New notebook

# In[ ]:


# Welcome to your new notebook
# Type here in the cell editor to add code!
import zipfile
import os
from pyspark.sql import SparkSession

# Define file paths
zip_file_path = "/lakehouse/default/Files/BACI_HS17_V202501.zip"  # Adjust path
extract_folder_path = "/lakehouse/default/Files/extracted_csvs/"

# Extract zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder_path)

print(f"Extracted files to: {extract_folder_path}")

