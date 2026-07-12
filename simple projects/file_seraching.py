import os

def search_file(target_directory, file_name):
    print(f"Searching for '{file_name}' inside '{target_directory}'...")
    found_paths = []

    # os.walk traverses through all folders and subfolders
    for root, dirs, files in os.walk(target_directory):
        if file_name in files:
            # Smartly combine the directory path and the filename
            full_path = os.path.join(root, file_name)
            found_paths.append(full_path)
            
    return found_paths

# ----------------- Main Program Execution -----------------

# 1. Get user inputs
search_dir = input("Enter the directory path to search in (e.g., . for current folder): ")
target_file = input("Enter the full filename you are looking for (e.g., report.csv): ")

# 2. Execute the search function
results = search_file(search_dir, target_file)

# 3. Display the results
print("\n--- Search Results ---")
if results:
    print(f"Success! The file was found in the following location(s):\n")
    for path in results:
        print(f"📍 {path}")
else:
    print("❌ Sorry, no file with that name was found in this directory.")