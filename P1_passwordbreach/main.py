import requests
import hashlib 
#Secure Hash Algorithm 1 (SHA-1) to hash the password to not expose it
#Website API does not accept raw passwords, to locally hashing is needed

def hashing(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    #encode converts string into bytes, hexdigest into readable hex string, upper to match API format (all uppercase)
    prefix, suffix = sha1[:5], sha1[5:]
    #splitting hash into 2 parts for security reasons
    return sha1, prefix, suffix

def checkforbreach(prefix, suffix):
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    #Call API, giving prefix as call parameter

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")
    #Error checking


    hashes = response.text.splitlines()
    #Splitting answer into suffixes and count of breaches (EXAMPLEHASH:1)


    for line in hashes:
        returned_suffix, count = line.split(":")
        if returned_suffix == suffix:
            return f"Found in {count} breaches."
    return "Found in 0 breaches."
    #Comparing suffixes for matches, adding count upon match



password = input("Enter your password: ")

hashed_password = hashing(password)

print(f"SHA-1 Hash: {hashed_password}")
print("Checking if your password has been breached...")
result = checkforbreach(hashed_password[1], hashed_password[2])
print(result)
