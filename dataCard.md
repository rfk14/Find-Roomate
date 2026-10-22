## 1. Dataset Overview
- **Filename:** `profiles1.csv`
- **Total Records:** 750 candidate profiles
- **Total Attributes:** 15 columns
- **Purpose:** Primary candidate database used by the Roommate Finder agent for similarity matching and hard-rule filtering[cite: 3, 4].

## 2. Feature Schema & Descriptions
- `user_name`: Candidate name.
- `work_shift`: Work pattern (`Morning`, `Evening`, `Night`).
- `profession`: Occupation type (`Engineer`, `Developer`, `Nurse`, `Supporting Staff`).
- `personality`: `Introvert` vs `Extrovert`.
- `cleanliness`: `Organised`, `Messy`, or `Both`.
- `bedtime` & `wake_time`: Sleeping schedule preferences.
- `sleep_type`: `Light Sleeper` vs `Heavy Sleeper`.
- `noise_preference`: `Quiet` vs `Noisy`.
- `social_energy_rating`: Rating from 1 to 10.
- `room_type_preference`: `Private Room` vs `Shared Room`.
- `privacy_importance`: `High`, `Medium`, or `Low`.
- `pets`: Pet ownership/tolerance.
- `smoking_drinking`: Habits and tolerance.
- `dietary_restrictions`: Dietary preferences (`Vegetarian`, `Non-Vegetarian`, `Jain`, `No Restrictions`).

## 3. Data Quality & Limitations
- **Self-Reported Data:** Attributes rely on self-reported survey input[cite: 3].
- **Scope Limit:** Dataset serves as an offline evaluation pool for prototyping[cite: 3, 4].