def main():
    try:
        # Task 1: File Creation and Writing
        # Create and open a new file "my_file.txt" in write mode ('w')
        with open("my_file.txt", 'w') as file:
            # Write three lines of text to the file
            file.write("Hello, this is the first line.\n")
            file.write("Here is the second line with a number: 42\n")
            file.write("And this is the third line.\n")
        print("File 'my_file.txt' created and written successfully.")

        # Task 2: File Reading and Display
        # Open the file in read mode ('r') and read its contents
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nContents of 'my_file.txt' after writing:")
            print(content)

        # Task 3: File Appending
        # Open the file in append mode ('a') to add more content
        with open("my_file.txt", 'a') as file:
            file.write("Now appending this fourth line.\n")
            file.write("Here's another line with a number: 99.\n")
            file.write("Finally, the sixth line is here.\n")
        print("\nFile 'my_file.txt' updated with appended content.")

        # Reading the file again to show the updated content
        with open("my_file.txt", 'r') as file:
            updated_content = file.read()
            print("\nContents of 'my_file.txt' after appending:")
            print(updated_content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile handling operation complete.")

# Run the main function
if __name__ == "__main__":
    main()
