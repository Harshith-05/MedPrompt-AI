from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
import faiss

# Initialize Flask app
app = Flask(__name__)

# Load Sentence Transformer for encoding sentences for FAISS
sentence_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load textbook and encode sentences for FAISS
def load_textbook(filepath):
    with open(filepath, 'r') as f:
        sentences = f.readlines()
    sentence_embeddings = sentence_model.encode(sentences)
    
    # Create FAISS index
    index = faiss.IndexFlatL2(sentence_embeddings.shape[1])
    index.add(sentence_embeddings)
    
    return sentences, index

# Load the textbook (e.g., "medical_textbook.txt")
sentences, faiss_index = load_textbook('medical_textbook.txt')

# Function to search relevant text using FAISS
def search_query(query, faiss_index, sentences, top_k=5):
    query_embedding = sentence_model.encode([query])
    distances, indices = faiss_index.search(query_embedding, top_k)
    
    valid_results = []
    for i in indices[0]:
        if i < len(sentences):  # Ensure index is within bounds
            valid_results.append(sentences[i])
    
    # If no valid results are found, return None
    if len(valid_results) == 0:
        return None
    
    return " ".join(valid_results)

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    user_query = request.form['question']
    
    # Step 1: Retrieve relevant context from the uploaded text
    retrieved_text = search_query(user_query, faiss_index, sentences)
    
    # If no relevant data found, return insufficient data
    if not retrieved_text:
        answer = "Insufficient data in uploaded file."
    else:
        answer = retrieved_text
    
    return render_template('index.html', question=user_query, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)


