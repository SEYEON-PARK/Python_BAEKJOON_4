#두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오. (0 < A, B < 10)

A=int(input("0보다 큰 정수를 입력하시오. : ")) # 정수 A 입력받기.

while(A<=0):
    if(A<=0):
      print("잘못 입력하셨습니다.")
      A=int(input("0보다 큰 정수를 입력해주세요. : "))
    continue
    
B=int(input("10보다 작은 정수를 입력하시오. : ")) # 정수 B 입력받기.

while(B>=10):
    if(B>=10):
      print("잘못 입력하셨습니다.")
      B=int(input("10보다 작은 정수를 입력해주세요. : "))
    continue

print(A-B)
