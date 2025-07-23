🛒 E-commerce AI Agent


This project builds an AI-powered agent that can answer natural language questions about e-commerce data by:

Translating the question into SQL,

Executing it on a local database,

Returning a human-readable answer, and

(Bonus) Visualizing the results or streaming responses.

📌 Features
🧠 Connects to a local LLM (like Ollama, Mistral, or Code Llama)

🗃️ Uses SQL (SQLite) for querying real e-commerce datasets

🔌 Exposes API endpoints via FastAPI for frontend/backend integration

🔍 Converts natural language questions → SQL queries → answers

📊 Optional visualizations (e.g., bar charts, pie charts)

🔁 Optional event-streaming responses (real-time interaction feel)



🚀 Getting Started
Clone the repo
git clone https://github.com/Yuvashree-2003/ecommerce_ai_agent.git
cd ecommerce_ai_agent

Install dependencies
pip install -r requirements.txt

Setup SQLite DB
python main.py  # or run any db_init.py if available

Run the app
uvicorn main:app --reload

Access the API
Open in browser:
http://127.0.0.1:8000/docs (Swagger UI)

🧠 Local LLM Setup (Optional but recommended)
You can use Ollama to run models like:

ollama run mistral
Make sure the LLM is running locally so that your app can access it via HTTP.

📈 Bonus Features
Graphical Output: Queries like "Show top 5 products by sales" will return a bar chart.

Streaming: Answers can be streamed using async endpoints with FastAPI.

💡 Example Questions
"What were the top 5 selling products last month?"

"How many users placed orders this week?"

"Show me total ad spend by product category."



