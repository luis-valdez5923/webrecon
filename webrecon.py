import argparse
import subprocess

parser = argparse.ArgumentParser(description="Web recon tool")

# mode
parser.add_argument("-m", "--mode",help="Mode of fuzzing: subdomains, vhosts, dir, ext, page", dest="mode")
# URL
parser.add_argument("-u", "--url", help="Target URL", dest="url")
# Directory dic
parser.add_argument("-w", "--wordlist", help="Wordlist", dest="wordlist")
# filter
parser.add_argument("-fs", help="filter size", dest="filtro")
# Secure site
parser.add_argument("--secure", help='is a secure site', action='store_true', dest='secure')
# Output file
parser.add_argument("-o", "--output", help="Output file", dest="output")

parser = parser.parse_args()

def execute(command):
    try:
        subprocess.run(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed with return code {e.returncode}")
        print(f"Command: {e.cmd}")
        print(f"Output: {e.output}")
    except FileNotFoundError:
        print("The specified executable or file was not found.")
    except PermissionError:
        print("Permission denied. You might not have sufficient permissions.")
    except ValueError as e:
        print(f"ValueError: {e}")
    except KeyboardInterrupt:
        print("Execution interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")

def buildCommand(command, output, filtro):
    if filtro:
        command += f" -fs {filtro}"
    if output:
        command += f" -o {output}"
    return command

def subdomains(target, wordlist, output, filtro, secure):
    if secure:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u https://FUZZ.{target}/", output=output, filtro=filtro)
    else:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u http://FUZZ.{target}/", output=output, filtro=filtro)
    print(f"Running subdomains fuzzing against {target}...")
    execute(command)
    print("Subdomains fuzzing completed.")

def directories(target, wordlist, output, filtro, secure):
    if secure:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u https://FUZZ.{target}/", output=output, filtro=filtro)
    else:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u http://FUZZ.{target}/", output=output, filtro=filtro)
    print(f"Running directory fuzzing against {target}...")
    execute(command)
    print("Directory fuzzing completed.")

def vhosts(target, wordlist, output, filtro, secure):
    if secure:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u https://{target}/ -H 'Host: FUZZ.{target}'", output=output, filtro=filtro)
    else:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u http://{target}/ -H 'Host: FUZZ.{target}'", output=output, filtro=filtro)
    print(f"Running VHost Fuzzing against {target}...")
    execute(command)
    print("VHost Fuzzing completed.")

def extension(target, wordlist, output, filtro, secure):
    if secure:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u https://{target}/indexFUZZ", output=output, filtro=filtro)
    else:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u http://{target}/indexFUZZ", output=output, filtro=filtro)
    print(f"Running extension Fuzzing against {target}...")
    execute(command)
    print("VHost extension completed.")

def page(target, wordlist, output, filtro, secure):
    if secure:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u https://{target}/FUZZ.php", output=output, filtro=filtro)
    else:
        command = buildCommand(f"ffuf -w {wordlist}:FUZZ -u http://{target}/FUZZ.php", output=output, filtro=filtro)
    print(f"Running page Fuzzing against {target}...")
    execute(command)
    print("VHost page completed.")

def main():
    match parser.mode:
        case "subdomains":
            subdomains(parser.url, parser.wordlist, parser.output, parser.filtro, parser.secure)
        case "dir":
            directories(parser.url, parser.wordlist, parser.output, parser.filtro, parser.secure)
        case "vhost":
            vhosts(parser.url, parser.wordlist, parser.output, parser.filtro, parser.secure)
        case "ext":
            extension(parser.url, parser.wordlist, parser.output, parser.filtro, parser.secure)
        case "page":
            page(parser.url, parser.wordlist, parser.output, parser.filtro, parser.secure)
        case _:
            print("Invalid mode specified")

if __name__ == "__main__":
    main()