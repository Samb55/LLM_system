from openai import OpenAI


class LLMService:
    def __init__(self):
        self.openai = OpenAI()
        self.model = "gpt-3.5-turbo"

    def get_response(self, user_input):
        completion = self.openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a personal assistant helping me to answer my questions."},
                {"role": "user", "content": user_input},
            ]
        )
        return completion.choices[0].message.content
    



if __name__ == "__main__":
    print(LLMService().get_response("What is the captial of USA?"))
