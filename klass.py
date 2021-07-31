class Klass :
   # 이 친구는 스페셜 메소드
   # 생성자 메소드
    def __new__(cls, name, age) :
        print("객체가 생성되었습니다")
        return object.__new__(cls)

     # 초기화 메소드
    def __init__(self, name, age) :
        print("객체를 초기화 합니다")
        self.name = name
        self.age = age

    # 소멸자 메소드
    def __del__(self) :
        print("객체를 삭제합니다")
        del self
