# Movie Recommendation System

This project implements a content-based movie recommendation system with an interactive user interface. It utilizes the TMDB 5000 movies dataset and the cosine similarity algorithm to suggest movies similar to a selected title.

## Project Overview

The goal of this project is to provide users with movie recommendations based on their preferences. By selecting a movie, the system suggests other movies that share similar characteristics, enhancing the user's movie discovery experience.

## Features

- **Content-Based Filtering**: Recommends movies similar to the selected title using cosine similarity.
- **Interactive User Interface**: Built with Streamlit for a user-friendly experience.

## Dataset

The system uses the TMDB 5000 movies dataset, which includes information such as genres, cast, crew, and keywords. This rich dataset allows for detailed analysis and accurate recommendations.

## Methodology

1. **Data Preprocessing**: Cleaned and prepared the dataset for analysis.
2. **Feature Extraction**: Extracted relevant features to represent each movie.
3. **Similarity Calculation**: Computed cosine similarity between movies to identify those with similar attributes.
4. **Recommendation Generation**: Based on the similarity scores, recommended movies that closely match the selected title.

## Installation and Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/koop46/Movie_recommendation_system.git
   cd Movie_recommendation_system
   ```

2. **Install Dependencies**:

   Ensure you have Python installed. Then, install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:

   ```bash
   streamlit run app.py
   ```

   This will launch the Streamlit app in your default web browser.

4. **Using the App**:

   - Select a movie from the dropdown menu.
   - Click the "Show Recommendations" button.
   - View the list of recommended movies.

## Repository Contents

- `app.py`: Main application script for the Streamlit interface.
- `recommender.py`: Contains functions for data processing and generating recommendations.
- `rec.ipynb`: Jupyter Notebook with exploratory data analysis and model development.
- `requirements.txt`: List of required Python libraries.

## Conclusion

This project demonstrates the application of content-based filtering techniques in building a movie recommendation system. The interactive interface enhances user engagement, making it easy to discover new movies based on individual preferences.

---
