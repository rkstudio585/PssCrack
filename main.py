import hashlib
import argparse
import itertools
from rich.console import Console
from rich.progress import Progress

console = Console()

# Supported hash types
HASH_FUNCTIONS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}

def detect_hash(hash_str):
    """Detect the type of hash based on its length."""
    hash_lengths = {
        32: "md5",
        40: "sha1",
        64: "sha256",
        128: "sha512",
    }
    return hash_lengths.get(len(hash_str), None)

def hash_password(password, hash_type):
    """Hash a password using the specified algorithm."""
    hash_func = HASH_FUNCTIONS.get(hash_type)
    if not hash_func:
        raise ValueError(f"Unsupported hash type: {hash_type}")
    return hash_func(password.encode()).hexdigest()

def dictionary_attack(hash_str, hash_type, wordlist):
    """Perform a dictionary attack using a wordlist."""
    console.print(f"[yellow]Starting dictionary attack using {wordlist}...[/yellow]")
    try:
        with open(wordlist, "r") as file:
            for line in file:
                password = line.strip()
                if hash_password(password, hash_type) == hash_str:
                    console.print(f"[green]Password found: {password}[/green]")
                    return password
    except FileNotFoundError:
        console.print("[red]Wordlist file not found![/red]")
    console.print("[red]Password not found in wordlist.[/red]")
    return None

def brute_force_attack(hash_str, hash_type, char_set, max_length):
    """Perform a brute force attack."""
    console.print("[yellow]Starting brute force attack...[/yellow]")
    with Progress() as progress:
        task = progress.add_task("[cyan]Brute forcing...", total=max_length)
        for length in range(1, max_length + 1):
            progress.update(task, completed=length)
            for attempt in itertools.product(char_set, repeat=length):
                password = "".join(attempt)
                if hash_password(password, hash_type) == hash_str:
                    console.print(f"[green]Password found: {password}[/green]")
                    return password
    console.print("[red]Password not found using brute force.[/red]")
    return None

def main():
    parser = argparse.ArgumentParser(description="Password Auditor Tool")
    parser.add_argument("-m", "--mode", choices=["dictionary", "bruteforce"], required=True, help="Attack mode to use.")
    parser.add_argument("-t", "--type", required=True, help="Hash type (e.g., md5, sha1, sha256, sha512).")
    parser.add_argument("-H", "--hash", required=True, help="The hash to crack.")
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist (for dictionary attack).")
    parser.add_argument("-c", "--charset", default="abcdefghijklmnopqrstuvwxyz", help="Character set for brute force.")
    parser.add_argument("-l", "--length", type=int, default=4, help="Maximum password length for brute force.")
    
    args = parser.parse_args()
    
    # Detect hash type if not provided
    hash_type = args.type.lower()
    if hash_type not in HASH_FUNCTIONS:
        console.print("[red]Unsupported hash type![/red]")
        return

    if args.mode == "dictionary":
        if not args.wordlist:
            console.print("[red]Wordlist is required for dictionary attack![/red]")
            return
        dictionary_attack(args.hash, hash_type, args.wordlist)
    elif args.mode == "bruteforce":
        brute_force_attack(args.hash, hash_type, args.charset, args.length)

if __name__ == "__main__":
    main()
  
