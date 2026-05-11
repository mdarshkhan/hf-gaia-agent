import requests


def submit_answers(answers):
    """
    Submit answers to the GAIA evaluation framework.
    
    Args:
        answers: List of dicts with 'task_id' and 'submitted_answer'
    """
    url = "https://agents-course-unit4-scoring.hf.space/submit"
    
    payload = {
        "username": "Arshkhan7",
        "agent_code": "https://github.com/mdarshkhan/hf-gaia-agent/tree/main",
        "answers": answers
    }
    
    response = requests.post(url, json=payload)
    
    return response.json()


if __name__ == "__main__":
    # Example submission
    example_answers = [
        {
            "task_id": "example_task_id",
            "submitted_answer": "example_answer"
        }
    ]
    
    result = submit_answers(example_answers)
    print(result)
