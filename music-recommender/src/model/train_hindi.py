import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

# Load the dataset
print("Loading dataset...")
# Get the absolute path to the data file
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, '..', 'data', 'spotify_millsongdata.csv')

# Check if main dataset exists, otherwise use Hindi sample
if not os.path.exists(data_path) or os.path.getsize(data_path) < 1000:
    print("Main dataset not found. Using Hindi songs sample...")
    data_path = os.path.join(script_dir, '..', 'data', 'hindi_songs_sample.csv')

df = pd.read_csv(data_path)
print(f"Original dataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Sample songs to reduce computational load (use min to avoid sampling more than available)
sample_size = min(5000, len(df))
print(f"Sampling {sample_size} songs...")
if 'link' in df.columns:
    df = df.sample(sample_size).drop('link', axis=1).reset_index(drop=True)
else:
    df = df.sample(sample_size).reset_index(drop=True)
print(f"Sampled dataset shape: {df.shape}")

# Text Cleaning/ Text Preprocessing
print("Cleaning text data...")
df['text'] = df['text'].str.lower().replace(r'^\w\s', ' ').replace(r'\n', ' ', regex=True)

# Tokenization and Stemming
print("Tokenizing and stemming...")
stemmer = PorterStemmer()

def tokenization(txt):
    try:
        tokens = nltk.word_tokenize(txt)
        stemming = [stemmer.stem(w) for w in tokens]
        return " ".join(stemming)
    except:
        return txt  # Return original text if tokenization fails

df['text'] = df['text'].apply(lambda x: tokenization(x))

# Feature Extraction
print("Extracting features using TF-IDF...")
# For Hindi/multilingual, we don't use English stop words
tfidvector = TfidfVectorizer(analyzer='word', max_features=5000)
matrix = tfidvector.fit_transform(df['text'])

# Compute Similarity Matrix
print("Computing similarity matrix...")
similarity = cosine_similarity(matrix)

# Create models directory if it doesn't exist
models_dir = os.path.join(script_dir, '..', '..', 'models')
models_dir = os.path.abspath(models_dir)
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

# Save the processed DataFrame and similarity matrix
print("Saving models...")
df_path = os.path.join(models_dir, 'df.pkl')
sim_path = os.path.join(models_dir, 'similarity.pkl')
pickle.dump(df, open(df_path, 'wb'))
pickle.dump(similarity, open(sim_path, 'wb'))

print("Training completed successfully!")
print(f"Models saved in {models_dir}")
print(f"Total songs in model: {len(df)}")
