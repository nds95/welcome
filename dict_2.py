# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수

def reverse_dict(dict):         # 'reverse_dict'라는 사전뒤집기 기능 구현
    new_dict = {}       # return에서 가져온 사전을 new_dict라고 정의함

    for key, value in dict.items():     #for문을 활용한 사전 key, value값 가져오기
        new_dict[value] = key       #new_dict라는 사전에 value값을 key값으로 변환

    return new_dict # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'consctience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print('영-한 단어장\n{}\n'.format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print('한-영 단어장\n{}'.format(reversed_vocab)
)