from colorama import Fore
print(Fore.RED + "")
txt = "PayloadInjector"
centered_txt = txt.center(50)
print(centered_txt)
txt2 = "Created By TheRedHackingHub"
centered_txt2 = txt2.center(50)
print(centered_txt2)
try:
	exe_file = input("[-] The Main Executable File: ")
	payload_file = input("[+] The Payload File To Inject: ")
	exef = open(str(exe_file), "ab")
	payf = open(str(payload_file), "rb")
	exef.append("\n")
	exef.append(payf)
	print()
	print("[*] Execution Succesful!")
except KeyboardInterrupt:
	print()
	print("[÷] Program Closed")

