def handle_file_error():
    filename = input("Please enter the filename: ")

    try:
        # Try to open the file and read its contents
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: There was an issue reading the file '{filename}'.")

# Example usage:
handle_file_error()
