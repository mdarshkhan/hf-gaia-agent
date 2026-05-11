import requests


def get_random_question():
    """Fetch a random question from the GAIA benchmark"""
    url = "https://agents-course-unit4-scoring.hf.space/random-question"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    
    return {"error": "Failed to fetch question"}


def get_all_questions():
    """Fetch all available questions from the GAIA benchmark"""
    url = "https://agents-course-unit4-scoring.hf.space/questions"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    
    return {"error": "Failed to fetch questions"}
