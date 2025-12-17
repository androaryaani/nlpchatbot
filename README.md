# Gemini GPT Persona Assistant

An intelligent chatbot powered by Google Gemini API with advanced NLP capabilities. This Streamlit application provides a conversational AI assistant with sentiment analysis, intent detection, and multi-language support (English & Hinglish).

---

##  Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup & Configuration](#setup--configuration)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [NLP Features Explained](#nlp-features-explained)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [API Key Setup](#api-key-setup)

---

## Features

### Core Features
- **Conversational AI** - Powered by Google Gemini 2.5 Flash model
- **Multi-language Support** - Responds in both English and Hinglish
- **Chat History** - Maintains conversation context
- **Real-time Processing** - Instant AI responses

### NLP Features
1. **Intent Detection**
   - Identifies user intent (greeting, help, coding, questions, etc.)
   
2. **Sentiment Analysis** 
   - Detects emotional tone (positive, negative, neutral, unclear)
   
3. **Keyword Extraction**
   - Extracts main keywords from user query
   
4. **Category Detection** 
   - Classifies conversation category (Tech, AI/ML, Learning, Creative, General)
   
5. **NLP Analytics Dashboard** 
   - Expandable panel showing all NLP insights

---

## Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Google API Key** (Gemini API)
- **Internet Connection**

---

## 🚀 Installation

### Step 1: Clone or Download Project
```bash
cd c:\5th\ sem\chtbot
```

### Step 2: Install Required Packages
```bash
pip install streamlit google-generativeai python-dotenv
```

Or install from requirements:
```bash
pip install -r requirements.txt
```

**Alternative (with conda):**
```bash
conda create -n chtbot python=3.10
conda activate chtbot
pip install streamlit google-generativeai python-dotenv
```

---

## ⚙️ Setup & Configuration

### Step 1: Get Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy your API key

### Step 2: Configure Environment

**Option A: Using `.env` file (Recommended for local development)**

1. Open `.env` file in project root
2. Add your API key:
```env
GOOGLE_API_KEY=your-google-api-key-here
```

**Option B: Using Streamlit Secrets (Recommended for deployment)**

1. Create/edit `.streamlit/secrets.toml`
2. Add your API key:
```toml
GOOGLE_API_KEY = "your-google-api-key-here"
```

**Option C: Using Environment Variables**
```bash
set GOOGLE_API_KEY=your-google-api-key-here
```

---

## ▶️ How to Run

### Option 1: Using Streamlit (Recommended)
```bash
streamlit run app.py
```

The app will open in your browser at: `http://localhost:8501`

### Option 2: Using Python
```bash
python app.py
```

**Note:** Direct Python execution won't work well with Streamlit. Use `streamlit run` instead.

---

## 💬 Usage Guide

### Basic Usage
1. **Start the app** using `streamlit run app.py`
2. **Enter your query** in the text input field
3. **Read the response** from the AI assistant
4. **View NLP insights** by clicking "NLP Analysis" dropdown

### Examples

**Tech/Coding Questions:**
```
"How do I create a list in Python?"
"Explain JavaScript arrow functions"
"What's the difference between SQL and NoSQL?"
```

**Hindi/Hinglish:**
```
"Python mein loop kaise likhe?"
"Machine learning kya hai?"
"API banane ke liye kaun-sa language use karein?"
```

**General Questions:**
```
"Tell me about artificial intelligence"
"How does machine learning work?"
"What is NLP?"
```

### NLP Analysis Panel
Click the **"NLP Analysis"** dropdown to see:
- **Sentiment:** Emotional tone of your message
- **Category:** Type of conversation (Tech, AI, Learning, etc.)
- **Intent:** What you're trying to do
- **Keywords:** Main topics from your message

---

## NLP Features Explained

### 1. Intent Detection
Analyzes your message to identify your primary intent:
- `greeting` - Hello, Hi, Namaste
- `help` - Help, Guide, Teach, Explain
- `code` - Programming, Python, Debug
- `question` - What, Why, When, How
- `command` - Create, Build, Generate
- `emotion` - Happy, Angry, Confused
- `info` - Tell, Information, Define

### 2. Sentiment Analysis
Detects emotional sentiment in your message:
```
 Positive   - Contains good, great, love, awesome
 Negative   - Contains bad, hate, terrible, error
 Neutral    - Contains ok, fine, normal
 Unclear    - No clear sentiment detected
```

### 3. Keyword Extraction
Extracts up to 5 most important keywords:
- Removes common words (the, a, is, etc.)
- Prioritizes meaningful words
- Helps understand main topics

### 4. Category Detection
Classifies conversation into categories:
```
 Tech & Coding       - Programming, API, Database
 AI & ML             - Machine Learning, Neural Networks
 Learning            - Tutorial, Course, Explain
 Creative            - Design, Art, Story
 General             - General queries```

---

## 📁 Project Structure

```
chtbot/
├── app.py                          # Main Streamlit application
├── .env                            # Environment variables (API key)
├── .streamlit/
│   └── secrets.toml               # Streamlit secrets
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## 📦 Dependencies

```
streamlit==1.28.0+
google-generativeai==0.3.0+
python-dotenv==1.0.0+
```

Create `requirements.txt`:
```
streamlit
google-generativeai
python-dotenv
```

---

## 🐛 Troubleshooting

### Issue 1: "API key not found"
**Solution:**
- Check if `.env` file exists and has `GOOGLE_API_KEY=...`
- Or check `.streamlit/secrets.toml` has `GOOGLE_API_KEY = "..."`
- Restart the app after adding the key

### Issue 2: "GenerativeModel.__init__() got an unexpected keyword argument"
**Solution:**
- Update google-generativeai package: `pip install --upgrade google-generativeai`

### Issue 3: App shows "Error: No content in response"
**Solution:**
- Check your API key is valid
- Ensure you have internet connection
- Try a simpler query

### Issue 4: Slow responses
**Solution:**
- Reduce `max_output_tokens` in `app.py` (currently 800)
- Use lower `temperature` for faster, more deterministic responses

### Issue 5: ModuleNotFoundError
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue 6: Port 8501 already in use
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

---

## 🔐 API Key Setup (Detailed)

### Getting a Free Google Gemini API Key

1. **Visit Google AI Studio**
   - Go to: https://aistudio.google.com/app/apikey

2. **Create New API Key**
   - Click "Create API Key"
   - Select "Create API key in new project"
   - Copy the generated key

3. **Add to Project**
   ```env
   GOOGLE_API_KEY=AIzaSyC...your...key...here
   ```

4. **Verify It Works**
   - Run the app and send a test message
   - If no error, key is working!

**⚠️ Important Security Notes:**
- **Never commit `.env` to Git** - Add to `.gitignore`
- **Keep your API key private**
- **Don't share your key publicly**
- For production, use environment variables or secure vaults

---

## 🎯 Configuration Options

Edit `app.py` to customize:

### Change AI Model
```python
model = genai.GenerativeModel("models/gemini-1.5-pro")  # Faster model
# Or
model = genai.GenerativeModel("models/gemini-2.5-flash")  # Cheaper model
```

### Adjust Response Settings
```python
generation_config={
    "temperature": 0.3,        # 0=deterministic, 1=creative
    "max_output_tokens": 800   # Response length
}
```

### Modify System Prompt
Edit the `SYSTEM_PROMPT` variable to change assistant behavior.

---

## 📞 Support & Issues

If you encounter issues:
1. Check the **Troubleshooting** section
2. Verify your API key is valid
3. Try a simple query like "Hello"
4. Check internet connection
5. Review error messages in terminal

---

## 🚀 Next Steps & Enhancements

Potential improvements:
- [ ] Add conversation export to PDF/TXT
- [ ] Implement conversation search
- [ ] Add voice input/output
- [ ] Support for more languages
- [ ] Database for chat history
- [ ] User authentication
- [ ] Custom knowledge base integration
- [ ] Multi-user support

---

## 📄 License

Free to use and modify for educational purposes.

---

## 👨‍💻 Author

Created as a 5th Semester AI/NLP project.

---

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io)
- [Google Generative AI Docs](https://ai.google.dev)
- [Streamlit Secrets](https://docs.streamlit.io/develop/concepts/connections/secrets-management)

---

**Enjoy your AI Assistant! 🤖**
