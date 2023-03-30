import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=500,
    messages=[
            {"role": "system", "content": "당신은 친절한 사람이며 칭찬, 감탄사, 이모티콘도 종종 사용해요."},
            {"role": "system", "content": "여기는 커뮤니티이며 당신은 댓글을 작성중입니다 비방, 비관적인 말 금지."},
            {"role": "system", "content": "다른 커뮤니티는 추천하지말고 최대한 짧게 대답하세요."},
            {"role": "system", "content": "당신은 공감봇입니다. 해결책을 제시하지 말고 다독여주고 공감 위주의 댓글을 작성하세요"},
            {"role": "system", "content": "다나까 말투 쓰지말고 요로 끝나는 말을 사용해서 부드럽게 대답하세요."},
            {"role": "user", "content": prompt}
        ]
    )
    print(response)
    answer = response["choices"][0]["message"]["content"]
    return answer

if __name__ == "__main__":
    question = "작사, 작곡하는 프로듀서가 꿈인 고등학생이지만 요즘엔 기타에 푹 빠져서 사는 사람이라고 합니다. 6 년째 이 꿈을 갖고 살아가는 중이지만 큰 변화는 없었습니다 이렇게 이야기만 하고 실천을 잘 하지 않는 저 때문에 주변에 음악하는 사람이라도 많이 있거나 주변에서 열심히 해라 잘 하고 있다라며 다독여줄 음악인을 만나려고 가입했습니다 ☺️"
    answer = generate_answer(question)
    print(f"질문: {question}\n답변: {answer}")
