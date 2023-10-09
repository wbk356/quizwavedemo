# QuizWave: With Interactive Voice Assistant

QuizWave is a web-based quiz application with an interactive voice assistant that allows users to take quizzes using voice commands developed using Python, Flask, HTML, CSS, and JavaScript.


## About

The Voice-Enabled Quiz Game with Interactive Voice Assistant is an innovative project that 
combines voice recognition technology, gamification elements, and an interactive voice 
assistant to create an engaging and interactive quiz experience. The project aims to provide 
users with a fun and interactive way to test their knowledge and learn new information.
The system allows users to participate in a quiz game where questions are presented through 
voice prompts. The users can respond to the questions by speaking their answers aloud. The 
voice recognition technology is utilized to convert the spoken answers into text for evaluation. 
The system then evaluates the answers and provides instant feedback to the users regarding the 
correctness of their responses.
The project aims to enhance user interaction, encourage engagement, and provide an innovative 
approach to quiz games.


## Features

- User authentication and login system.
- Quiz-taking functionality.
- Score calculation.
- User-friendly web interface using Bootstrap.
- Interactive voice assistant integration.


## Technologies Used

- **Backend**: Python with Flask framework and MySQL database.
- **Frontend**: HTML, CSS, JavaScript, Bootstrap.
- **Voice Assistant Integration**: Alan Studio.
- **Database**: MySQL.
- **Development Environment**: Visual Studio Code.


## Getting Started

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/wbk356/quizwavedemo.git
    cd QuizWave
    ```

2. Set up a virtual environment (optional but recommended).
   
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install project dependencies.
    
    ```python
    pip install -r requirements.txt
    ```

4. Create a MySQL database and configure your database connection settings.
    
    ### Database Setup
    To run QuizWave, you need to set up a MySQL database. Follow these steps to configure and initialize the database:
    
    - Step 1: Install MySQL
        If you don't already have MySQL installed, download and install it from the official [MySQL](https://dev.mysql.com/downloads/installer/) website.

    - Step 2: Create a MySQL Database
        Open a terminal or MySQL command-line tool.

        Log in to MySQL using your credentials:

          ```
          mysql -u your_username -p
          ```
        Replace your_username with your MySQL username.
    
    - Step 3: Create a new database for QuizWave:
          
          ```
          CREATE DATABASE quizwavedb;
          ```
    
    - Step 3: Configure Database Connection. In your Flask application, configure the database connection settings in the app.py file. 
            
            

    - Step 4: Create Database Tables. You'll need to manually create the necessary tables for QuizWave in your database.  
            
        
             


            

5. Start the Flask application.
    
    ```python
    python app.py
    ```

6. Access the application in your web browser at http://localhost:5000.


## Usage

- Register for an account or log in if you already have one.
- Press Start to attend the quiz.
- Answer the quiz questions.
- After completing the quiz, view your score.



## Acknowledgments


- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Bootstrap](https://getbootstrap.com/)
- [Alan Studio](https://alan.app/)


## Contact

If you have any questions or suggestions, please feel free to contact us at valeedibnukhalidtk@gmail.com.





 
© 2023 - Valeed Ibnu Khalid T K