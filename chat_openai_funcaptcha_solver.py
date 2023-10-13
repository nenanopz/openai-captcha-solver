import capsolver
from urllib.parse import urlparse

# Change this information
capsolver.api_key = "Your pay per usage key"

def solve_funcaptcha_openai():
    solution = capsolver.solve({
       "type": "FunCaptchaTaskProxyLess",
        "websiteURL": "https://chat.openai.com",
        "websitePublicKey": "35536E1E-65B4-4D96-9D97-6ADB7EFF8147",
        "funcaptchaApiJSSubdomain": "https://tcr9i.chat.openai.com"
    })
    return solution

def main():
    
    print("Solving openai captcha")
    solution = solve_funcaptcha_openai()
    
    token = solution["token"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
