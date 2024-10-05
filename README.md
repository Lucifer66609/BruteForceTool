# Brute Force Tool

## Overview

The **Brute Force Tool** is an advanced Python-based application designed for educational and authorized security testing purposes. This tool allows users to perform brute force attacks on web applications by attempting various password combinations against a specified username. It is essential to use this tool responsibly and only on systems where you have explicit permission to conduct security assessments.

## Features

- **Password Mutation**: Automatically generates various mutations of the provided passwords.
- **Concurrent Requests**: Utilizes threading to improve the speed of password attempts.
- **Logging**: Records login attempts and outcomes in a log file for analysis.
- **Customizable**: Accepts a user-defined wordlist for password attempts.

## Requirements

- Python 3.x
- Required Python libraries:
  - `requests`
  - `concurrent.futures`
  - `argparse`
  - `logging`

You can install the required libraries using pip:

```bash
pip install requests current.futures argparse logging
```

##Usage
```bash
python brute_force_tool.py --url <url> --username <username> --wordlist <path_to_wordlist> [--ports <port_numbers>] [--output <output_file>]
```
Command-Line Arguments
- '--url': The target url of the web application to test.
- '--username': The username to use for the brute force attack:
- '--wordlist': Path to the wordlist file containing potential passwords.
- '--ports': (Optional) List of ports for open services (default:22,80,443,8080).
- '--output': (Optional) output file for the security report (default: 'security_report.json').

##Example
```bash
  python brute_force_tool.py --url http://example.com/login --username admin --wordlist passwords.txt
```

## Acknowledgments

- **Open Source Libraries**: This tool utilizes several open-source libraries, including [Requests](https://docs.python-requests.org/en/master/) for handling HTTP requests and [Concurrent Futures](https://docs.python.org/3/library/concurrent.futures.html) for multithreading.
  
- **Inspiration**: The development of this tool was inspired by the need for better security practices and education in ethical hacking.

- **Community Contributions**: Thank you to the ethical hacking community for their ongoing discussions, insights, and resources that contribute to better security awareness.

- **Documentation Resources**: Special thanks to the Python documentation and various online tutorials that helped guide the development of this tool.

##License

This project is licensed under the MIT License. Please refer to the [License](LICENSE) file for details.
##Disclamer
The authors are not responsible for any misuse of this tool. Use it at your own risk.
