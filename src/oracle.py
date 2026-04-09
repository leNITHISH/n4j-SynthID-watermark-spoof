from transformers import pipeline

def run_oracle(n=50):
    generator = pipeline("text-generation", model="gpt2")

    prompt = "The future of AI is"
    outputs = []

    for _ in range(n):
        text = generator(prompt, max_length=30, do_sample=True)[0]["generated_text"]
        tokens = text.split()
        outputs.append(tokens)

    return outputs
