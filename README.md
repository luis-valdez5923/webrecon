Of course! Here's the template for your README file that you can copy and use directly. Just replace the placeholders with your actual project information:

```markdown
# Web Recon Tool

This is a command-line web reconnaissance tool that supports various fuzzing modes to discover information about a target website.

## Features

- Subdomains fuzzing
- Directory fuzzing
- Virtual host (vhost) fuzzing
- Extension fuzzing
- Page fuzzing

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/web-recon-tool.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd web-recon-tool
   ```

3. Install any dependencies (if required).

4. Run the script:
   ```bash
   python script.py -m <mode> -u <url> -w <wordlist> -o <output> -fs <filter>
   ```

## Usage

Replace the placeholders with actual values:
- `<mode>`: subdomains, dir, vhost, ext, page
- `<url>`: Target URL
- `<wordlist>`: Path to the wordlist file
- `<output>`: Path to the output file (optional)
- `<filter>`: Filter size (optional)

## Examples

Fuzz subdomains:
```bash
python script.py -m subdomains -u example.com -w subdomains.txt -o output.txt -fs 200
```

Fuzz directories:
```bash
python script.py -m dir -u example.com -w directories.txt -o output.txt -fs 404
```

... (add more examples for other modes)

## Contributions

Contributions and feedback are welcome! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to copy the above template and replace the placeholders with your actual information. Make sure to save the file with the name `README.md` in the root directory of your GitHub repository. After making the changes, commit and push the README file along with the rest of your project to GitHub.
