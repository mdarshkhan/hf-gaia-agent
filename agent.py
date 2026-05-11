from transformers import pipeline


class SimpleAgent:
    """A simple autonomous agent that uses an LLM to reason through questions."""
    
    def __init__(self, model="gpt2"):
        """
        Initialize the agent with an LLM.
        
        Args:
            model: HuggingFace model ID (default: gpt2)
        """
        self.llm = pipeline(
            "text-generation",
            model=model
        )
    
    def think(self, question):
        """
        Think through a question and generate an answer.
        
        Args:
            question: The question to solve
            
        Returns:
            The generated answer
        """
        prompt = f"""
You are an intelligent AI agent.

Solve the following question carefully.

Question:
{question}

Return ONLY the final answer.
"""
        
        result = self.llm(
            prompt,
            max_new_tokens=50
        )
        
        return result[0]["generated_text"]
