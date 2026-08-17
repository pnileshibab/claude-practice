import re
import urllib.request

URL = "https://example.com"


def main():
    with urllib.request.urlopen(URL) as response:
        status_code = response.status
        html = response.read().decode("utf-8")

    match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    title = match.group(1).strip() if match else "(no title found)"

    print(f"Status code: {status_code}")
    print(f"Page title: {title}")


if __name__ == "__main__":
    main()