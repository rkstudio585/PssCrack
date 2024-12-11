# PssCrack

# Password Auditor Tool

The **Password Auditor Tool** is a powerful and simple command-line utility designed to test the strength of passwords by performing **dictionary attacks** and **brute force attacks**. Built for ethical purposes such as auditing password security, this tool supports popular hashing algorithms like MD5, SHA-1, SHA-256, and SHA-512.  

---

## Features

### 1. **Hash Type Support**
The tool supports the following hash types:
- **MD5**
- **SHA-1**
- **SHA-256**
- **SHA-512**

### 2. **Attack Modes**
- **Dictionary Attack:** Attempts to match the target hash with passwords from a user-specified wordlist.  
- **Brute Force Attack:** Generates all possible combinations of characters up to a specified length to match the target hash.

### 3. **Customizable Settings**
- Define the character set for brute force attacks.
- Specify the maximum password length for brute force attacks.
- Choose your own wordlist for dictionary attacks.

### 4. **Command-Line Interface (CLI)**
The tool features a clean and intuitive CLI, making it easy to specify options and perform attacks.

### 5. **Real-Time Feedback**
- Progress updates during brute force attacks.
- Immediate result display when the password is found.

---

## How It Works

The tool takes a **hashed password** as input and attempts to recover the original password using one of two modes: **dictionary attack** or **brute force attack**. Here's an overview of the workflow:

1. **Hash Detection**  
   The user specifies the hash type. If it's incorrect, the tool won't work properly.  
   
2. **Password Generation**  
   - For dictionary attacks, the tool reads passwords line-by-line from a wordlist.  
   - For brute force attacks, the tool generates password combinations based on the user-defined character set and length.

3. **Hash Comparison**  
   Each generated password is hashed using the specified algorithm and compared to the target hash.

4. **Result Display**  
   Once the password is found, it's displayed to the user.

---

## Installation

1. **Clone the Repository**
  ```bash
   git clone https://github.com/rkstudio585/PssCrack
   cd PssCrack
   ```

2. **Install Python Dependencies**
   Make sure Python 3 is installed on your system. The tool uses the `rich` library for CLI styling. Install it via pip:
   ```bash
   pip install rich
   ```

3. **Run the Tool**
   ```bash
   python main.py --help
   ```

---

## Usage

The tool supports two attack modes: dictionary and brute force. Below are examples of how to use each mode.

### 1. **Dictionary Attack**
Run the following command:
```bash
python main.py -m dictionary -t md5 -H <HASH> -w <WORDLIST_PATH>
```
- `-m dictionary`: Specifies the dictionary attack mode.
- `-t md5`: Indicates the hash type (replace with `sha1`, `sha256`, or `sha512` as needed).
- `-H <HASH>`: The target hash you want to crack.
- `-w <WORDLIST_PATH>`: Path to the wordlist file.

#### Example:
```bash
python main.py -m dictionary -t sha256 -H d2d2d0e05640c52298961b3c0a372e2c74f0ab728c7b88264e0d7eb7e2f4fbbd -w wordlist.txt
```

### 2. **Brute Force Attack**
Run the following command:
```bash
python main.py -m bruteforce -t sha256 -H <HASH> -c abc123 -l 5
```
- `-m bruteforce`: Specifies the brute force attack mode.
- `-t sha256`: Indicates the hash type (replace with `md5`, `sha1`, or `sha512` as needed).
- `-H <HASH>`: The target hash you want to crack.
- `-c abc123`: Character set to use for brute force (e.g., letters, numbers, or symbols).
- `-l 5`: Maximum password length to attempt.

#### Example:
```bash
python main.py -m bruteforce -t md5 -H 5f4dcc3b5aa765d61d8327deb882cf99 -c abcdefghijklmnopqrstuvwxyz -l 4
```

---

## Wordlist Creation

### Example Wordlist
Below is a sample `wordlist.txt` file that you can use with the tool:
```
password
123456
qwerty
letmein
welcome
monkey
password1
iloveyou
trustno1
```

### Expanding the Wordlist
You can find publicly available wordlists like the **RockYou** wordlist for larger datasets.

---

## Example Outputs

### Dictionary Attack
```bash
python main.py -m dictionary -t md5 -H 5f4dcc3b5aa765d61d8327deb882cf99 -w wordlist.txt
```
**Output:**
```
[INFO] Starting dictionary attack using wordlist.txt...
[SUCCESS] Password found: password
```

### Brute Force Attack
```bash
python main.py -m bruteforce -t sha256 -H 6dcd4ce23d88e2ee9568ba546c007c63df6a62e72b6c0b7b030b99144f6503d0 -c abc123 -l 3
```
**Output:**
```
[INFO] Starting brute force attack...
[SUCCESS] Password found: abc
```

---

## Limitations

1. **Performance:** Brute force attacks are computationally expensive and may take significant time for long passwords or large character sets.
2. **Supported Hash Types:** Only common hash types (MD5, SHA-1, SHA-256, SHA-512) are supported in this version.
3. **Wordlist Size:** The success of dictionary attacks depends heavily on the quality and size of the wordlist.

---

## Future Improvements

- **Multi-threading:** Speed up brute force attacks using concurrent processing.
- **Additional Hashes:** Add support for more complex hash types like bcrypt or Argon2.
- **GUI Interface:** Provide a graphical user interface for non-technical users.
- **Real-Time Stats:** Display attack progress and estimated time for completion.

---

## Ethical Considerations

This tool is intended for ethical use only:
- Test password strength on systems you own or have explicit permission to audit.
- Do not use this tool for illegal or unauthorized purposes.

Unauthorized use of this tool may violate privacy laws and result in severe penalties.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

## Contact

For questions, suggestions, or feedback, reach out at:
- **GitHub:** [GitHub Profile](https://github.com/rkstudio585)
- **Email:** rkriad585@yahoo.com
