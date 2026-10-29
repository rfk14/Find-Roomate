import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="Roommate Matchmaker AI", page_icon="🏠", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("profiles1.csv")

profiles_df = load_data()

st.title("🏠 Roommate Matchmaker AI")
st.caption("Interactive matching engine with configurable Deal-Breakers (Hard Rules) and Soft Preference Weights.")

# --- TOP CONTROL PANEL WITH DEAL-BREAKER CHECKBOXES ---
with st.container():
    st.subheader("⚙️ Match Preferences & Decision Logic")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        shift = st.selectbox("Work Shift", ["Morning", "Night", "Evening"])
        db_shift = st.checkbox("Deal-Breaker? (Hard Rule)", value=True, key="db_shift")
        
    with col2:
        sleep = st.selectbox("Sleep Habit", ["Light Sleeper", "Heavy Sleeper"])
        db_sleep = st.checkbox("Deal-Breaker? (Hard Rule)", value=True, key="db_sleep")
        
    with col3:
        clean = st.selectbox("Cleanliness Expectation", ["Organised", "Messy", "Flexible"])
        db_clean = st.checkbox("Deal-Breaker? (Hard Rule)", value=False, key="db_clean")
        w_clean = st.slider("Cleanliness Priority Weight", 0, 5, 3)
        
    with col4:
        noise = st.selectbox("Noise Preference", ["Quiet", "Moderate", "Loud"])
        db_noise = st.checkbox("Deal-Breaker? (Hard Rule)", value=False, key="db_noise")
        w_noise = st.slider("Quietness Priority Weight", 0, 5, 3)

st.divider()

# --- FILTERING LOGIC (DYNAMIC HARD RULES) ---
filtered_candidates = profiles_df.copy()

# Dynamically apply hard filters only if "Deal-Breaker" checkbox is checked
if db_shift:
    filtered_candidates = filtered_candidates[filtered_candidates['work_shift'] == shift]
if db_sleep:
    filtered_candidates = filtered_candidates[filtered_candidates['sleep_type'] == sleep]
if db_clean:
    filtered_candidates = filtered_candidates[filtered_candidates['cleanliness'] == clean]
if db_noise:
    filtered_candidates = filtered_candidates[filtered_candidates['noise_preference'] == noise]

# Summary KPI Counters
m1, m2, m3 = st.columns(3)
m1.metric("Total Candidates in System", f"{len(profiles_df)}")
m2.metric("Filtered Candidates (Passed Hard Rules)", f"{len(filtered_candidates)}")
m3.metric("Match Rate", f"{(len(filtered_candidates)/len(profiles_df))*100:.1f}%")

st.divider()

# --- SOFT SCORING ENGINE ---
if not filtered_candidates.empty:
    weights_sum = max(w_clean + w_noise, 1)
    
    def calculate_score(row):
        sim_clean = 1.0 if row['cleanliness'] == clean else 0.5
        sim_noise = 1.0 if row['noise_preference'] == noise else 0.5
        return ((w_clean * sim_clean + w_noise * sim_noise) / weights_sum) * 100

    filtered_candidates['Match_Score'] = filtered_candidates.apply(calculate_score, axis=1)
    top_candidates = filtered_candidates.sort_values(by='Match_Score', ascending=False)

    # --- APP NAVIGATION TABS ---
    tab1, tab2, tab3 = st.tabs(["🏆 Top Match Cards", "⚖️ Side-by-Side Compare", "📊 Full Candidate Table"])

    # TAB 1: Match Cards
    with tab1:
        st.subheader("Top Recommended Profiles")
        for idx, (_, row) in enumerate(top_candidates.head(5).iterrows(), start=1):
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
            "Select candidates to compare:", 
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
    st.error("No candidates matched your active deal-breakers! Try unchecking one of the 'Deal-Breaker?' checkboxes above.")