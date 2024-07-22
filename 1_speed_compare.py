
from openai import OpenAI
import time, os

os.environ['OPENAI_API_KEY'] = ''

def measure_generation_time(model, prompt, max_tokens=50):
    start_time = time.time()
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    end_time = time.time()
    generation_time = end_time - start_time
    tokens_generated = len(response.choices[0].message.content.split())
    time_per_token = generation_time / tokens_generated if tokens_generated else 0
    return generation_time, tokens_generated, time_per_token

def main():
    models = ["gpt-3.5-turbo", "gpt-4o", "gpt-4o-mini-2024-07-18"]
    prompt = "Once upon a time in a faraway land, there lived a"

    print(f"{'Model':<20}{'Total Time (s)':<20}{'Tokens Generated':<20}{'Time per Token (s)':<20}")
    print("="*80)

    for model in models:
        total_time, tokens, time_per_token = measure_generation_time(model, prompt)
        print(f"{model:<30}{total_time:<20.4f}{tokens:<20}{time_per_token:<20.4f}")

if __name__ == "__main__":
    main()
