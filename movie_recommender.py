#!/usr/bin/env python3
"""
Movie Recommendation CLI
A command-line application to get movie recommendations based on various criteria.
"""

import requests
import sys
from typing import List, Dict, Optional

class MovieRecommender:
    """Main class for movie recommendations using TMDB API."""
    
    def __init__(self, api_key: str):
        """Initialize with TMDB API key."""
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"
        
    def search_movie(self, title: str) -> Optional[Dict]:
        """Search for a movie by title and return the best match."""
        url = f"{self.base_url}/search/movie"
        params = {
            'api_key': self.api_key,
            'query': title,
            'language': 'en-US'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data['results']:
                return data['results'][0]  # Return the first (best) match
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error searching for movie: {e}")
            return None
    
    def get_movie_details(self, movie_id: int) -> Optional[Dict]:
        """Get detailed information about a movie."""
        url = f"{self.base_url}/movie/{movie_id}"
        params = {
            'api_key': self.api_key,
            'append_to_response': 'credits,keywords'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting movie details: {e}")
            return None
    
    def get_recommendations_by_genre(self, movie_id: int, limit: int = 10) -> List[Dict]:
        """Get movie recommendations based on genre."""
        movie_details = self.get_movie_details(movie_id)
        if not movie_details or 'genres' not in movie_details:
            return []
        
        genre_ids = [genre['id'] for genre in movie_details['genres']]
        
        url = f"{self.base_url}/discover/movie"
        params = {
            'api_key': self.api_key,
            'with_genres': ','.join(map(str, genre_ids)),
            'sort_by': 'popularity.desc',
            'language': 'en-US'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data['results'][:limit]
        except requests.exceptions.RequestException as e:
            print(f"Error getting genre recommendations: {e}")
            return []
    
    def get_recommendations_by_director(self, movie_id: int, limit: int = 10) -> List[Dict]:
        """Get movie recommendations based on director."""
        movie_details = self.get_movie_details(movie_id)
        if not movie_details or 'credits' not in movie_details:
            return []
        
        # Find the director
        director = None
        for crew_member in movie_details['credits']['crew']:
            if crew_member['job'] == 'Director':
                director = crew_member
                break
        
        if not director:
            return []
        
        # Get other movies by this director
        url = f"{self.base_url}/discover/movie"
        params = {
            'api_key': self.api_key,
            'with_crew': director['id'],
            'sort_by': 'popularity.desc',
            'language': 'en-US'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            # Filter out the original movie
            return [movie for movie in data['results'] if movie['id'] != movie_id][:limit]
        except requests.exceptions.RequestException as e:
            print(f"Error getting director recommendations: {e}")
            return []
    
    def get_recommendations_by_cast(self, movie_id: int, limit: int = 10) -> List[Dict]:
        """Get movie recommendations based on cast members."""
        movie_details = self.get_movie_details(movie_id)
        if not movie_details or 'credits' not in movie_details:
            return []
        
        # Get top 3 cast members
        cast = movie_details['credits']['cast'][:3]
        if not cast:
            return []
        
        cast_ids = [actor['id'] for actor in cast]
        
        url = f"{self.base_url}/discover/movie"
        params = {
            'api_key': self.api_key,
            'with_cast': ','.join(map(str, cast_ids)),
            'sort_by': 'popularity.desc',
            'language': 'en-US'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            # Filter out the original movie
            return [movie for movie in data['results'] if movie['id'] != movie_id][:limit]
        except requests.exceptions.RequestException as e:
            print(f"Error getting cast recommendations: {e}")
            return []
    
    def get_recommendations_by_keywords(self, movie_id: int, limit: int = 10) -> List[Dict]:
        """Get movie recommendations based on plot keywords."""
        movie_details = self.get_movie_details(movie_id)
        if not movie_details or 'keywords' not in movie_details:
            return []
        
        keywords = movie_details['keywords'].get('keywords', [])
        if not keywords:
            return []
        
        # Use top 5 keywords
        keyword_ids = [kw['id'] for kw in keywords[:5]]
        
        url = f"{self.base_url}/discover/movie"
        params = {
            'api_key': self.api_key,
            'with_keywords': ','.join(map(str, keyword_ids)),
            'sort_by': 'popularity.desc',
            'language': 'en-US'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            # Filter out the original movie
            return [movie for movie in data['results'] if movie['id'] != movie_id][:limit]
        except requests.exceptions.RequestException as e:
            print(f"Error getting keyword recommendations: {e}")
            return []
    
    def get_recommendations_by_rating(self, movie_id: int, limit: int = 10) -> List[Dict]:
        """Get movie recommendations based on similar ratings."""
        movie_details = self.get_movie_details(movie_id)
        if not movie_details:
            return []
        
        rating = movie_details.get('vote_average', 0)
        genre_ids = [genre['id'] for genre in movie_details.get('genres', [])]
        
        url = f"{self.base_url}/discover/movie"
        params = {
            'api_key': self.api_key,
            'vote_average.gte': max(0, rating - 1),
            'vote_average.lte': min(10, rating + 1),
            'with_genres': ','.join(map(str, genre_ids)) if genre_ids else None,
            'sort_by': 'popularity.desc',
            'language': 'en-US'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            # Filter out the original movie
            return [movie for movie in data['results'] if movie['id'] != movie_id][:limit]
        except requests.exceptions.RequestException as e:
            print(f"Error getting rating recommendations: {e}")
            return []
    
    def get_tmdb_recommendations(self, movie_id: int, limit: int = 10) -> List[Dict]:
        """Get TMDB's built-in recommendations."""
        url = f"{self.base_url}/movie/{movie_id}/recommendations"
        params = {
            'api_key': self.api_key,
            'language': 'en-US'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data['results'][:limit]
        except requests.exceptions.RequestException as e:
            print(f"Error getting TMDB recommendations: {e}")
            return []
    
    def display_movie_info(self, movie: Dict):
        """Display formatted movie information."""
        title = movie.get('title', 'Unknown')
        year = movie.get('release_date', 'Unknown')[:4] if movie.get('release_date') else 'Unknown'
        rating = movie.get('vote_average', 0)
        overview = movie.get('overview', 'No overview available.')
        
        print(f"\n{'='*80}")
        print(f"Title: {title} ({year})")
        print(f"Rating: {rating}/10")
        print(f"Overview: {overview}")
        print(f"{'='*80}")
    
    def display_recommendations(self, movies: List[Dict], criteria: str):
        """Display a list of recommended movies."""
        if not movies:
            print(f"\nNo recommendations found based on {criteria}.")
            return
        
        print(f"\n\n{'#'*80}")
        print(f"RECOMMENDATIONS BASED ON {criteria.upper()}")
        print(f"{'#'*80}")
        
        for i, movie in enumerate(movies, 1):
            title = movie.get('title', 'Unknown')
            year = movie.get('release_date', 'Unknown')[:4] if movie.get('release_date') else 'Unknown'
            rating = movie.get('vote_average', 0)
            
            print(f"\n{i}. {title} ({year}) - Rating: {rating}/10")


def main():
    """Main function to run the movie recommendation CLI."""
    print("\n" + "="*80)
    print(" "*20 + "MOVIE RECOMMENDATION SYSTEM")
    print("="*80 + "\n")
    
    # Check if API key is provided
    api_key = input("Enter your TMDB API key (or press Enter to use default): ").strip()
    if not api_key:
        print("\nPlease provide a TMDB API key to use this application.")
        print("You can get a free API key at: https://www.themoviedb.org/settings/api")
        return
    
    recommender = MovieRecommender(api_key)
    
    # Get movie title from user
    movie_title = input("\nEnter a movie title: ").strip()
    if not movie_title:
        print("No movie title provided. Exiting.")
        return
    
    # Search for the movie
    print(f"\nSearching for '{movie_title}'...")
    movie = recommender.search_movie(movie_title)
    
    if not movie:
        print(f"Could not find movie: {movie_title}")
        return
    
    # Display movie information
    recommender.display_movie_info(movie)
    movie_id = movie['id']
    
    # Show menu for recommendation criteria
    while True:
        print("\n" + "-"*80)
        print("How would you like to find similar movies?")
        print("-"*80)
        print("1. By Genre")
        print("2. By Director")
        print("3. By Cast")
        print("4. By Plot Keywords")
        print("5. By Rating")
        print("6. TMDB Recommendations (Combined)")
        print("7. Show All (All criteria)")
        print("8. Search for a different movie")
        print("9. Exit")
        print("-"*80)
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            recommendations = recommender.get_recommendations_by_genre(movie_id)
            recommender.display_recommendations(recommendations, "Genre")
        elif choice == '2':
            recommendations = recommender.get_recommendations_by_director(movie_id)
            recommender.display_recommendations(recommendations, "Director")
        elif choice == '3':
            recommendations = recommender.get_recommendations_by_cast(movie_id)
            recommender.display_recommendations(recommendations, "Cast")
        elif choice == '4':
            recommendations = recommender.get_recommendations_by_keywords(movie_id)
            recommender.display_recommendations(recommendations, "Plot Keywords")
        elif choice == '5':
            recommendations = recommender.get_recommendations_by_rating(movie_id)
            recommender.display_recommendations(recommendations, "Rating")
        elif choice == '6':
            recommendations = recommender.get_tmdb_recommendations(movie_id)
            recommender.display_recommendations(recommendations, "TMDB Algorithm")
        elif choice == '7':
            print("\n" + "#"*80)
            print(" "*25 + "ALL RECOMMENDATIONS")
            print("#"*80)
            
            recommender.display_recommendations(
                recommender.get_recommendations_by_genre(movie_id, 5), "Genre"
            )
            recommender.display_recommendations(
                recommender.get_recommendations_by_director(movie_id, 5), "Director"
            )
            recommender.display_recommendations(
                recommender.get_recommendations_by_cast(movie_id, 5), "Cast"
            )
            recommender.display_recommendations(
                recommender.get_recommendations_by_keywords(movie_id, 5), "Plot Keywords"
            )
            recommender.display_recommendations(
                recommender.get_recommendations_by_rating(movie_id, 5), "Rating"
            )
            recommender.display_recommendations(
                recommender.get_tmdb_recommendations(movie_id, 5), "TMDB Algorithm"
            )
        elif choice == '8':
            movie_title = input("\nEnter a new movie title: ").strip()
            if movie_title:
                print(f"\nSearching for '{movie_title}'...")
                movie = recommender.search_movie(movie_title)
                if movie:
                    recommender.display_movie_info(movie)
                    movie_id = movie['id']
                else:
                    print(f"Could not find movie: {movie_title}")
            else:
                print("No movie title provided.")
        elif choice == '9':
            print("\nThank you for using Movie Recommendation System!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
