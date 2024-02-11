def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""

def write_combined_file(file1_content, file2_content, combined_filename):
    try:
        with open(combined_filename, 'w') as combined_file:
            combined_file.write(file1_content)
            combined_file.write("\n")
            combined_file.write(file2_content)
        print(f"Combined contents written to '{combined_filename}'")
    except Exception as e:
        print(f"Error occurred while writing to '{combined_filename}': {e}")

def read_and_print_combined_file(combined_filename):
    try:
        with open(combined_filename, 'r') as combined_file:
            print("Contents of Combined File:")
            print(combined_file.read())
    except FileNotFoundError:
        print(f"Error: File '{combined_filename}' not found.")
    except Exception as e:
        print(f"Error occurred while reading '{combined_filename}': {e}")

if __name__ == "__main__":
    file1_name = input("Enter the first file name: ")
    file2_name = input("Enter the second file name: ")

    file1_content = read_file(file1_name)
    file2_content = read_file(file2_name)

    if file1_content and file2_content:
        combined_filename = "combined_files.txt"
        write_combined_file(file1_content, file2_content, combined_filename)
        read_and_print_combined_file(combined_filename)
