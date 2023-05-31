from openai import ChatCompletion

class pyknopa:
    def __init__(self, api_key):
        self.chat_completion = ChatCompletion(api_key=api_key)


    def goodanswer(self, query):
        response = self.chat_completion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a user"},
                {"role": "user", "content": query}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return answer
