import os


def create_folder_structure(base_path):
    folders = [
        "Communication & Security/Encryption",
        "Communication & Security/Password Mgmt. & 2FA",
        "Communication & Security/VPN",
        "Documents/Certificates and Cards",
        "Documents/Financial Records",
        "Documents/ID's",
        "Documents/Insurance Policies",
        "Documents/Legal Documents",
        "Documents/Medical Records",
        "Emergency/Emergency & First Aid Manuals",
        "Emergency/Emergency Plan",
        "Emergency/Emergency Resources",
        "Emergency/Offline Maps",
        "Miscellaneous",
        "Personal/Contacts",
        "Personal/Photos",
        "Personal/Videos",
        "Software & Utilities"
    ]

    readme_messages = {
        "Encryption": "Use this folder to store encrypted files and related tools.",
        "Password Mgmt. & 2FA": "Store your password management tools and two-factor authentication details here.",
        "VPN": "VPN configurations and software go here.",
        "Certificates and Cards": "Keep scanned copies of certificates and cards here.",
        "Financial Records": "Financial documents such as bank statements, receipts, and investment records.",
        "ID's": "Store scans of IDs like passports and driver’s licenses here.",
        "Insurance Policies": "Store all insurance policy documents in this folder.",
        "Legal Documents": "Legal documents including contracts, deeds, and agreements should be kept here.",
        "Medical Records": "Store all medical and health-related documents here.",
        "Emergency & First Aid Manuals": "Keep emergency procedures and first aid manuals here.",
        "Emergency Plan": "Store your emergency plans and contact information here.",
        "Emergency Resources": "Resources like emergency contact numbers, relief locations, and more.",
        "Offline Maps": "Store offline maps and navigational aids here.",
        "Miscellaneous": "For any files that do not fit the other categories.",
        "Contacts": "Keep your personal and professional contacts here.",
        "Photos": "This folder is for personal photos.",
        "Videos": "A place for personal videos.",
        "Software & Utilities": "Any useful software tools and utilities."
    }


    for folder in folders:
        # Create the full folder path
        folder_path = os.path.join(base_path, folder)
        # Create the folder if it doesn't already exist
        os.makedirs(folder_path, exist_ok=True)

        # Get the last part of the folder path for determining README content
        last_folder_name = folder.split('/')[-1]

        # Create a README file in the folder
        readme_path = os.path.join(folder_path, "README.txt")
        with open(readme_path, 'w') as file:
            # Write customized content to the README file
            folder_key = ' '.join(last_folder_name.split(' & ')).strip()  # Normalize keys to match
            message = readme_messages.get(folder_key, "This is a default README content.")
            file.write(message)
        
        print(f"Created folder and README in: {folder_path}")

       
# Use the current working directory as the base path
base_path = os.getcwd()
create_folder_structure(base_path)
