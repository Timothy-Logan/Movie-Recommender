# Quick Start Guide

Get up and running with Movie Recommender CLI in 5 minutes!

## 1. Get Your API Key (2 minutes)

1. Visit https://www.themoviedb.org/signup
2. Create a free account
3. Go to Settings → API
4. Request an API Key (choose "Developer")
5. Copy your API Key (v3 auth)

## 2. Install (1 minute)

```bash
# Clone the repository
git clone https://github.com/Timothy-Logan/movie-recommender-cli.git
cd movie-recommender-cli

# Install dependencies
pip install -r requirements.txt
```

## 3. Run (2 minutes)

```bash
python movie_recommender.py
```

Enter your API key when prompted, then enter a movie title and start exploring!

## Example Commands

```bash
# Run the application
python movie_recommender.py

# When prompted:
# 1. Enter your TMDB API key
# 2. Enter a movie (e.g., "Inception")
# 3. Choose option 7 to see ALL recommendations
```

## Tips

- Use option 7 "Show All" to see recommendations across all criteria
- The app remembers your movie, so you can try different criteria without re-searching
- Press option 8 to search for a different movie anytime
- Your API key allows 50,000 requests per day (more than enough!)

That's it! Happy movie hunting! 🎬
