import openai

# OpenAI API 키 설정
openai.api_key = "your_api_key_here"

def generate_answer(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer

if __name__ == "__main__":
    question = "지구의 반지름은 얼마인가요?"
    answer = generate_answer(question)
    print(f"질문: {question}\n답변: {answer}")
