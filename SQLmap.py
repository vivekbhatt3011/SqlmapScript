import subprocess  # Import subprocess to run SQLMap commands

def print_available_options():
    """
    Displays commonly used SQLMap options to guide the user.
    """
    options = [
        ("-u", "Target URL (e.g., http://example.com/vulnerable_page.php?id=1)"),
        ("--data", "Data to send in a POST request (e.g., 'id=1&submit=Submit')"),
        ("--cookie", "Send a custom cookie (e.g., 'PHPSESSID=abcdef123')"),
        ("--user-agent", "Set a custom user-agent string"),
        ("--proxy", "Route traffic through a proxy (e.g., 'http://127.0.0.1:8080')"),
        ("--batch", "Non-interactive mode (auto answers with default choices)"),
        ("--threads", "Number of concurrent threads (e.g., --threads=10)"),
        ("--level", "Level of tests to perform (1-5). Higher levels perform more tests."),
        ("--risk", "Risk level for tests (1-3). Higher risk means more aggressive tests."),
        ("--dbs", "Enumerate databases"),
        ("--tables", "Enumerate tables (use with --dbs to specify a database)"),
        ("--columns", "Enumerate columns (use with --tables to specify a table)"),
        ("--dump", "Dump the contents of a table (use with --columns to specify columns)"),
        ("--tor", "Route traffic through the Tor network for anonymity"),
        ("--output-dir", "Directory to store SQLMap output files (e.g., './sqlmap_output')")
    ]
    
    print("\nAvailable SQLMap options:")
    for option, description in options:
        print(f"{option}: {description}")
    print("\nNote: Use only options you understand and have permission to test.")

def run_sqlmap(target_url, options=""):
    """
    Runs SQLMap against a single target URL with user-provided options.
    :param target_url: The target URL to test.
    :param options: Additional SQLMap options as a string.
    """
    if not target_url.startswith("http"):
        print("[!] Invalid URL. Please provide a valid target.")
        return
    
    print(f"\n[+] Running SQLMap on {target_url} with options: {options}")
    
    # Securely construct command as a list (avoids shell injection)
    command = ["sqlmap", "-u", target_url] + options.split()
    
    try:
        subprocess.run(command, check=True)  # Execute SQLMap
    except subprocess.CalledProcessError as e:
        print(f"[!] Error occurred: {e}")

def run_sqlmap_file(target_file, options=""):
    """
    Runs SQLMap against multiple targets listed in a text file.
    :param target_file: Path to the file containing target URLs.
    :param options: Additional SQLMap options as a string.
    """
    print(f"\n[+] Running SQLMap with target file: {target_file} and options: {options}")
    
    # Use --file to scan multiple targets from a file
    command = ["sqlmap", "--batch", "--file", target_file] + options.split()
    
    try:
        subprocess.run(command, check=True)  # Execute SQLMap
    except subprocess.CalledProcessError as e:
        print(f"[!] Error occurred: {e}")

if __name__ == "__main__":
    """
    Main execution flow:
    - Prints available SQLMap options.
    - Asks the user for input: either a single URL or a file with multiple targets.
    - Runs SQLMap based on user input.
    """
    print_available_options()  # Display available options
    
    target = input("\nEnter the target URL (or path to file with --file option): ").strip()
    extra_options = input("Enter additional SQLMap options (or leave blank): ").strip()
    
    # Determine whether to scan a single URL or multiple from a file
    if target.endswith(".txt"):
        run_sqlmap_file(target, extra_options)
    elif target:
        run_sqlmap(target, extra_options)
    else:
        print("[!] Please provide a valid target.")
