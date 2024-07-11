import instaloader
import pandas as pd
import re

def remove_emojis(text):
    # Remove emojis using regex
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642" 
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def process_username(username):
    # Initialize Instaloader
    # try:
        L = instaloader.Instaloader()

        
    # Fetch the profile of the user
        profile = instaloader.Profile.from_username(L.context, username)
    
    # Extract user data
        user_data = {
                "Username": profile.username,
                "Full Name": remove_emojis(profile.full_name) if profile.full_name else 'aa',
                "Followers": profile.followers,
                "Following": profile.followees,
                "Bio": remove_emojis(profile.biography) if profile.biography else 'aa' ,
                "Website": profile.external_url,
                "Posts Count": profile.mediacount,
        }

    # Create a DataFrame from the user_data dictionary
        print(pd.DataFrame([user_data]))
    #     print(df)

    #     df.to_csv(csv_file_path, index=False)
    #     print("Data saved successfully.")
    
    # except instaloader.exceptions.ProfileNotExistsException:
    #         print("Error: Profile not found.")
    
    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")
    
    # # Specify the CSV file path where you want to save the data
    # csv_file_path = r"C:\Users\deepa\OneDrive\Desktop\Aishu\fake_account_detector\myproject\myapp\FAKE_ACC\instagram_user_data.csv"


    # # Save the data to the CSV file
    # df.to_csv(csv_file_path, index=False)

    # df.fillna("aa", inplace=True)
    
    

if __name__ == "__main__":
    # You can also add test code here if needed
    pass
