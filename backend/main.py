
# Entry point for FastAPI app
# main_app.py

import os
import sys
'''# Get the path to the current directory (where main.py is)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the 'backend' directory to the Python path
backend_dir = os.path.join(current_dir, 'backend')
sys.path.append(backend_dir)

# Now you can import modules from the subdirectories within 'backend'
# This treats 'backend' as a package and its subdirectories as subpackages
# Assume these files are in the same directory'''
from db.connection import connect_to_database, execute_query
from nlp.query_generator import generate_sql_query
from services.groundwater_service import generate_report
from nlp.translator import translate_text_english, translate_text_hindi  # Import translators

def is_english(text):
    try:
        text.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

def main():
    db_connection = connect_to_database()
    if not db_connection:
        return

    print("\n💧 Welcome to the Water Data Insight Tool! 💧")
    print("Ask a question about the water data, e.g., 'What is the average rainfall for each state?'")
    print("Type 'exit' to quit.")

    try:
        while True:
            user_question = input("\n>> Your Question: ")
            if user_question.lower() == 'exit':
                break

            # Detect language and translate only if not English
            if is_english(user_question):
                final_question = user_question
                detected_lang = "en-IN"
            else:
                final_question, detected_lang = translate_text_english(user_question)
                print(f"Detected language: {detected_lang}, translated to English: {final_question}")

            # Step 1: Generate SQL query
            sql_query = generate_sql_query(final_question)
            print(f"Generated SQL: {sql_query}")

            if not sql_query or not sql_query.strip():
                print("❌ Could not generate a valid SQL query.")
                continue

            # Step 2: Execute the query and get results
            results = execute_query(db_connection, sql_query, fetch=True)
            
            if results is None:
                print("❌ Failed to execute query.")
                continue

            # Step 3: Analyze results and generate a report
            print("\nGenerating report from results...")
            report = generate_report(final_question, results)

            # Step 4: Translate report back if needed
            if not detected_lang.lower().startswith('en'):
                # Example for Hindi, you can add more languages as needed
                report = translate_text_hindi(report, detected_lang)
                print("\n✅ Insights Report (translated):")
            else:
                print("\n✅ Insights Report:")

            print(report)

    finally:
        if db_connection and db_connection.is_connected():
            db_connection.close()
            print("\nMySQL connection is closed.")

if __name__ == "__main__":
    main()
