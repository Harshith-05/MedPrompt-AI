# MedPrompt-AI

 MedPrompt AI is an innovative medical question-and-answer system designed to empower users with accurate and concise information sourced from preloaded medical textbooks. This generative AI solution harnesses advanced natural language processing techniques to retrieve and generate meaningful responses to user queries, facilitating informed decision-making in medical contexts.

Requirements
Before running the MedPrompt AI application, ensure you have the following installed on your system:

Python 3.7 or later
pip (Python package manager)
Git (for cloning the repository)
Installation Instructions
Clone the Repository:

Open your terminal or command prompt and run the following command to clone the MedPrompt AI repository:

bash
Copy code
git clone [Clone this repo](https://github.com/Harshith-05/Medprompt-AI.git)


Navigate to the Project Directory:

Change into the project directory:

bash
Copy code
cd MedPrompt-AI
Create a Virtual Environment (Optional but Recommended):

It's a good practice to create a virtual environment for Python projects. You can do this using the following commands:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install Required Packages:

Use pip to install the necessary packages listed in the requirements.txt file (make sure you create this file in your project directory):

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt, you can manually install the packages used in the project:

bash
Copy code
pip install flask sentence-transformers faiss-cpu
Prepare the Medical Textbook:

Ensure you have a text file (e.g., medical_textbook.txt) that contains the medical information you want the chatbot to utilize. Place this file in the same directory as your Flask application code.

Run the Flask Application:

Start the Flask application by running the following command:

bash
Copy code
python app.py
The application will run on http://127.0.0.1:5000/ by default.

Access the Chatbot:

Open your web browser and navigate to http://127.0.0.1:5000/ to interact with MedPrompt AI. Enter your medical questions, and the chatbot will provide relevant answers based on the preloaded textbook.
Uploading Untitled and 10 more pages - Personal - Microsoft​ Edge 2024-10-06 17-27-47.mp4…
