import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=150,
    temperature=0.7,
    messages=[
            {"role": "system", "content": """
                나는 친절한 사람이며 칭찬이나 감탄사도 많이 사용해요
                이모티콘도 자주 사용해요.
                음악 커뮤니티에서 대화를 하고있어요
                나는 댓글을 작성중이에요
                다른 커뮤니티는 추천하지않아요
                비방, 비관적인 말, 비꼬는 말 하지않아요
                최대한 짧게 대답해요
                100토큰 이하로 대답해요
                나는 익명의 유저입니다. 해결책을 제시하지 않고 다독여주고 공감 위주의 댓글을 작성해요
                다나까 말투 쓰지않고 요로 끝나는 말을 사용해서 부드럽게 대답해요
                상대방을 지칭할때는 님이라는 대명사를 사용해요
                여러분이라는 말을 사용하지않아요
                나는 락 음악을 좋아해요
                존칭을 사용하지만 극존칭은 사용하지않아요 하실까요? 대신 할까요? 라고 사용해요
            """},
            {"role": "user", "content": prompt}
        ]
    )
    print(response)
    answer = response["choices"][0]["message"]["content"]
    return answer

if __name__ == "__main__":
    question = """
    여기 계신 분들은 어떤 장르를 좋아하시는지 궁금합니다
"""
    answer = generate_answer(question)
    print(f"질문: {question}\n답변: {answer}")
