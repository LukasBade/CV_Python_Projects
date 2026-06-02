import hashlib 
#Secure Hash Algorithm 1 (SHA-1) to hash the password for extra security
#Info: Website API does not accept raw passwords, so locally hashing is needed

def hashing(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    #encode converts string into bytes, hexdigest into readable hex string, upper to match API format (all uppercase)
    prefix, suffix = sha1[:5], sha1[5:]
    #splitting hash into 2 parts for security reasons
    return sha1, prefix, suffix