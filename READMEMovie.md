# Movie Recommendation CLI

A command-line application that helps you discover similar movies based on various criteria using The Movie Database (TMDB) API.

## Features

- Search for movies by title
- Get movie recommendations based on:
  - **Genre** - Find movies in the same genre(s)
  - **Director** - Discover other films by the same director
  - **Cast** - Find movies featuring the same actors
  - **Plot Keywords** - Get recommendations based on similar themes/topics
  - **Rating** - Find movies with similar ratings
  - **TMDB Algorithm** - Use TMDB's built-in recommendation engine
- View detailed movie information including title, year, rating, and overview
- Interactive menu system for easy navigation

## Prerequisites

- Python 3.7 or higher
- A TMDB API key (free)

## Step-by-Step Setup Instructions

### Step 1: Get a TMDB API Key

1. Go to [The Movie Database website](https://www.themoviedb.org/)
2. Create a free account (click "Join TMDB" in the top right)
3. After logging in, go to your account settings
4. Navigate to the "API" section (Settings → API)
5. Click "Create" or "Request an API Key"
6. Choose "Developer" option
7. Fill out the application form (you can use personal/educational purpose)
8. Once approved, copy your **API Key (v3 auth)**

### Step 2: Clone or Download the Repository

```bash
# If using git
git clone https://github.com/Timothy-Logan/movie-recommender-cli.git
cd movie-recommender-cli

# Or download the ZIP file and extract it
```

### Step 3: Install Dependencies

```bash
# Install the required Python package
pip install -r requirements.txt

# Or install directly
pip install requests
```

### Step 4: Run the Application

```bash
python movie_recommender.py
```

## How to Use

### Basic Usage

1. **Start the application:**
   ```bash
   python movie_recommender.py
   ```

2. **Enter your TMDB API key** when prompted
   - You only need to enter this each time you run the program
   - Keep your API key private and don't share it publicly

3. **Search for a movie:**
   - Enter a movie title (e.g., "The Matrix", "Inception", "Pulp Fiction")
   - The app will find the best match and display movie details

4. **Choose recommendation criteria:**
   - Select from the menu (options 1-7) to get recommendations based on different criteria
   - Option 7 shows recommendations for ALL criteria at once

5. **Explore recommendations:**
   - Browse the list of recommended movies
   - Each recommendation shows title, year, and rating

6. **Search for another movie:**
   - Choose option 8 to search for a different movie
   - Or option 9 to exit

### Example Session

```
================================================================================
                    MOVIE RECOMMENDATION SYSTEM
================================================================================

Enter your TMDB API key: YOUR_API_KEY_HERE

Enter a movie title: The Dark Knight

Searching for 'The Dark Knight'...

================================================================================
Title: The Dark Knight (2008)
Rating: 8.5/10
Overview: Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent...
================================================================================

--------------------------------------------------------------------------------
How would you like to find similar movies?
--------------------------------------------------------------------------------
1. By Genre
2. By Director
3. By Cast
4. By Plot Keywords
5. By Rating
6. TMDB Recommendations (Combined)
7. Show All (All criteria)
8. Search for a different movie
9. Exit
--------------------------------------------------------------------------------

Enter your choice (1-9): 1

################################################################################
RECOMMENDATIONS BASED ON GENRE
################################################################################

1. The Batman (2022) - Rating: 7.7/10
2. Batman Begins (2005) - Rating: 7.7/10
3. Joker (2019) - Rating: 8.2/10
...
```

## Menu Options Explained

1. **By Genre** - Finds movies in the same genre(s) as your selected movie
2. **By Director** - Shows other films directed by the same person
3. **By Cast** - Recommends movies featuring the main actors from your movie
4. **By Plot Keywords** - Uses TMDB's keywords to find thematically similar films
5. **By Rating** - Finds movies with similar audience ratings
6. **TMDB Recommendations** - Uses TMDB's proprietary recommendation algorithm
7. **Show All** - Displays recommendations from ALL criteria (5 from each)
8. **Search for a different movie** - Start a new search without restarting the program
9. **Exit** - Close the application

## Troubleshooting

### "Could not find movie"
- Try a different spelling or use the full official title
- Some movies might not be in the TMDB database
- Try adding the year (e.g., "The Matrix 1999")

### "No recommendations found"
- Some criteria might not return results for certain movies
- Try a different recommendation method
- Use option 7 to see all available recommendations

### API Key Issues
- Make sure you're using the v3 API key (not v4)
- Check that you copied the entire key without extra spaces
- Verify your API key is active in your TMDB account settings

### Connection Errors
- Check your internet connection
- TMDB API might be temporarily unavailable
- Your API key might have reached its rate limit (unlikely with normal use)

## API Information

This application uses The Movie Database (TMDB) API:
- **Free tier:** 50,000 requests per day
- **Rate limit:** 50 requests per second
- **Documentation:** https://developers.themoviedb.org/3

## License

This project is open source and available for personal and educational use.

## Credits

- Movie data provided by [The Movie Database (TMDB)](https://www.themoviedb.org/)
- This product uses the TMDB API but is not endorsed or certified by TMDB

## Contributing

Feel free to fork this repository and submit pull requests for any improvements!

## Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Review the TMDB API documentation
3. Open an issue on GitHub
