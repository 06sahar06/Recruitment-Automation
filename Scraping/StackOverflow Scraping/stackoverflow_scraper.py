import requests
import streamlit as st 

def search_stackoverflow_profiles(keyword, site='stackoverflow'):
    search_url="https://api.stackexchange.com/2.3/users"
    params = {
        'order': 'desc',
        'sort': 'reputation',
        'inname': keyword,
        'site': site,
        'pagesize': 50,
    }

    try:
        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            users_data = response.json()
            if users_data['items']:
                return users_data['items']
            else:
                st.write("No users found with the given keyword.")
                return []
        else:
            st.write(f"Failed to search for profiles: {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        st.write(f"Error: {e}")
        return []

def analyze_profile(profile):
    st.write(f"Username: {profile['display_name']}")
    st.write(f"Profile URL: {profile['link']}")
    st.write(f"Reputation: {profile['reputation']}")
    st.write(f"Location: {profile.get('location', 'Not provided')}")
    st.write(f"Profile Creation Date: {profile['creation_date']}")
    st.write(f"Profile Last Access Date: {profile['last_access_date']}")
    st.write(f"Number of Answers: {profile.get('answer_count', 0)}")
    st.write(f"Number of Questions: {profile.get('question_count', 0)}")
    st.write("-" * 30)

def main():
    search_url="https://api.stackexchange.com/2.3/users"
    keyword = st.text_input("Enter a keyword to search for profiles: ")
    profiles = search_stackoverflow_profiles(keyword)

    if profiles:
        st.write(f"Found {len(profiles)} profiles:")
        st.write("=" * 30)
        for profile in profiles:
            analyze_profile(profile)
    else:
        st.write("No profiles to analyze.")

if __name__ == "__main__":
    main()

