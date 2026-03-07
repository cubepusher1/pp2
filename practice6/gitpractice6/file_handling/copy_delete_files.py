import shutil
import os

# Copy file
shutil.copy("source.txt", "copy.txt")

# Delete file
os.remove("copy.txt")