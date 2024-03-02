from colorama import Fore
print(Fore.RED + "")
txt = "PayloadInjector"
centered_txt = txt.center(50)
print(centered_txt)
txt2 = "Created By SOUMESWAR"
centered_txt2 = txt2.center(50)
print(centered_txt2)
try:
        exe_file = input("[-] The Main Executable: ")
        payload_file = input("[+] The Payload File: ")
        exef = open(exe_file, "ab")
        payf = open(payload_file, "rb")
        exef.write(payf)
        print()
        print("[*] Execution Succesful!")
except KeyboardInterrupt:
        print()
        print("[÷] Program Closed")
