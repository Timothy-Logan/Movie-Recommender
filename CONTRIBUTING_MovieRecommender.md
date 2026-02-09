# Contributing to Movie Recommender CLI

Thank you for your interest in contributing to the Movie Recommender CLI! We welcome contributions from the community.

## Ways to Contribute

### 🐛 Report Bugs

Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version)
- Movie title or query that caused the issue
- Error messages or screenshots

### 💡 Suggest Features

Have an idea? Open an issue describing:
- The feature you'd like to see
- Why it would be useful
- Possible implementation approach
- Examples of similar features in other tools

### 📝 Improve Documentation

Documentation improvements are always welcome:
- Fix typos or unclear explanations
- Add more example queries
- Improve troubleshooting section
- Add tips for getting better recommendations

### 🔧 Submit Code

1. **Fork** the repository
2. **Create a branch** for your feature
   ```bash
   git checkout -b feature/add-rating-filter
   ```
3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add comments for complex logic
   - Update documentation if needed
   - Add docstrings to new functions
4. **Test your changes**
   - Run the CLI with various movie titles
   - Test error cases (invalid titles, no results)
   - Verify API calls work correctly
5. **Commit with clear message**
   ```bash
   git commit -m "Add: filter recommendations by minimum rating"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/add-rating-filter
   ```
7. **Open a Pull Request**
   - Describe your changes clearly
   - Reference any related issues
   - Include example outputs if applicable

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Movie-Recommender
cd Movie-Recommender

# Install dependencies
pip install -r requirements.txt

# Get a TMDB API key
# 1. Go to https://www.themoviedb.org/signup
# 2. Create account and request API key
# 3. Add your key to movie_recommender.py (line 16)

# Run the CLI
python movie_recommender.py
```

## Code Style Guidelines

- Follow [PEP 8](https://pep8.org/) Python style guide
- Use descriptive variable names (e.g., `movie_title` not `mt`)
- Add docstrings to all functions and classes
- Keep functions focused and under 50 lines when possible
- Comment API calls and complex logic
- Use type hints for function parameters and returns

Example:
```python
def get_recommendations_by_director(self, movie_id: int, limit: int = 10) -> list:
    """
    Get movie recommendations based on director.
    
    Args:
        movie_id: TMDB movie ID
        limit: Maximum number of recommendations to return
        
    Returns:
        List of recommended movies with metadata
    """
    # Implementation here
```

## Testing

Before submitting a pull request:

1. **Test with various movies**:
   ```bash
   python movie_recommender.py
   # Try these test cases:
   # - Popular movie: "The Matrix"
   # - Obscure movie: "Moon" (2009)
   # - Very old movie: "Casablanca"
   # - Invalid movie: "asdfghjkl"
   # - Movie with special characters: "Amélie"
   ```

2. **Test error handling**:
   - Try without internet connection
   - Try with invalid API key
   - Try with very short input
   - Try with very long input

3. **Check code style**:
   ```bash
   # Install flake8 if needed
   pip install flake8
   
   # Run linter
   flake8 movie_recommender.py --max-line-length=100
   ```

## Project Structure

```
Movie-Recommender/
├── movie_recommender.py  # Main CLI application
├── requirements.txt      # Python dependencies
├── LICENSE              # MIT License
├── README.md            # Project documentation
├── QUICKSTART.md        # Quick setup guide
└── .gitignore          # Git ignore rules
```

## Adding New Features

### Want to add a new recommendation algorithm?

1. Add new method to `MovieRecommender` class
2. Follow existing method patterns
3. Document the algorithm in docstring
4. Update README with new feature details

### Want to improve the CLI interface?

1. Modify the main loop in `movie_recommender.py`
2. Keep interface simple and intuitive
3. Add helpful prompts for users
4. Test with various user inputs

### Want to add more TMDB data?

1. Check TMDB API documentation
2. Add new API call in appropriate method
3. Parse and format the data nicely
4. Update README with new information shown

## Feature Ideas

Looking for something to work on? Here are some ideas:

**Easy:**
- Add color output to make results more readable
- Add more error handling for edge cases
- Improve help text and prompts
- Add command-line arguments for direct queries

**Medium:**
- Add support for TV shows
- Save favorite movies to a file
- Add filtering by year or rating
- Cache API results to reduce API calls

**Advanced:**
- Add collaborative filtering
- Implement user rating-based recommendations
- Create a simple web interface
- Add support for multiple languages

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update requirements.txt if you add new dependencies
3. Add examples of new features in README
4. Your PR will be reviewed within 2-3 days
5. Address any feedback from reviewers
6. Once approved, your changes will be merged!

## TMDB API Guidelines

When working with the TMDB API:
- Respect rate limits (40 requests per 10 seconds)
- Cache results when possible to reduce API calls
- Handle API errors gracefully
- Follow TMDB's terms of service
- Give credit to TMDB in any public-facing features

## Questions or Need Help?

Feel free to:
- Open an issue for discussion
- Email: [tjlogan9@gmail.com](mailto:tjlogan9@gmail.com)
- Check existing issues for similar questions
- Ask about TMDB API usage

## Code of Conduct

### Our Standards

- Be respectful and constructive
- Welcome newcomers and help them learn
- Focus on what is best for the project
- Show empathy towards other contributors
- Give and accept constructive feedback gracefully

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## Recognition

Contributors will be:
- Listed in the project's acknowledgments
- Credited in release notes for their contributions
- Invited to collaborate on future enhancements
- Mentioned in README if making significant contributions

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

---

Thank you for helping improve the Movie Recommender CLI! 🎬
