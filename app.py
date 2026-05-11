from tools import get_random_question
from agent import SimpleAgent


def main():
    """Main application entry point."""
    
    # Initialize agent
    agent = SimpleAgent()
    
    # Fetch a random question from GAIA
    question_data = get_random_question()
    
    print("\n" + "="*60)
    print("GAIA Agent - Question Solver")
    print("="*60)
    print("\nQuestion Data:\n")
    print(question_data)
    
    # Check if question was retrieved successfully
    if "question" in question_data:
        question = question_data["question"]
        
        print("\n" + "-"*60)
        print("Agent Thinking...")
        print("-"*60 + "\n")
        
        # Generate answer
        answer = agent.think(question)
        
        print("\nGenerated Answer:\n")
        print(answer)
        print("\n" + "="*60)
        
    else:
        print("\n❌ Failed to retrieve question")
        print("="*60)


if __name__ == "__main__":
    main()
