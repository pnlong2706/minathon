import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Mentor data with name, email, and birthday
mentors_data = [
    {"name": "John Doe", "email": "john@example.com", "birthday": "1990-01-01",
     "characteristics": "Experienced, patient, friendly", "hobbies": "Reading, hiking",
     "location": "New York", "language": "English", "programming_language": "Python", "job": "Software Engineer"},
    {"name": "Alice Smith", "email": "alice@example.com", "birthday": "1985-05-15",
     "characteristics": "Detail-oriented, problem solver", "hobbies": "Playing guitar, painting",
     "location": "San Francisco", "language": "English", "programming_language": "Java", "job": "Data Scientist"},
    {"name": "Bob Johnson", "email": "bob@example.com", "birthday": "1988-11-30",
     "characteristics": "Creative, innovative", "hobbies": "Cooking, traveling",
     "location": "Los Angeles", "language": "English", "programming_language": "JavaScript", "job": "Web Developer"},
    {"name": "Emma Brown", "email": "emma@example.com", "birthday": "1992-03-20",
     "characteristics": "Analytical, logical", "hobbies": "Playing piano, photography",
     "location": "Chicago", "language": "English", "programming_language": "C++", "job": "Software Engineer"},
    {"name": "Michael Davis", "email": "michael@example.com", "birthday": "1980-07-10",
     "characteristics": "Friendly, approachable", "hobbies": "Swimming, gardening",
     "location": "Miami", "language": "English", "programming_language": "Ruby", "job": "Full Stack Developer"},
    {"name": "Sophia Wilson", "email": "sophia@example.com", "birthday": "1987-09-25",
     "characteristics": "Patient, good listener", "hobbies": "Yoga, reading",
     "location": "Seattle", "language": "English", "programming_language": "Python", "job": "Machine Learning Engineer"},
    {"name": "David Lee", "email": "david@example.com", "birthday": "1975-12-05",
     "characteristics": "Adaptable, quick learner", "hobbies": "Fishing, hiking",
     "location": "Denver", "language": "English", "programming_language": "Java", "job": "Software Architect"},
    {"name": "Emily Taylor", "email": "emily@example.com", "birthday": "1993-06-18",
     "characteristics": "Organized, detail-oriented", "hobbies": "Dancing, cooking",
     "location": "Boston", "language": "English", "programming_language": "JavaScript", "job": "Frontend Developer"},
    {"name": "James Brown", "email": "james@example.com", "birthday": "1982-04-12",
     "characteristics": "Energetic, enthusiastic", "hobbies": "Running, painting",
     "location": "Atlanta", "language": "English", "programming_language": "Python", "job": "Data Engineer"},
    {"name": "Olivia Martinez", "email": "olivia@example.com", "birthday": "1978-08-08",
     "characteristics": "Calm, composed", "hobbies": "Meditation, cooking",
     "location": "Houston", "language": "English", "programming_language": "Python", "job": "Software Engineer"},
    # Add more mentors data as needed
]

# Convert mentor data into DataFrame
mentors_df = pd.DataFrame(mentors_data)

# Concatenate mentor features for TF-IDF vectorization
mentors_df['features'] = mentors_df['characteristics'] + ' ' + mentors_df['hobbies'] + ' ' + \
                          mentors_df['location'] + ' ' + mentors_df['language'] + ' ' + \
                          mentors_df['programming_language'] + ' ' + mentors_df['job']

# TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(mentors_df['features'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_mentors(name, location=None, hobbies=None, language=None, programming_language=None, job=None):
    # Find index of the mentor with given name
    mentor_index = mentors_df[mentors_df['name'] == name].index[0]
    
    # Filter mentors based on user-specified criteria
    filtered_mentors_df = mentors_df.copy()
    if location:
        filtered_mentors_df = filtered_mentors_df[filtered_mentors_df['location'] == location]
    if hobbies:
        filtered_mentors_df = filtered_mentors_df[filtered_mentors_df['hobbies'].str.contains(hobbies, case=False)]
    if language:
        filtered_mentors_df = filtered_mentors_df[filtered_mentors_df['language'] == language]
    if programming_language:
        filtered_mentors_df = filtered_mentors_df[filtered_mentors_df['programming_language'] == programming_language]
    if job:
        filtered_mentors_df = filtered_mentors_df[filtered_mentors_df['job'] == job]
    
    # Compute similarity scores for filtered mentors
    tfidf_matrix_filtered = tfidf_vectorizer.transform(filtered_mentors_df['features'])
    mentor_similarities = cosine_similarity(tfidf_matrix_filtered, tfidf_matrix_filtered)
    
    # Get similarity scores for the mentor
    mentor_sim_scores = list(enumerate(mentor_similarities[mentor_index]))
    
    # Sort mentors by similarity scores
    mentor_sim_scores = sorted(mentor_sim_scores, key=lambda x: x[1], reverse=True)
    
    # Exclude the mentor itself
    mentor_sim_scores = mentor_sim_scores[1:]
    
    # Get top 3 similar mentors
    top_mentors_indices = [i[0] for i in mentor_sim_scores[:3]]
    
    # Return recommended mentors
    recommended_mentors = filtered_mentors_df.iloc[top_mentors_indices]['name']
    return recommended_mentors.tolist()

# Example usage:
# Replace 'John Doe' with the name of the mentor you want to find recommendations for
# You can also provide additional filter parameters such as location, hobbies, language, programming language, and job
recommended_mentors = recommend_mentors('John Doe', location='New York', programming_language='Python')
print("Recommended mentors for John Doe:")
print(recommended_mentors)
