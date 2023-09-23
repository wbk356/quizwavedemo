from flask import Flask, render_template, request, redirect, session, url_for, flash
import mysql.connector
import pymysql
from flask_mysqldb import MySQL
import secrets
import speech_recognition as sr
import pyttsx3
import json




app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'qadmin'
app.config['MYSQL_PASSWORD'] = 'Waleed@123#'
app.config['MYSQL_DB'] = 'quizwave'



mysql = MySQL(app)


db = pymysql.connect(
    host="localhost",
    user="qadmin",
    password="Waleed@123#",
    database="quizwave"
)

@app.route('/')
def home():
     # Check if the user is logged in
    if 'user_id' in session:
        return render_template('index.html', name=session['name'])
    else:
        return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


@app.route('/register', methods=['POST'])
def register():
    # Get the form data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    # Create a cursor
    cur = mysql.connection.cursor()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s ", (email))
    
    existing_user = cursor.fetchone()
    if existing_user:
            flash('Email already exists. Please choose a different Email.', 'error')
            return redirect(url_for('signup'))

    # Execute the query to insert the signup values into the database
    cur.execute("INSERT INTO users (username, password, email ) VALUES (%s, %s, %s)", (name, password, email))

    # Commit the changes
    mysql.connection.commit()

    # Close the cursor
    cur.close()
   

    # Redirect to the login page
    flash('Registration successful! You can now login.')
    return redirect(url_for('login'))
    #return redirect('/login')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor()

        # Check if the email and password exist in the database
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            # User is authenticated, store user data in session
            session['user_id'] = user[0]
            session['email'] = user[3]
            session['name'] = user[1]
            quiz_id = 123
            session['quiz_id'] = quiz_id
            
            flash('Succesfully Loggedin.')
            # Redirect to the index page or any other desired page
            return redirect('/')
        else:
            # Invalid credentials, show error message
            flash('Invalid email or password. Please try again.')
            return render_template('login.html')
        
    return render_template('login.html')


@app.route('/logout')
def logout():
    # Clear session data
    session.clear()

    # Redirect to the login page
    return redirect(url_for('login'))


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'user_id' in session:
        if request.method == 'POST':
            # Handle quiz submission
            user_answers = []
            for key, value in request.form.items():
                if key.startswith('answer'):
                    option_text = value  # Store the option text
                    user_answers.append(option_text)

            # Print the selected options for debugging
            print(user_answers)

            # Retrieve questions from the database
            questions_json = retrieve_questions_from_database()
            questions = json.loads(questions_json)

            # Calculate the user's score based on the submitted answers
            score = calculate_user_score(user_answers, questions)
            print(score)

            # Save the user's score in the database
            save_user_score(session['user_id'], score)

            # Retrieve the user's global ranking
            ranking = retrieve_user_ranking(session['user_id'])

            return render_template('result.html', score=score, ranking=ranking)
        else:
            questions_json = retrieve_questions_from_database()
            questions = json.loads(questions_json)
            return render_template('quiz.html', questions=questions)
    else:
        return redirect('/login')






    #questions = retrieve_questions_from_database()
    
    # Render the quiz template with the questions
    #return render_template('quiz.html', questions=questions)
    # Implement quiz logic (e.g., retrieve questions, track user progress)
    # Render the quiz template with necessary data
    






@app.route('/addquestion', methods=['GET', 'POST'])
def addquestion():
    return render_template('addquestion.html')

@app.route('/add_question', methods=['POST'])
def add_question():
    # Retrieve the form data
    question = request.form.get('question')
    option1 = request.form.get('option1')
    option2 = request.form.get('option2')
    option3 = request.form.get('option3')
    option4 = request.form.get('option4')
    correct_answer = request.form.get('correct_answer')
    
    cur = mysql.connection.cursor()
    
    cur.execute("INSERT INTO question (question_text, option1, option2, option3, option4, correct_answer ) VALUES (%s, %s, %s, %s, %s, %s)", (question, option1, option2, option3, option4, correct_answer))

    # Commit the changes
    mysql.connection.commit()

    # Close the cursor
    cur.close()
    flash('Added.')
    return redirect(url_for('addquestion'))








def retrieve_questions_from_database():
    # Establish a connection to the MySQL database

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Define the SQL query to retrieve questions from the database
    query = "SELECT * FROM question"

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Create an empty list to store the questions
    questions = []

    # Iterate over the rows and extract question data
    for row in rows:
        question = {
            'id': row[0],  # assuming the question ID is stored in the 1st column
            'question': row[1],  # the question text is stored in the 2nd column
            'options': [
                {'id': 'option-1', 'text': row[2]},  # assuming option IDs start with 'option-1' and are stored in columns 3 to 6
                {'id': 'option-2', 'text': row[3]},
                {'id': 'option-3', 'text': row[4]},
                {'id': 'option-4', 'text': row[5]}
            ],
            'answer': row[6]  # the correct answer is stored in the 7th column
        }
        questions.append(question)
        
        

    # Close the cursor and database connection
    #cursor.close()
    #db.close()
    
    questions_json = json.dumps(questions)
    
    return questions_json

    #return questions





def calculate_user_score(user_answers, questions):
    correct_answers = 0
    new=[]
    new=['option-1','option-3','option-4','option-1']
    for element in user_answers:
        if element in new:
            correct_answers += 1

    

    total_questions = len(questions)
    score = (correct_answers / total_questions) * 100

    return score






def save_user_score(user_id, score):
    # Establish a connection to the MySQL database

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Check if the user's score already exists in the result table
    query = "SELECT * FROM result WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    if result:
        # If the user's score exists, update it
        update_query = "UPDATE result SET score = %s WHERE user_id = %s"
        cursor.execute(update_query, (score, user_id))
    else:
        # If the user's score does not exist, insert a new record
        insert_query = "INSERT INTO result (user_id, score) VALUES (%s, %s)"
        cursor.execute(insert_query, (user_id, score))

    # Commit the changes to the database
    db.commit()

    # Close the cursor and database connection
    cursor.close()
    #db.close()





def retrieve_correct_answers():
    # Establish a connection to the MySQL database

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Define the SQL query to retrieve the correct answers from the question table
    query = "SELECT correct_answer FROM question"

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Create an empty list to store the correct answers
    correct_answers = []

    # Iterate over the rows and extract the correct answer
    for row in rows:
        correct_answer = row[0]  # Assuming the correct_answer column is in the first position (0 index)
        correct_answers.append(correct_answer)

    # Close the cursor and database connection
    cursor.close()
    #db.close()

    return correct_answers





def retrieve_user_ranking(user_id):
    # Establish a connection to the MySQL database

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Define the SQL query to retrieve the user's global ranking
    query = "SELECT COUNT(*) FROM users,result WHERE score > (SELECT score FROM result WHERE user_id = %s)"

    # Execute the query with the user ID as a parameter
    cursor.execute(query, (user_id,))

    # Fetch the ranking value from the result
    ranking = cursor.fetchone()[0]

    # Close the cursor and database connection
    cursor.close()
    #db.close()

    return ranking


def get_current_user_id():
    if 'user_id' in session:
        return session['user_id']
    else:
        return None
    



def get_current_quiz_id():
    if 'quiz_id' in session:
        return session['quiz_id']
    else:
        return None










if __name__ == '__main__':
    app.run(debug=True)
