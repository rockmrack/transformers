from transformers import pipeline

pipe = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

prompt = "Write a short professional greeting for a quotation email to a client."

result = pipe(prompt, max_new_tokens=60)
print(result[0]["generated_text"])