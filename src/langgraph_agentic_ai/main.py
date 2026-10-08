import streamlit as st
from src.langgraph_agentic_ai.ui.streamlit_ui.load_ui import LoadStreamlitUI
from src.langgraph_agentic_ai.llm.groq_llm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.ui.streamlit_ui.display_result import DisplayResultStreamlit

def load_langgraph_agentic_ai_app():
    '''
    Loads and runs the Langgraph Agentic AI application using Streamlit
    '''
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error : Failed to load user input")
        return

    user_message  = st.chat_input("Enter your message")

    if user_message:
        try:
            ## configure llm
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("ERROR:Failed to initialize the LLM Model")
                return

            usecase = user_input.get("Selected Usecase")

            if not usecase:
                st.error("Error : No use case selected ")
                return

            ## graph builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayResultStreamlit(usecase, user_message,graph).display_result_on_ui()
            except Exception as e:
                st.error(f"Error occured while building the graph : {e}")
                return
            

        except Exception as e:
            st.error(f"An error occured : {e}")
            return
