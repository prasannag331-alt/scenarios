import csv
import re

def load_movies(filename="movies.csv"):
    """Reads movie records from a CSV file."""
    movies = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            # Using DictReader assumes the CSV has a header row (e.g., Movie ID, Title, Genre, Year)
            reader = csv.DictReader(file)
            for row in reader:
                movies.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please ensure the file exists in the same directory.")
    return movies

def display_all_movies(movies):
    """Displays all movie information."""
    if not movies:
        print("No movie records available.")
        return
    
    print("\n--- All Movie Records ---")
    # Dynamically print keys and values for flexibility based on CSV headers
    for movie in movies:
        details = ", ".join([f"{key}: {value}" for key, value in movie.items()])
        print(details)

def search_by_id(movies, movie_id):
    """Searches for a movie using a specific Movie ID."""
    # Assumes the first column/header contains 'ID' or 'Movie ID'
    id_key = next((k for k in movies[0].keys() if 'id' in k.lower()), None) if movies else None
    
    if not id_key:
        print("Could not automatically determine the ID column from CSV headers.")
        return

    found = False
    for movie in movies:
        if movie[id_key].strip() == str(movie_id).strip():
            print(f"\nMovie Found (ID: {movie_id}):")
            for key, value in movie.items():
                print(f"  {key}: {value}")
            found = True
            break
            
    if not found:
        print(f"No movie found with ID: {movie_id}")

def search_by_title_regex(movies, pattern):
    """Uses Regular Expressions to search movies by title."""
    # Assumes a column/header contains 'title'
    title_key = next((k for k in movies[0].keys() if 'title' in k.lower()), None) if movies else None
    
    if not title_key:
        print("Could not automatically determine the Title column from CSV headers.")
        return

    try:
        compiled_pattern = re.compile(pattern, re.IGNORECASE)
    except re.error:
        print("Invalid regular expression pattern.")
        return

    print(f"\n--- Search Results for Pattern: '{pattern}' ---")
    count = 0
    for movie in movies:
        if compiled_pattern.search(movie[title_key]):
            details = ", ".join([f"{key}: {value}" for key, value in movie.items()])
            print(details)
            count += 1
            
    if count == 0:
        print("No movies matched the title pattern.")

def main():
    # 1. Read movie records from movies.csv
    movies = load_movies("movies.csv")
    if not movies:
        return

    while True:
        print("\n=========================")
        print(" Movie Collection System ")
        print("=========================")
        print("1. Display All Movies")
        print("2. Search by Movie ID")
        print("3. Search by Title (Regex)")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            display_all_movies(movies)
        elif choice == '2':
            search_id = input("Enter Movie ID to search: ").strip()
            search_by_id(movies, search_id)
        elif choice == choice == '3':
            regex_pattern = input("Enter Regular Expression for title search: ")
            search_by_title_regex(movies, regex_pattern)
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid menu option.")

if _name_ == "_main_":
    main()
