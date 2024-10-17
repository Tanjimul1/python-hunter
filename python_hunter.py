import os
import requests
from bs4 import BeautifulSoup
from scapy.all import *
from pwn import *

class PythonHunter:
    def __init__(self):
        self.logo = '''
        ================================
        |        Python Hunter  v 3.0  |
        ================================
        '''
        print(self.logo)

    def display_help(self):
        help_text = '''
        Available Commands:
        - find_xss <target>
        - find_sqli <target>
        - find_rce <target>
        - exploit <target>
        - analyze_malware <sample>
        - help
        - exit
        '''
        print(help_text)

    def find_xss(self, target):
        try:
            response = requests.get(target)
            if "<script>" in response.text:
                print(f"Potential XSS vulnerability found in {target}")
            else:
                print("No XSS vulnerabilities found.")
        except Exception as e:
            print(f"Error: {str(e)}")

    def find_sqli(self, target):
        try:
            response = requests.get(target + "'")
            if "SQL syntax" in response.text:
                print(f"Potential SQL Injection vulnerability found in {target}")
            else:
                print("No SQL Injection vulnerabilities found.")
        except Exception as e:
            print(f"Error: {str(e)}")

    def find_rce(self, target):
        try:
            payload = {'cmd': 'whoami'}
            response = requests.post(target, data=payload)
            if response.text.strip() == "www-data":
                print(f"Potential RCE vulnerability found in {target}")
            else:
                print("No RCE vulnerabilities found.")
        except Exception as e:
            print(f"Error: {str(e)}")

    def exploit(self, target):
        try:
            print(f"Executing exploit on {target}...")
            
        except Exception as e:
            print(f"Error: {str(e)}")

    def analyze_malware(self, sample):
        try:
            print(f"Analyzing malware sample: {sample}...")
            
        except Exception as e:
            print(f"Error: {str(e)}")

    def run(self):
        while True:
            command = input("PythonHunter> ")
            if command == "exit":
                break
            elif command == "help":
                self.display_help()
            elif command.startswith("find_xss"):
                target = command.split(" ")[1]
                self.find_xss(target)
            elif command.startswith("find_sqli"):
                target = command.split(" ")[1]
                self.find_sqli(target)
            elif command.startswith("find_rce"):
                target = command.split(" ")[1]
                self.find_rce(target)
            elif command.startswith("exploit"):
                target = command.split(" ")[1]
                self.exploit(target)
            elif command.startswith("analyze_malware"):
                sample = command.split(" ")[1]
                self.analyze_malware(sample)
            else:
                print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    tool = PythonHunter()
    tool.run()

