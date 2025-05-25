import streamlit as st
from datetime import datetime
import pandas as pd

# Page config
st.set_page_config(
    page_title="Personality AI Daily Spouse Selector",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for aesthetics
st.markdown(
    """
    <style>
    .reportview-container { background-color: #f2f2f2; }
    .sidebar .sidebar-content { background-color: #ffffff; }
    h1, h2, h3 { text-align: center; font-family: 'Arial', sans-serif; }
    .profile-card { padding: 1rem; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); background-color: white; margin-bottom: 1rem; }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'topics' not in st.session_state:
    st.session_state['topics'] = []

# Sidebar menu
menu = st.sidebar.radio("Navigate", ["Home", "History & Insights", "Husband Profiles", "Wife Profiles"] )

# Data definitions
husband_profiles = [
    {"name": "Angry & Spiky", "video_url": "https://youtu.be/angry_spiky_demo", "desc": "Spiky hair, intense gaze, wearing leather; speaks blunt truths with fiery passion.", "traits": {"Hair": "Spiky & chaotic", "Clothing": "Leather jacket", "Hygiene": "Rugged", "Mood": "Irritable", "Interests": "Debate & spikes", "Flexibility": "Low", "Presence": "Critical", "Loving": "Sparingly"}},
    {"name": "Poofy & Reserved", "video_url": "https://youtu.be/poofy_reserved_demo", "desc": "Soft poofy hair, gentle eyes, pastel sweater; speaks in soft tones, thoughtful and introspective.", "traits": {"Hair": "Poofy & neat", "Clothing": "Pastel sweater", "Hygiene": "Pristine", "Mood": "Calm", "Interests": "Journaling & tea", "Flexibility": "Moderate", "Presence": "Observant", "Loving": "Steady"}},
    {"name": "Too Cool & Busy", "video_url": "https://youtu.be/too_cool_busy_demo", "desc": "Sunglasses, slicked-back hair, designer suit; talks about accomplishments, checks phone constantly.", "traits": {"Hair": "Sleek & styled", "Clothing": "Designer suit", "Hygiene": "Top tier", "Mood": "Distracted", "Interests": "Networking & events", "Flexibility": "Low", "Presence": "Distant", "Loving": "Surface-level"}},
    {"name": "Busybody & Chaotic", "video_url": "https://youtu.be/busybody_chaotic_demo", "desc": "Runs around in plaid shirt, clipboards in hand; always organizing others but missing his own keys.", "traits": {"Hair": "Tousled", "Clothing": "Plaid & cargo pants", "Hygiene": "Casual", "Mood": "Jittery", "Interests": "Checklists & gossip", "Flexibility": "Variable", "Presence": "Overbearing", "Loving": "Well-meaning"}},
    {"name": "Chill & Present", "video_url": "https://youtu.be/chill_present_demo", "desc": "Soft denim shirt, warm smile, salt & pepper beard; listens intently, jokes gently, supports every step.", "traits": {"Hair": "Salt & pepper, neatly trimmed", "Clothing": "Denim & comfort", "Hygiene": "Fresh & clean", "Mood": "Relaxed", "Interests": "Family & faith", "Flexibility": "High", "Presence": "Fully here", "Loving": "Overflowing"}}
]

wife_profiles = [
    {"name": "A Wife Preset", "desc": "Brilliant, flexible, kind & loving, quick to listen, trusting & patient, communicative.", "traits": {"Essence": "Brilliant & loving", "Role": "Herald of God's Word"}},
    {"name": "Supportive & Cheerful", "desc": "Bright eyes, open heart, always ready to encourage.", "traits": {"Mood": "Cheerful", "Support": "High"}},
    {"name": "Reflective & Calm", "desc": "Soft tone, thoughtful presence, brings peace.", "traits": {"Mood": "Calm", "Wisdom": "Deep"}}
]

# Helper: record today's entry
def record_entry(husb, wife, prayers_done):
    st.session_state['history'].append({
        'date': datetime.now().strftime('%Y-%m-%d'),
        'husband': husb,
        'wife': wife,
        'prayers_done': prayers_done
    })

# Home view
def show_home():
    st.title("❤️ Daily Spouse Selector & Accountability ❤️")
    husb = st.selectbox("Select today's husband personality:", [p['name'] for p in husband_profiles])
    wife = st.selectbox("Select today's wife personality:", [w['name'] for w in wife_profiles])
    st.markdown("---")
    st.subheader("🙏 Prayer Tracker 🙏")
    times = ["6:30 AM", "9:00 AM", "12:00 PM", "3:00 PM", "8:00 PM"]
    done = [st.checkbox(f"Prayed at {t}") for t in times]
    prayers_done = sum(done)
    st.markdown("---")
    st.subheader("📝 Parking Lot Topics 📝")
    new_topic = st.text_input("Add topic:")
    if st.button("Park") and new_topic:
        st.session_state['topics'].append(new_topic)
    for i, top in enumerate(st.session_state['topics'], 1):
        st.write(f"{i}. {top}")
    if st.button("Submit Today's Record"):
        record_entry(husb, wife, prayers_done)
        st.success("Today's entry recorded!")
        avg = sum(e['prayers_done'] for e in st.session_state['history']) / len(st.session_state['history'])
        st.info(f"You've averaged {avg:.1f}/5 prayers. Aim for 5 daily for spiritual growth.")

# History & Insights view
def show_history():
    st.title("📊 History & Insights 📊")
    if not st.session_state['history']:
        st.write("No history yet.")
        return
    df = pd.DataFrame(st.session_state['history'])
    st.dataframe(df)
    combo = df.groupby(['husband', 'wife']).size().reset_index(name='count')
    st.subheader("Profile Combinations Frequency")
    st.table(combo)
    least = combo.sort_values('count').iloc[0]
    st.info(f"Try the combo '{least.husband}' & '{least.wife}' for a fresh dynamic!")

# Husband Profiles view
def show_husband_profiles():
    st.title("👨‍💼 Husband Personality Profiles 👨‍💼")
    choice = st.selectbox("Pick a husband profile:", [p['name'] for p in husband_profiles])
    prof = next(p for p in husband_profiles if p['name'] == choice)
    st.video(prof['video_url'])
    st.write(prof['desc'])
    st.markdown("**Traits**")
    st.table(prof['traits'])

# Wife Profiles view
def show_wife_profiles():
    st.title("👩‍❤‍💋‍👩 Wife Personality Profiles 👩‍❤‍💋‍👩")
    choice = st.selectbox("Pick a wife profile:", [w['name'] for w in wife_profiles])
    prof = next(w for w in wife_profiles if w['name'] == choice)
    st.write(prof['desc'])
    st.markdown("**Traits**")
    st.table(prof['traits'])

# Main app
if menu == "Home":
    show_home()
elif menu == "History & Insights":
    show_history()
elif menu == "Husband Profiles":
    show_husband_profiles()
else:
    show_wife_profiles()
