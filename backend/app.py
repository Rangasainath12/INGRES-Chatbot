from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import backend modules
from db.connection import connect_to_database, execute_query
from nlp.query_generator import generate_sql_query
from services.groundwater_service import generate_report
from nlp.translator import translate_text_english, translate_text_hindi

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_english(text):
    try:
        text.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        print(f"Received message: {user_message}")
        
        # Detect language and translate if not English
        if is_english(user_message):
            final_question = user_message
            detected_lang = "en-IN"
        else:
            final_question, detected_lang = translate_text_english(user_message)
            print(f"Detected language: {detected_lang}, translated to English: {final_question}")
        
        # Generate SQL query from the user's question
        sql_query = generate_sql_query(final_question)
        
        # Connect to the database
        db_connection = connect_to_database()
        if not db_connection:
            return jsonify({"response": "Sorry, I couldn't connect to the database. Please try again later."})
        
        # Execute the query
        results = execute_query(db_connection, sql_query)
        
        # Process results and generate a response
        if results:
            response = f"Based on the data, here's what I found: {results}"
        else:
            response = "I couldn't find any data matching your query. Could you try asking in a different way?"
        
        # Translate response back if original message wasn't in English
        if detected_lang != "en-IN":
            response, _ = translate_text_hindi(response)
        
        return jsonify({"response": response})
    
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({"response": "Sorry, I encountered an error processing your request. Please try again."})

@app.route('/action', methods=['POST'])
def action():
    try:
        data = request.json
        action_type = data.get('action', '')
        
        print(f"Received action: {action_type}")
        
        # Handle different action types
        if action_type == 'view_trends':
            response = "Here are the latest groundwater trends across India. The data shows significant changes in the following regions..."
        
        elif action_type == 'generate_report':
            report = generate_report()
            response = f"I've generated a comprehensive report on groundwater data: {report}"
        
        elif action_type == 'water_quality':
            response = "The water quality analysis shows varying levels of contaminants across different regions. Major concerns include..."
        
        elif action_type == 'rainfall_data':
            response = "The rainfall data for the past year shows above average precipitation in the northern regions and below average in the southern regions..."
        
        elif action_type == 'groundwater_levels':
            response = "Current groundwater levels are critically low in 24% of districts, moderate in 45%, and satisfactory in 31% of districts across the country..."
        
        elif action_type == 'water_conservation':
            response = "Here are some effective water conservation techniques being implemented: 1. Rainwater harvesting, 2. Micro-irrigation systems, 3. Groundwater recharge structures..."
        
        else:
            response = "I'm not sure how to handle that action. Please try one of the available quick actions or ask a question."
        
        return jsonify({"response": response})
    
    except Exception as e:
        print(f"Error in action endpoint: {str(e)}")
        return jsonify({"response": "Sorry, I encountered an error processing your request. Please try again."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)