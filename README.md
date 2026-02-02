# 🎬 Movie Recommendation System
# coding is remaining 

A content-based movie recommendation system built with Python and Streamlit that suggests similar movies based on user selection using cosine similarity.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [API Configuration](#api-configuration)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## ✨ Features

- **Content-Based Filtering**: Recommends movies based on similarity scores
- **Interactive UI**: User-friendly interface built with Streamlit
- **Movie Posters**: Displays poster images for recommended movies using TMDb API
- **Top 10 Recommendations**: Shows the 10 most similar movies to your selection
- **Fast Performance**: Pre-computed cosine similarity matrix for quick recommendations

## 🎥 Demo

The application displays:
1. A dropdown menu to select a movie
2. A "Recommend" button to generate suggestions
3. Top 10 recommended movies with posters and titles in a grid layout

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- TMDb API key (free from [TheMovieDB.org](https://www.themoviedb.org/settings/api))

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Required Files

Ensure you have the following files in your project directory:
- `movie.pkl` - Pickled file containing movies DataFrame and cosine similarity matrix
- `app.py` - Main Streamlit application

## 📦 Dependencies

Create a `requirements.txt` file with:

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
requests>=2.31.0
scikit-learn>=1.3.0
```

## 💻 Usage

### Step 1: Get TMDb API Key

1. Sign up at [TheMovieDB.org](https://www.themoviedb.org/)
2. Go to Settings → API
3. Request an API key (Developer option)
4. Copy your API key

### Step 2: Configure API Key

Open `app.py` and replace `YOUR_TMDB_API_KEY_HERE` with your actual API key:

```python
def fetch_poster(movie_id):
    api_key = "your_api_key_here"  # Replace this
    # ... rest of the code
```

### Step 3: Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Step 4: Use the Application

1. Select a movie from the dropdown menu
2. Click the "Recommend" button
3. View the top 10 recommended movies with their posters

## 🔧 How It Works

### 1. Data Preparation
- Movie dataset is processed and features are extracted
- Features include: genres, keywords, cast, crew, overview, etc.
- Text data is converted to numerical vectors using TF-IDF or Count Vectorization

### 2. Similarity Calculation
- Cosine similarity is computed between all movie pairs
- Results are stored in a similarity matrix
- The matrix and movie data are saved in `movie.pkl`

### 3. Recommendation Generation
```python
def get_recommendation(title, cosine_sim=cosine_sim):
    # Find movie index
    idx = movies[movies['title'] == title].index[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort by similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get top 10 (excluding the movie itself)
    sim_scores = sim_scores[1:11]
    
    # Return movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    return movies.iloc[movie_indices]
```

### 4. Poster Fetching
- Uses TMDb API to fetch movie posters
- Falls back to placeholder image if poster not available

## 📁 Project Structure

```
movie-recommendation-system/
│
├── app.py                      # Main Streamlit application
├── movie.pkl                   # Pickled model and data
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── notebooks/                  # Jupyter notebooks (optional)
│   └── data_preprocessing.ipynb
│
└── data/                       # Raw data files (optional)
    └── movies_metadata.csv
```

## 🔑 API Configuration

### TMDb API

The application uses TMDb API v3 for fetching movie posters:

```python
# API Endpoint Format
https://api.themoviedb.org/3/movie/{movie_id}?api_key={YOUR_API_KEY}

# Image Base URL
https://image.tmdb.org/t/p/w500{poster_path}
```

**Rate Limits**: 40 requests per 10 seconds (free tier)

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning (TF-IDF, Cosine Similarity)
- **Requests**: HTTP library for API calls
- **Pickle**: Model serialization

## 📊 Dataset

The recommendation system can work with any movie dataset containing:
- Movie titles
- Movie IDs (TMDb format)
- Features for similarity calculation (genres, cast, crew, keywords, etc.)

Common datasets:
- [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)

## 🐛 Troubleshooting

### Common Issues

**1. "No module named 'streamlit'"**
```bash
pip install streamlit
```

**2. "FileNotFoundError: movie.pkl"**
- Ensure `movie.pkl` is in the same directory as `app.py`
- Run the data preprocessing script to generate the pickle file

**3. Posters not loading**
- Check your TMDb API key is valid
- Verify your internet connection
- Ensure movie_id values in dataset are valid TMDb IDs

**4. "KeyError: 'title'"**
- Verify your DataFrame has a 'title' column
- Check the pickle file structure

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contribution
- Add filtering options (genre, year, rating)
- Implement collaborative filtering
- Add user rating system
- Improve UI/UX design
- Add more recommendation algorithms
- Create deployment guide

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [TMDb](https://www.themoviedb.org/) for providing the movie database API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Kaggle](https://www.kaggle.com/) for datasets
- The open-source community for inspiration

## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Recommendations
![Recommendations](screenshots/recommendations.png)

---

**Note**: Replace placeholder links, images, and contact information with your actual details before publishing.

## 🚀 Future Enhancements

- [ ] Add user authentication
- [ ] Implement collaborative filtering
- [ ] Add movie search functionality
- [ ] Include movie trailers
- [ ] Add watchlist feature
- [ ] Implement rating system
- [ ] Deploy to cloud (Heroku, AWS, or Streamlit Cloud)
- [ ] Add mobile responsive design
- [ ] Multi-language support
- [ ] Cache API responses

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Contact via email

---

⭐ If you found this project helpful, please give it a star!
