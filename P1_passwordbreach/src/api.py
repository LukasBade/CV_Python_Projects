import requests

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


