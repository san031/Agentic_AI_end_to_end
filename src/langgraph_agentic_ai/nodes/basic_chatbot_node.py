from src.langgraph_agentic_ai.state.state import State

class BasicChatbotNode:
    """
    A basic chatbot login implementation
    """

    def __init__(self,model):
        self.model = model

    def process(self, state:State)->dict:
        """
        processes the input state and generates a chatbot response
        """

        return {
            "messages" : self.llm.invoke(state["messages"])
        }