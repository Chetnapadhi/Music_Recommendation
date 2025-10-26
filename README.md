# Music Recommender System

This project is a Music Recommender System built using machine learning techniques. It utilizes a dataset of songs to provide recommendations based on user input.

## Project Structure

```
# 🎵 Music Recommender System

A machine learning-based music recommendation system that suggests similar songs based on text features using TF-IDF and cosine similarity.

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Chetnapadhi/Music_Recommendation.git
cd Music_Recommendation/music-recommender
```

### Step 2: Install Required Packages

Open PowerShell in the project directory and run:

```powershell
pip install -r requirements.txt
```

### Step 3: Train the Model

Navigate to the music-recommender directory and run:

```powershell
cd music-recommender
python src/model/train.py
```

**Note:** The repository includes a sample Hindi songs dataset. For a larger dataset:
1. Download the Spotify Million Song Dataset from Kaggle
2. Replace `src/data/spotify_millsongdata.csv` with your dataset
3. Re-run the training script

This will:
- Load the dataset (Hindi songs sample or your custom dataset)
- Process and clean the text data
- Generate similarity matrix
- Save the trained models in the `models/` folder

**Note:** Training may take 5-10 minutes depending on your system and dataset size.

### Step 3: Run the Streamlit App

After training is complete, run:

```powershell
streamlit run src/app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
music-recommender/
├── src/
│   ├── app.py                      # Streamlit web application
│   ├── model/
│   │   └── train.py               # Model training script
│   └── data/
│       └── spotify_millsongdata.csv  # Dataset
├── notebooks/
│   └── Model_Training.ipynb       # Jupyter notebook for exploration
├── models/
│   ├── df.pkl                     # Processed dataset (generated)
│   └── similarity.pkl             # Similarity matrix (generated)
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🎯 How It Works

1. **Data Processing**: The system processes song lyrics/text data
2. **Feature Extraction**: Uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text to numerical features
3. **Similarity Calculation**: Computes cosine similarity between songs
4. **Recommendations**: Returns the 5 most similar songs based on the similarity matrix
5. **UI**: Displays recommendations with album covers fetched from Spotify API

## 🔧 Features

- Select from 5000 popular songs
- Get 5 similar song recommendations
- View album covers for recommended songs
- Clean and intuitive user interface

## 🐛 Troubleshooting

**Issue: Module not found**
- Solution: Make sure you installed all requirements: `pip install -r requirements.txt`

**Issue: Model files not found**
- Solution: Run the training script first: `python src/model/train.py`

**Issue: NLTK punkt error**
- Solution: The training script automatically downloads required NLTK data

## 📝 Notes

- The repository includes a sample Hindi songs dataset for testing
- Model files (`*.pkl`) are excluded from git due to size (>100MB)
- You need to train the model locally after cloning the repository
- For larger datasets, download from Kaggle and replace the sample CSV
- Album covers are fetched from Spotify API
- Default album cover is shown if a song is not found on Spotify

## 🗂️ Model Files

The trained model files are generated locally and stored in the `models/` directory:
- `df.pkl` - Processed dataset with song information
- `similarity.pkl` - Cosine similarity matrix for recommendations

These files are automatically created when you run the training script and are excluded from version control due to their large size.

## 🤝 Contributing

Feel free to fork this project and make improvements!

## 📄 License

This project is for educational purposes.
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd music-recommender
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the music recommender application, execute the following command:
```
streamlit run src/app.py
```

This will start a local web server and open the application in your default web browser.

## Usage

1. Type or select a song from the dropdown menu.
2. Click on the "Show Recommendation" button to get song recommendations based on your selection.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
