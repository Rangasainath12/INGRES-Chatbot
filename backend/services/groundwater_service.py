# Handles fetching + formatting results
# report_generator.py

import os
import google.generativeai as genai

# Configure the API key
try:
    genai.configure(api_key='AIzaSyAKVGLnh7VVGYhVk5zrohTg1a6yeUZ-OiA')
    # genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")

model = genai.GenerativeModel('gemini-2.5-pro')

def generate_report(user_question, query_results):
    """
    Analyzes query results and generates a human-readable report.
    """
    # Convert the list of dictionaries to a readable string format
    data_string = "\n".join([str(row) for row in query_results])

    # Construct the prompt for analysis
    prompt = f"""
    You are a professional data analyst. Your task is to analyze the provided data and generate a clear, concise report based on the user's original question.

    ### Instructions
    - Identify key insights and trends in the data.
    - Do not make up any information. Base your report strictly on the data provided.
    - Summarize the findings in a paragraph, followed by a bulleted list of key takeaways.
    - The tone should be professional and easy to understand for a non-technical audience.
    
    ### User Question
    {user_question}
    
    ### Data
    {data_string}
    
    ### Report
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred while generating the report: {e}"