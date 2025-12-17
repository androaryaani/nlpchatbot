import streamlit as st
import google.generativeai as genai
import os
import re
from collections import Counter
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Gemini GPT Persona Assistant",
    page_icon="🤖",
    layout="centered"
)

# ================== API KEY & MODEL HANDLING ==================
# Load key from: Windows env var → .env file → .streamlit/secrets.toml
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

# Keep the key and model in session state so UI can load even if key is missing
if "GEMINI_API_KEY" not in st.session_state:
    st.session_state["GEMINI_API_KEY"] = GEMINI_API_KEY

def _init_model(key):
    genai.configure(api_key=key)
    return genai.GenerativeModel("models/gemini-2.5-flash")

if st.session_state.get("GEMINI_API_KEY"):
    try:
        st.session_state["model"] = _init_model(st.session_state["GEMINI_API_KEY"])
    except Exception:
        st.session_state["model"] = None
else:
    st.warning("❌ Gemini API key not found — enter the key in Sidebar to continue")
    st.session_state["model"] = None

# ================== SYSTEM PROMPT ==================
SYSTEM_PROMPT = """
You are a GPT-style Personal Assistant.

STRICT RULES (MUST FOLLOW):
- NEVER start with greetings like Hello, Hi, How can I help
- NEVER introduce yourself
- Directly answer the user's question
- If user writes in Hindi/Hinglish → respond in Hinglish
- Use clear headings, bullet points & step-by-step explanations
- Be professional, concise, and helpful
"""

# ================== NLP HELPER FUNCTIONS ==================

def detect_intent(text):
    """Detect user intent from query"""
    text_lower = text.lower()
    
    intents = {
        "greeting": r"\b(hello|hi|hey|namaste|hlo|hii)\b",
        "help": r"\b(help|guide|teach|explain|how|tutorial)\b",
        "code": r"\b(code|programming|python|js|function|debug|error)\b",
        "question": r"\b(what|why|when|where|who|how)\b",
        "command": r"\b(do|make|create|write|generate|build)\b",
        "emotion": r"\b(angry|sad|happy|frustrated|excited|confused)\b",
        "info": r"\b(tell|info|information|about|define)\b"
    }
    
    detected = []
    for intent, pattern in intents.items():
        if re.search(pattern, text_lower):
            detected.append(intent)
    
    return detected if detected else ["general"]

def detect_sentiment(text):
    """Simple sentiment analysis"""
    text_lower = text.lower()
    
    positive_words = r"\b(good|great|excellent|amazing|love|awesome|perfect|thanks|thank you)\b"
    negative_words = r"\b(bad|hate|terrible|awful|angry|sad|stupid|useless|error|wrong)\b"
    neutral_words = r"\b(ok|fine|normal|average)\b"
    
    pos_count = len(re.findall(positive_words, text_lower))
    neg_count = len(re.findall(negative_words, text_lower))
    neu_count = len(re.findall(neutral_words, text_lower))
    
    if pos_count > neg_count:
        return "😊 Positive"
    elif neg_count > pos_count:
        return "😞 Negative"
    elif neu_count > 0:
        return "😐 Neutral"
    else:
        return "❓ Unclear"

def extract_keywords(text, num_keywords=5):
    """Extract main keywords from text"""
    # Remove common words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have',
        'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
        'what', 'how', 'why', 'where', 'when', 'who', 'which', 'this', 'that',
        'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
    }
    
    words = re.findall(r'\b[a-z]+\b', text.lower())
    keywords = [w for w in words if w not in stop_words and len(w) > 2]
    
    word_freq = Counter(keywords)
    return [word for word, _ in word_freq.most_common(num_keywords)]

def detect_category(text):
    """Detect conversation category"""
    text_lower = text.lower()
    
    categories = {
        "Tech & Coding": r"\b(python|javascript|code|program|api|database|html|css|error|debug)\b",
        " AI & ML": r"\b(ai|machine learning|neural|nlp|deep learning|model|training|data)\b",
        " Learning": r"\b(learn|tutorial|course|lesson|explain|educate|teach|study)\b",
        " Creative": r"\b(design|art|write|create|story|poem|creative)\b",
        " General": r"\b(what|how|why|help|tell|general)\b"
    }
    
    for category, pattern in categories.items():
        if re.search(pattern, text_lower):
            return category
    
    return "General"

# ================== PAGE CONFIG ==================

# ================== SESSION STATE ==================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ================== UI HEADER ==================
st.markdown("""
<h2 style='text-align:center;'> Personal Assistant</h2>
<p style='text-align:center; color:gray;'>Gemini • NLP Powered • Smart Responses</p>
<hr>
""", unsafe_allow_html=True)

# ================== SIDEBAR ==================
with st.sidebar:
    st.title("⚙️ Settings")
    
    # Clear history button
    if st.button("🗑️ Clear Chat History", key="clear_history"):
        st.session_state.chat_history = []
        st.success("✅ Chat cleared!")
        st.rerun()
    
    st.divider()
    
    # Show API Key Status
    st.subheader("🔑 API Key Status")
    if st.session_state.get("GEMINI_API_KEY"):
        st.success("✅ API Key loaded & ready")
    else:
        st.error("❌ No API Key found")

# ================== SHOW CHAT ==================
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# ================== USER INPUT ==================
user_input = st.chat_input("Ask anything...")

if user_input:
    # ================== NLP ANALYSIS ==================
    intents = detect_intent(user_input)
    sentiment = detect_sentiment(user_input)
    keywords = extract_keywords(user_input, num_keywords=4)
    category = detect_category(user_input)
    
    # Show user message with analysis in sidebar
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Show NLP insights
    with st.expander("NLP Analysis", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Sentiment:** {sentiment}")
            st.write(f"**Category:** {category}")
        with col2:
            st.write(f"**Intent:** {', '.join([i.capitalize() for i in intents])}")
            st.write(f"**Keywords:** {', '.join(keywords)}")

    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    # ================== BUILD GEMINI PROMPT ==================
    conversation = f"""
### SYSTEM INSTRUCTION (STRICT)
{SYSTEM_PROMPT}

IMPORTANT:
- Do NOT greet
- Do NOT introduce yourself
- Answer directly

### CONVERSATION
"""

    for msg in st.session_state.chat_history:
        role = "User" if msg["role"] == "user" else "Assistant"
        conversation += f"{role}: {msg['content']}\n"

    # ================== GEMINI RESPONSE ==================
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                if not st.session_state.get("model"):
                    assistant_reply = "❌ No Gemini API key configured. Please enter it in the Sidebar and update to use the assistant."
                else:
                    response = st.session_state["model"].generate_content(
                        conversation,
                        generation_config={
                            "temperature": 0.3,
                            "max_output_tokens": 800
                        }
                    )
                    assistant_reply = response.text.strip()
            except Exception as e:
                assistant_reply = f"Error: {str(e)}"

        st.markdown(assistant_reply)

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_reply
    })

st.markdown("---")
