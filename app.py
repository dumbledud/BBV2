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
menu = st.sidebar.radio("Navigate", ["Home", "History & Insights", "Wife Profiles"] )

# Data definitions
husband_profiles = [
    {"name":"Angry & Spiky", "video_url":"https://youtu.be/angry_spiky_demo", "desc":"Spiky hair, intense gaze...","traits":{"Mood":"Irritable","Presence":"Critical","Loving":"Sparingly"}},
    {"name":"Poofy & Reserved", "video_url":"https://youtu.be/poofy_reserved_demo", "desc":"Soft poofy hair...","traits":{"Mood":"Calm","Presence":"Observant","Loving":"Steady"}},
    {"name":"Too Cool & Busy", "video_url":"https://youtu.be/too_cool_busy_demo", "desc":"Slick style...","traits":{"Mood":"Distracted","Presence":"Distant","Loving":"Surface-level"}},
    {"name":"Busybody & Chaotic", "video_url":"https://youtu.be/busybody_chaotic_demo", "desc":"Organizing others...","traits":{"Mood":"Jittery","Presence":"Overbearing","Loving":"Well-meaning"}},
    {"name":"Chill & Present", "video_url":"https://youtu.be/chill_present_demo", "desc":"Warm smile...","traits":{"Mood":"Relaxed","Presence":"Fully here","Loving":"Overflowing"}}
]

wife_profiles = [
    {"name":"A Wife Preset","video_url":"","desc":"Brilliant, flexible, kind...","traits":{"Essence":"Brilliant & loving","Role":"Herald of God's Word"}},
    {"name":"Supportive & Cheerful","video_url":"","desc":"Bright eyes, open heart...","traits":{"Mood":"Cheerful","Support":"High"}},
    {"name":"Reflective & Calm","video_url":"","desc":"Soft tone, thoughtful...","traits":{"Mood":"Calm","Wisdom":"Deep"}}
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
    # Select profiles
    husb = st.selectbox("Select today's husband personality:", [p['name'] for p in husband_profiles])
    wife = st.selectbox("Select today's wife personality:", [w['name'] for w in wife_profiles])
    st.markdown("---")
    # Prayer tracker
    st.subheader("🙏 Prayer Tracker 🙏")
    times = ["6:30 AM","9:00 AM","12:00 PM","3:00 PM","8:00 PM"]
    done = [st.checkbox(f"Prayed at {t}") for t in times]
    prayers_done = sum(done)
    # Parking lot
    st.markdown("---")
    st.subheader("📝 Parking Lot Topics 📝")
    new_topic = st.text_input("Add topic:")
    if st.button("Park") and new_topic:
        st.session_state['topics'].append(new_topic)
    for i, top in enumerate(st.session_state['topics'],1): st.write(f"{i}. {top}")
    # Submit
    if st.button("Submit Today's Record"):
        record_entry(husb, wife, prayers_done)
        st.success("Today's entry recorded!")
        # Suggestion
        avg = (sum([e['prayers_done'] for e in st.session_state['history']]) / len(st.session_state['history']))
        st.info(f"You've averaged {avg:.1f}/5 prayers. Aim for 5 daily for spiritual growth.")

# History & Insights view
def show_history():
    st.title("📊 History & Insights 📊")
    if not st.session_state['history']:
        st.write("No history yet.")
        return
    df = pd.DataFrame(st.session_state['history'])
    st.dataframe(df)
    # Combination counts
    combo = df.groupby(['husband','wife']).size().reset_index(name='count')
    st.subheader("Profile Combinations Frequency")
    st.table(combo)
    # Suggest least used combo
    least = combo.sort_values('count').iloc[0]
    st.info(f"Try the combo '{least.husband}' & '{least.wife}' for a fresh dynamic!")

# Wife Profiles view
def show_wife_profiles():
    st.title("👩‍❤‍💋‍👩 Wife Personality Profiles 👩‍❤‍💋‍👩")
    choice = st.selectbox("Pick a wife profile:", [w['name'] for w in wife_profiles])
    prof = next(w for w in wife_profiles if w['name']==choice)
    st.write(prof['desc'])
    st.markdown("**Traits**")
    st.table(prof['traits'])

# Main app
if menu == "Home":
    show_home()
elif menu == "History & Insights":
    show_history()
else:
    show_wife_profiles()
