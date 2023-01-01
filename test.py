import openai

openai.api_key = "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"

# response = openai.Completion.create(
#   engine="davinci",
#   prompt="world is full of pain and suffering",
#   max_tokens=20,
#   temperature=0.5,
# )

# generated_text = response["choices"][0]["text"]
# print(generated_text)
query = str(input("Enter query: "))
response = openai.Image.create(
  prompt=query,
  n=1,
  size="256x256"
)
image_url = response['data'][0]['url']
print(image_url)