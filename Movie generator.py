from faker import Faker
import random
import csv

fake = Faker()

def generate_drama_data(num_records):
    genres = ["Romance", "Action", "Fantasy", "Thriller", "Comedy", "Drama", "Historical", "Mystery"]
    seasons = ["Winter", "Spring", "Summer", "Fall"]
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    networks = ["tvN", "SBS", "JTBC", "KBS2", "MBC", "OCN", "Netflix"]
    ratings = ["15", "12", "18", "All"]
    
    data = []
    
    for _ in range(num_records):
        title = fake.catch_phrase()
        year = fake.year()
        director = fake.name()
        writer = fake.name()
        country = "South Korea"
        genre = random.choice(genres)
        episodes = 16
        duration = 70
        season = random.choice(seasons)
        weekday = random.choice(weekdays)
        network = random.choice(networks)
        rating = random.choice(ratings)
        description = fake.sentence(nb_words=12)
        score = round(random.uniform(7.0, 9.5), 1)
        
        data.append([
            title, year, director, writer, country, genre, episodes, 
            duration, season, weekday, network, rating, description, score
        ])
        
    return data

def save_to_csv(filename, data):
    headers = ["Title", "Year", "Director", "Writer", "Country", "Genre", "Episodes", 
               "Duration", "Season", "Weekday", "Network", "Rating", "Description", "Score"]

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# Generate 10,000 records
drama_data = generate_drama_data(10000)

# Save to CSV
save_to_csv("/mnt/data/kdrama_data.csv", drama_data)

"/mnt/data/kdrama_data.csv"
