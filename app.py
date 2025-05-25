import streamlit as st

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
    .reportview-container {
        background-color: #f2f2f2;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    h1, h2, h3 {
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .profile-card {
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        background-color: white;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("❤️ Personality AI Daily Spouse Selector ❤️")
st.markdown("""
Welcome to your personalized daily selector! 🥰
Choose which version of the man you love most today.
Let accountability, grace, and love guide your day — and don't forget to pray together! 🙏
""")

# === Sidebar: Wife's Default Preferences ===
st.sidebar.header("A Wife's Default Presets")
wife_prefs = {
    "Essence": "Brilliant, flexible (mind & body), kind & loving, quick to listen, trusting & patient, communicative",
    "Look": "Dreamboat Michael Phelps x John Krasinski; salt & pepper hair, distinguished hairline",
    "Role": "Herald of God's Word; calm, silly, trusted forever; cocoon style"
}
for k, v in wife_prefs.items():
    st.sidebar.subheader(k)
    st.sidebar.write(v)

# === Husband Profiles ===
profiles = [
    {
        "name": "Angry & Spiky",
        "video_url": "https://youtu.be/angry_spiky_demo",
        "video_desc": "A man with spiky hair, intense gaze, wearing black leather, speaks blunt truths with fiery passion.",
        "traits": {
            "Hair": "Spiky & chaotic",
            "Clothing": "Leather jacket",
            "Hygiene": "Rugged (needs shampoo)",
            "Mood": "Irritable",
            "Interests": "Debate & spikes",
            "Flexibility": "Low",
            "Presence": "Critical",
            "Loving": "Sparingly"
        }
    },
    {
        "name": "Poofy & Reserved",
        "video_url": "https://youtu.be/poofy_reserved_demo",
        "video_desc": "Soft poofy hair, gentle eyes, pastel sweater; speaks in soft tones, thoughtful and introspective.",
        "traits": {
            "Hair": "Poofy & neat",
            "Clothing": "Pastel sweater",
            "Hygiene": "Pristine",
            "Mood": "Calm",
            "Interests": "Journaling & tea",
            "Flexibility": "Moderate",
            "Presence": "Observant",
            "Loving": "Steady"
        }
    },
    {
        "name": "Too Cool & Busy",
        "video_url": "https://youtu.be/too_cool_busy_demo",
        "video_desc": "Sunglasses, slicked-back hair, designer suit; talks about his accomplishments, checks phone constantly.",
        "traits": {
            "Hair": "Sleek & styled",
            "Clothing": "Designer suit",
            "Hygiene": "Top tier",
            "Mood": "Distracted",
            "Interests": "Networking & events",
            "Flexibility": "Low",
            "Presence": "Distant",
            "Loving": "Surface-level"
        }
    },
    {
        "name": "Busybody & Chaotic",
        "video_url": "https://youtu.be/busybody_chaotic_demo",
        "video_desc": "Runs around in plaid shirt, clipboards in hand; always organizing others but missing his own keys.",
        "traits": {
            "Hair": "Tousled",
            "Clothing": "Plaid & cargo pants",
            "Hygiene": "Casual",
            "Mood": "Jittery",
            "Interests": "Checklists & gossip",
            "Flexibility": "Variable",
            "Presence": "Overbearing",
            "Loving": "Well-meaning"
        }
    },
    {
        "name": "Chill & Present",
        "video_url": "https://youtu.be/chill_present_demo",
        "video_desc": "Soft denim shirt, warm smile, salt & pepper beard; listens intently, jokes gently, supports every step.",
        "traits": {
            "Hair": "Salt & pepper, neatly trimmed",
            "Clothing": "Denim & comfort",
            "Hygiene": "Fresh & clean",
            "Mood": "Relaxed",
            "Interests": "Family & faith",
            "Flexibility": "High",
            "Presence": "Fully here",
            "Loving": "Overflowing"
        }
    }
]

# Select today's profile
selection = st.selectbox("Choose today's husband personality:", [p["name"] for p in profiles])
profile = next(p for p in profiles if p["name"] == selection)

# Display selected profile
st.markdown("---")
col1, col2 = st.columns([1, 2])
with col1:
    st.video(profile["video_url"])
with col2:
    st.subheader(f"{profile['name']} Bio")
    st.write(profile["video_desc"])
    st.markdown("**Traits**")
    st.table(profile["traits"])

# === Prayer Reminders ===
st.markdown("---")
st.header("🙏 Today's Prayer Times 🙏")
prayer_times = ["6:30 AM", "9:00 AM", "12:00 PM", "3:00 PM", "8:00 PM"]
for t in prayer_times:
    st.write(f"• Pray together at {t}")

# === Parking Lot: Discussion Topics ===
st.markdown("---")
st.header("📝 Parking Lot: Discussion Topics")
if "topics" not in st.session_state:
    st.session_state["topics"] = []
new_topic = st.text_input("Add a topic to the parking lot:")
if st.button("Park Topic") and new_topic:
    st.session_state.topics.append(new_topic)
if st.session_state.topics:
    for idx, topic in enumerate(st.session_state.topics, 1):
        st.write(f"{idx}. {topic}")
