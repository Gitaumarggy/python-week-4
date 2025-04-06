def read_and_write_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Modify the content (this is just an example, you can modify as you want)
        modified_content = content.upper()  # Converts all text to uppercase

        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing to the files.")

# Example usage:
input_file = "marggy.txt"  # Replace with your input file
output_file = "modified-marggy.txt"  # Replace with your output file
read_and_write_file(input_file, output_file)
