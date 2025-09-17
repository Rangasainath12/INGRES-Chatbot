import os
import google.generativeai as genai

# 1. Configure the API key
try:
    genai.configure(api_key="AIzaSyAKVGLnh7VVGYhVk5zrohTg1a6yeUZ-OiA")
    
except KeyError:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")

# 2. Define your database schema
# This is the most critical part. The LLM needs this context to know your table's structure.
schema_string = """
CREATE TABLE water_data (
    id INT,
    state VARCHAR(100),
    year INT,
    rainfall_mm FLOAT,
    annual_extractable_resources FLOAT,
    groundwater_extraction FLOAT,
    category VARCHAR(20)
);
"""

# 3. Initialize the Gemini Pro model
# We create an instance of the Gemini Pro model to interact with the API.
model = genai.GenerativeModel('gemini-2.5-pro')

def generate_sql_query(user_question):
    """
    Generates an SQL query from a user's natural language question using the Gemini Pro API.
    
    Args:
        user_question (str): The question in plain English.
        
    Returns:
        str: The generated SQL query.
    """
    # 4. Construct the prompt
    # The prompt is a set of instructions and data that tells the LLM what to do.
    # It must be clear and direct.
    prompt = f"""
    You are a professional SQL query generator. Your task is to write a SQL query based on the user's request and the provided database schema.

    ### Instructions
    - Write only the SQL query.
    - Do not include any explanations, code blocks (```), or extra text.
    - Be precise and accurate with column and table names from the schema.
    - The output must be a single SQL statement.
    - If a request is not possible, state that clearly.

    ### Database Schema
    {schema_string}

    ### User Request
    {user_question}

    ### SQL Query
    """
    
    # 5. Send the prompt to the model and get the response
    # The generate_content method sends the request to the Gemini API.
    response = model.generate_content(prompt)
    
    # 6. Extract and clean the output
    # We take the raw text from the response and clean up any leading/trailing whitespace.
    sql_query = response.text.strip()
    
    # Optional: You can add more robust post-processing here if needed.
    
    return sql_query

# Example Usage:
if __name__ == "__main__":
    question1 = "What is the total groundwater extraction for each state in the year 2022?"
    query1 = generate_sql_query(question1)
    print(f"User Question: {question1}")
    print(f"Generated Query: {query1}\n")

    question2 = "List the states where the category is 'Safe' and the rainfall is above 2000 mm."
    query2 = generate_sql_query(question2)
    print(f"User Question: {question2}")
    print(f"Generated Query: {query2}\n")

    question3 = "Find the average rainfall for all years in Arunachal Pradesh."
    query3 = generate_sql_query(question3)
    print(f"User Question: {question3}")
    print(f"Generated Query: {query3}\n")