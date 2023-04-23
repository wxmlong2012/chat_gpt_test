import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="File name to save")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

request_data = {
    "model": "text-davinci-003",
    "prompt": f"write python script for {args.prompt}",
    "max_tokens": 500,
    "temperature": 0.5,
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"request failed with status code: {str(response.status_code)}")
