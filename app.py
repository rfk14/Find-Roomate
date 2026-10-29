import streamlit as st
import pandas as pd

st.set_page_config(page_title="Roommate Finder AI", layout="wide")
st.title("🏠 Find Roommate — AI Matching Engine")

@st.cache_data
def load_data():
    return pd.read_csv("profiles1.csv")

profiles_df = load_data()

# Sidebar controls
st.sidebar.header("1. Hard-Rule Filters")
shift = st.sidebar.selectbox("Work Shift", ["Morning", "Night", "Evening"])
sleep = st.sidebar.selectbox("Sleep Type", ["Light Sleeper", "Heavy Sleeper"])

st.sidebar.header("2. Soft Scoring Weights")
w_clean = st.sidebar.slider("Cleanliness Weight", 0, 3, 1)
w_noise = st.sidebar.slider("Noise Weight", 0, 3, 1)
w_pets  = st.sidebar.slider("Pets Weight", 0, 3, 1)

# Tier 1: Hard Rules
candidates = profiles_df[
    (profiles_df['work_shift'] == shift) & 
    (profiles_df['sleep_type'] == sleep)
].copy()

st.info(f"🔍 **Hard-Rule Filter:** {len(candidates)} candidates retained out of {len(profiles_df)}")

if not candidates.empty:
    # Tier 2: Soft Scoring
    weights_sum = max(w_clean + w_noise + w_pets, 1)

    def score_row(r):
        sim_clean = 1.0 if r['cleanliness'] == 'Organised' else 0.5
        sim_noise = 1.0 if r['noise_preference'] == 'Quiet' else 0.5
        sim_pets  = 1.0 if "Pets" in str(r['pets']) else 0.5
        return ((w_clean * sim_clean + w_noise * sim_noise + w_pets * sim_pets) / weights_sum) * 100

    candidates['live_score'] = candidates.apply(score_row, axis=1)
    top_5 = candidates.sort_values(by='live_score', ascending=False).head(5)

    st.subheader("🏆 Top 5 Recommended Matches")
    for rank, (_, row) in enumerate(top_5.iterrows(), start=1):
        with st.expander(f"#{rank} {row['user_name']} — {row['live_score']:.1f}% Match", expanded=True):
            st.write(f"• **Shift:** {row['work_shift']} | **Sleep:** {row['sleep_type']}")
            st.write(f"• **Cleanliness:** {row['cleanliness']} | **Noise:** {row['noise_preference']}")
            st.write(f"• **Pets:** {row['pets']}")