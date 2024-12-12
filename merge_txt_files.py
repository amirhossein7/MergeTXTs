import os

def merge_txt_files(folder_path, output_file="merged.txt"):
    try:
        # Get a list of all txt files in the folder
        txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

        # Sort files numerically based on their numeric prefixes
        txt_files.sort(key=lambda x: int(x.split(".")[0]))

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for txt_file in txt_files:
                file_path = os.path.join(folder_path, txt_file)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content + '\n')  # Add a newline between files
        print(f"All text files have been merged into {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing txt files: ").strip()
    output_file = input("Enter the output file name (default: merged.txt): ").strip() or "merged.txt"
    merge_txt_files(folder_path, output_file)
