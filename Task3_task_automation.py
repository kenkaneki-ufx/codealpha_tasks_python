# Task 3: Task Automation with Python Scripts
# CodeAlpha Python Programming Internship
# Author: Aryan Pandey

import os
import shutil
import re
import requests
from pathlib import Path

def move_jpg_files():
    """
    Move all .jpg files from a folder to a new folder.
    """
    print("\n" + "=" * 60)
    print("MOVING JPG FILES")
    print("=" * 60)
    
    source_folder = input("Enter source folder path: ").strip()
    destination_folder = input("Enter destination folder path: ").strip()
    
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")
    
    # Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return
    
    # Move .jpg files
    moved_count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename}")
                moved_count += 1
            except Exception as e:
                print(f"Error moving {filename}: {e}")
    
    print(f"\nTotal files moved: {moved_count}")

def extract_emails():
    """
    Extract all email addresses from a .txt file and save them to another file.
    """
    print("\n" + "=" * 60)
    print("EXTRACTING EMAIL ADDRESSES")
    print("=" * 60)
    
    input_file = input("Enter input text file path: ").strip()
    output_file = input("Enter output file path (for emails): ").strip()
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return
    
    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Extract emails using regex
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)
    
    # Remove duplicates while preserving order
    unique_emails = list(dict.fromkeys(emails))
    
    # Save emails to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for email in unique_emails:
                f.write(email + '\n')
        print(f"Extracted {len(unique_emails)} unique email addresses")
        print(f"Saved to: {output_file}")
    except Exception as e:
        print(f"Error saving emails: {e}")

def scrape_webpage_title():
    """
    Scrape the title of a fixed webpage and save it.
    """
    print("\n" + "=" * 60)
    print("SCRAPING WEBPAGE TITLE")
    print("=" * 60)
    
    url = input("Enter webpage URL: ").strip()
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        # Send GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Extract title using regex (simple approach)
        title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE | re.DOTALL)
        
        if title_match:
            title = title_match.group(1).strip()
            print(f"Page Title: {title}")
            
            # Save title to file
            save_option = input("Do you want to save this title to a file? (y/n): ").lower().strip()
            if save_option == 'y':
                filename = input("Enter filename (without extension): ").strip()
                if not filename:
                    filename = "webpage_title"
                
                with open(f"{filename}.txt", 'w', encoding='utf-8') as f:
                    f.write(f"URL: {url}\n")
                    f.write(f"Title: {title}\n")
                
                print(f"Title saved to {filename}.txt")
        else:
            print("Could not find title tag in the webpage.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to run task automation scripts."""
    print("=" * 60)
    print("TASK AUTOMATION WITH PYTHON SCRIPTS")
    print("=" * 60)
    print("\nChoose an automation task:")
    print("1. Move .jpg files from one folder to another")
    print("2. Extract email addresses from a text file")
    print("3. Scrape webpage title")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            move_jpg_files()
        elif choice == '2':
            extract_emails()
        elif choice == '3':
            scrape_webpage_title()
        elif choice == '4':
            print("Exiting task automation.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        
        print("\n" + "-" * 60)

if __name__ == "__main__":
    main()