# 파일 내용 덮어쓰기
with open('new_file.txt', 'w') as f:
    f.write("Hello world!\n")
    f.write("My name is Codeit.")

# 파일 내용 추가하기
with open('new_file.txt', 'a') as f:
    f.write("Hello world!\n")
    f.write("My name is Codeit.")