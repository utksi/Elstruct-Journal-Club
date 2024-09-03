import os
from datetime import datetime

def get_latest_meeting_folder(root_dir):
    meeting_folders = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f))]
    date_folders = []
    for folder in meeting_folders:
        try:
            date = datetime.strptime(folder, "%Y-%m-%d")
            date_folders.append((date, folder))
        except ValueError:
            continue
    if not date_folders:
        return None
    return max(date_folders)[1]

def update_readme(root_dir):
    latest_folder = get_latest_meeting_folder(root_dir)
    if not latest_folder:
        print("No meeting folders found.")
        return

    readme_content = f"""# Elstruct Journal Club
Minutes from Journal club meetings for elstruct@LiU

The last meeting was on {latest_folder}.

"""

    minutes_path = os.path.join(root_dir, latest_folder, "README.md")
    if os.path.exists(minutes_path):
        with open(minutes_path, 'r') as minutes_file:
            readme_content += minutes_file.read()
    else:
        readme_content += f"No minutes found for the meeting on {latest_folder}."

    with open(os.path.join(root_dir, "README.md"), 'w') as readme_file:
        readme_file.write(readme_content)

    print(f"README.md updated with minutes from {latest_folder}")

if __name__ == "__main__":
    root_directory = "."  # You can change this to the specific path of your repository
    update_readme(root_directory)
