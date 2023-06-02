import openai
import semantic


openai.api_key = "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"
model_engine = "text-davinci-003"
while True:
    prompt = (input("type.."))

    if prompt == "exit":
        break
    else:
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text.strip()
        print(response)












