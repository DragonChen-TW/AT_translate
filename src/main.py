from openai import OpenAI
from dotenv import load_dotenv
import logging

status = load_dotenv()
logging.info(f"Status of loading .env file: {status}")
client = OpenAI()

msgs = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {
        "role": "assistant",
        "content": "The Los Angeles Dodgers won the World Series in 2020.",
    },
    {"role": "user", "content": "Where was it played?"},
]

total_len = sum([len(m['content']) for m in msgs])
print('total_len:', total_len, 'tokens: 53')


# response = client.chat.completions.create(model="gpt-3.5-turbo", messages=msgs)
# print(response)