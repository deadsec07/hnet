Web Tools

sql_injector.py
- Usage: `python tools/web/sql_injector.py`
- Example prompts:
  - Target URL (with parameter): http://example.com/page?id=1
  - Parameter name: id

xss_tester.py
- Usage: `python tools/web/xss_tester.py`
- Example prompts:
  - Target URL (with parameter): http://example.com/search?q=1
  - Parameter name: q

web_recon.py
- Prerequisites provided by `requirements.txt` (requests, dnspython, python-whois)
- Usage: `python tools/web/web_recon.py`
- Example prompt:
  - Enter the target URL (with protocol, e.g., https://example.com): https://example.com

