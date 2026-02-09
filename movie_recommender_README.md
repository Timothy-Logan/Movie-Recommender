# Movie Recommender CLI

A command-line Python application that provides movie recommendations using The Movie Database (TMDB) API. Get personalized suggestions based on movie titles, directors, and genres.

## Features
- 🎬 Search for movies by title
- 🎭 Get movie recommendations based on directors
- 📊 Discover movies by genre
- 🔍 Fetch detailed movie information (cast, crew, ratings)
- 💻 Simple command-line interface

## Technologies
- **Python 3.9+**
- **TMDB API** - The Movie Database for movie data
- **Requests** - HTTP library for API calls
- **sys** - Command-line argument handling

## Prerequisites

You'll need a TMDB API key to use this application:
1. Create a free account at [https://www.themoviedb.org/](https://www.themoviedb.org/)
2. Navigate to Settings → API
3. Request an API key (choose "Developer" option)
4. Copy your API key

## Installation

### Local Setup
```bash
# Clone repository
git clone https://github.com/Timothy-Logan/movie-recommender-cli
cd movie-recommender-cli

# Install dependencies
pip install -r requirements.txt

# Set up your API key
# Edit movie_recommender.py and add your TMDB API key on line 16
```

## Usage

### Basic Command
```bash
python movie_recommender.py
```

### Get Recommendations
The CLI will prompt you to:
1. Search for a movie by title
2. View movie details (cast, crew, ratings)
3. Get recommendations based on:
   - Movies by the same director
   - Movies in the same genre
   - Popular movies in the genre

### Example Session
```bash
$ python movie_recommender.py
Enter movie title: The Matrix
Found: The Matrix (1999)
Rating: 8.2/10

Director: Wachowski Brothers
Recommendations based on director:
- Cloud Atlas (2012)
- Speed Racer (2008)
...

Recommendations based on genre (Action, Sci-Fi):
- Inception (2010)
- Blade Runner (1982)
...
```

## How It Works

The application uses TMDB API to:
1. **Search for movies** - Finds movies matching your search query
2. **Get movie details** - Retrieves cast, crew, and genre information
3. **Find recommendations** - Uses the director and genre data to suggest similar movies
4. **Sort by popularity** - Ranks recommendations by TMDB popularity scores

## API Limitations
- Free TMDB API tier: 40 requests per 10 seconds
- Data is limited to what's available in TMDB database
- Some older or obscure films may have incomplete information

## Future Improvements
- [ ] Add user rating-based recommendations
- [ ] Implement collaborative filtering
- [ ] Save favorite movies and get personalized suggestions
- [ ] Add support for TV shows
- [ ] Create a configuration file for API key management
- [ ] Add filtering by release year or rating

## Dataset
All movie data is sourced from [The Movie Database (TMDB)](https://www.themoviedb.org/), a community-built movie and TV database.

## License
MIT License

## Contact
Timothy Logan - [tjlogan9@gmail.com](mailto:tjlogan9@gmail.com)  
GitHub: [@Timothy-Logan](https://github.com/Timothy-Logan)

## Acknowledgments
- Movie data provided by [The Movie Database (TMDB)](https://www.themoviedb.org/)
- This product uses the TMDB API but is not endorsed or certified by TMDB
