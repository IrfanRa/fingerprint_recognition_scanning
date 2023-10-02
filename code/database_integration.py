import sqlite3
import numpy as np

# Define file paths
database_path = "database/biometric_data.db"
dataset_path = "fingerprint_dataset/np_data/"

# Connect to the SQLite database
print("Connecting to the database...\n")
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Create the fingerprint_data table if it doesn't exist
print("Creating the 'fingerprint_data' table...")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS fingerprint_data (
        id INTEGER PRIMARY KEY,
        fingerprint_image BLOB,
        is_match BOOLEAN
    )
''')

# Export and load your fingerprint dataset
print("Exporting and loading fingerprint dataset...")
try:
    fingerprint_data = np.load(dataset_path + "img_real.npy")
    match_data = np.load(dataset_path + "label_real.npy")
    
    # Loop through your dataset and insert records into the database
    print("Importing records into the database...")
    for i, fingerprint_image in enumerate(fingerprint_data):
        is_match = match_data[i]  # True or False indicating a match
        cursor.execute("INSERT INTO fingerprint_data (fingerprint_image, is_match) VALUES (?, ?)",
                       (fingerprint_image.tobytes(), is_match))


    # Commit changes and close the connection
    print("Committing changes and closing the connection...\n")
    conn.commit()
    conn.close()
    
    print("Database operation completed.")
except Exception as e:
    print("Error:", str(e))
