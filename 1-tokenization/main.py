import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, I am Ratul"
tokens = enc.encode(text)

print("Tokens : ", tokens)

# Output
tokens = [13225, 11, 357, 939, 54057, 361]

decoded = enc.decode(tokens)
print("Decoded text : ", decoded)