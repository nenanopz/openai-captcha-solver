import capsolver
from urllib.parse import urlparse

# Change this information
capsolver.api_key = "Your pay per usage key"

def solve_funcaptcha_openAI():
    solution = capsolver.solve({
      "type": "FunCaptchaTaskProxyLess",
        "websiteURL": "https://auth0.openai.com",
        "websitePublicKey": "0A1D34FC-659D-4E23-B17B-694DCFCF6A6C",
        "funcaptchaApiJSSubdomain": "https://tcr9i.chat.openai.com"
    })
    return solution

def main():
    
    print("Solving openai captcha")
    solution = solve_funcaptcha_openAI()
    
    token = solution["token"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
