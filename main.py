from urllib.parse import urlparse

def show_banner():
    print("""\033[94m
    **************************************
    *                                    *
    *      SARATH's URL MASKING TOOL     *
    *                                    *
    **************************************
    \033[0m""")

def validate_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ('http', 'https') and parsed.netloc

def main():
    show_banner()
    
    # Get original URL
    original_url = input("\n\033[93m[+] Paste the URL to mask: \033[0m").strip()
    if not validate_url(original_url):
        print("\033[91m[!] Invalid URL. Please include http:// or https:// and a valid domain.\033[0m")
        return

    # Subdomain configuration
    use_sub = input("\n\033[93m[+] Use a subdomain? (y/n): \033[0m").lower()
    subdomain = ''
    if use_sub == 'y':
        subdomain = input("\033[93m[+] Enter subdomain name (without parent domain): \033[0m").strip()

    # Domain configuration
    domain = input("\n\033[93m[+] Enter main domain name (e.g., example.com): \033[0m").strip()

    # Path configuration
    path = input("\n\033[93m[+] Enter optional URL path (e.g., 'redirect' or leave empty): \033[0m").strip()
    if path:
        path = '/' + path.lstrip('/')

    # Protocol selection
    protocol = 'https' if input("\n\033[93m[+] Use HTTPS for masked URL? (y/n): \033[0m").lower() == 'y' else 'http'

    # Build masked URL
    masked_domain = f"{subdomain}.{domain}" if subdomain else domain
    masked_url = f"{protocol}://{masked_domain}{path}"

    # Generate HTML redirect content
    html_content = f"""<html>
<head>
    <meta http-equiv="refresh" content="0; url='{original_url}'" />
    <title>Redirecting...</title>
</head>
<body>
    <p>Redirecting to <a href="{original_url}">original content</a>...</p>
</body>
</html>"""

    # Save HTML file
    filename = "masked_redirect.html"
    with open(filename, 'w') as f:
        f.write(html_content)

    # Output instructions
    print("\n\033[92m" + "="*50)
    print(f"   Masked URL successfully created: {masked_url}")
    print("="*50 + "\033[0m")
    print(f"\n\033[95mGenerated HTML file:\033[0m \033[93m{filename}\033[0m")
    print("\n\033[95mDeployment Instructions:\033[0m")
    print(f"\033[96m1. Host {filename} on your web server at: {path or '/'}")
    print(f"2. Configure DNS for {masked_domain} to point to your server")
    print(f"3. Test by visiting: {masked_url}\033[0m")
    print("\n\033[91mNote: Actual redirection requires proper web server configuration!\033[0m")

    print("\n\033[95m" + "¯" * 50)
    print(" Thank you for using Sarath's URL Masking Tool! ")
    print("¯" * 50 + "\033[0m")

if __name__ == "__main__":
    main()
