import pandas as pd
import pickle

# Sample data for the DataFrame
data = {
    'song': ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5', 
             'Song 6', 'Song 7', 'Song 8', 'Song 9', 'Song 10'],
    'artist': ['Artist 1', 'Artist 2', 'Artist 3', 'Artist 4', 'Artist 5', 
               'Artist 6', 'Artist 7', 'Artist 8', 'Artist 9', 'Artist 10'],
    # Add more columns as needed
}

# Creating DataFrame
df = pd.DataFrame(data)

# Save DataFrame to a pickle file
with open('df.pkl', 'wb') as f:
    pickle.dump(df, f)
