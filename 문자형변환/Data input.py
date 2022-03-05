

user = bool(input('입력'))


print(user)
print(type(user))


weather = input('오늘의 날씨를 입력하세요')
print(weather)

width = int(input('가로길이입력'))
height = int(input('세로길이입력'))


print(width * height)
print(width * height/2)

### 포멧 문자열

username = 'hong gil dong'
print(f'User name : {username}')

num = 10
print(type(num), type(str(num)))

num1 = 10
num2 = "10"

print(num1+int(num2))