import streamlit as st
import pandas as pd

# Page setup - Centered full-app layout
st.set_page_config(page_title="Find Roommate AI", page_icon="🏠", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("profiles1.csv")

profiles_df = load_data()

# Header Toolbar
st.title("🏠 Roommate Matchmaker AI")
st.caption("Interactive matching engine and profile comparison tool")

# --- TOP INTERACTIVE CONTROL PANEL ---
with st.container():
    st.subheader("⚙️ Match Preferences & Filters")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        shift = st.selectbox("Work Shift", ["Morning", "Night", "Evening"])
    with col2:
        sleep = st.selectbox("Sleep Habit", ["Light Sleeper", "Heavy Sleeper"])
    with col3:
        w_clean = st.slider("Cleanliness Priority", 0, 5, 3)
    with col4:
        w_noise = st.slider("Quietness Priority", 0, 5, 3)

st.divider()

# --- HARD RULE FILTERING ---
candidates = profiles_df[
    (profiles_df['work_shift'] == shift) & 
    (profiles_df['sleep_type'] == sleep)
].copy()

# Metric Bar
m1, m2, m3 = st.columns(3)
m1.metric("Total Candidates in System", f"{len(profiles_df)}")
m2.metric("Filtered Candidates", f"{len(candidates)}")
m3.metric("Match Rate", f"{(len(candidates)/len(profiles_df))*100:.1f}%")

st.divider()

if not candidates.empty:
    # Soft Scoring Calculation
    weights_sum = max(w_clean + w_noise, 1)
    
    def calculate_score(row):
        sim_clean = 1.0 if row['cleanliness'] == 'Organised' else 0.5
        sim_noise = 1.0 if row['noise_preference'] == 'Quiet' else 0.5
        return ((w_clean * sim_clean + w_noise * sim_noise) / weights_sum) * 100

    candidates['Match_Score'] = candidates.apply(calculate_score, axis=1)
    top_candidates = candidates.sort_values(by='Match_Score', ascending=False)

    # --- APP NAVIGATION TABS ---
    tab1, tab2, tab3 = st.tabs(["🏆 Top Match Cards", "⚖️ Side-by-Side Compare", "📊 Full Candidate Table"])

    # TAB 1: Match Cards
    with tab1:
        st.subheader("Top Recommended Profiles")
        for idx, (_, row) in enumerate(top_candidates.head(4).iterrows(), start=1):
            with st.expander(f"👤 #{idx} {row['user_name']} — {row['Match_Score']:.1f}% Match Score", expanded=True):
                c1, c2, c3 = st.columns([1, 2, 2])
                with c1:
                    st.metric("Compatibility", f"{row['Match_Score']:.0f}%")
                    st.progress(int(row['Match_Score']))
                with c2:
                    st.markdown(f"**Work Shift:** `{row['work_shift']}`")
                    st.markdown(f"**Sleep Type:** `{row['sleep_type']}`")
                with c3:
                    st.markdown(f"**Cleanliness:** `{row['cleanliness']}`")
                    st.markdown(f"**Noise Level:** `{row['noise_preference']}`")
                st.button(f"Connect with {row['user_name']}", key=f"btn_{idx}")

    # TAB 2: Side-by-Side Comparison
    with tab2:
        st.subheader("Compare Candidates Head-to-Head")
        selected_names = st.multiselect(
            "Select 2 or 3 candidates to compare:", 
            options=top_candidates['user_name'].tolist(),
            default=top_candidates['user_name'].head(2).tolist()
        )
        if selected_names:
            compare_df = top_candidates[top_candidates['user_name'].isin(selected_names)]
            st.dataframe(compare_df[['user_name', 'Match_Score', 'work_shift', 'sleep_type', 'cleanliness', 'noise_preference']], use_container_width=True)

    # TAB 3: Full Data Table
    with tab3:
        st.subheader("Filterable Candidate Database")
        st.dataframe(top_candidates, use_container_width=True)

else:
    st.error("No candidates matched those criteria. Try adjusting the dropdowns above!")