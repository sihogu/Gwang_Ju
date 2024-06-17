class 학생_성적_관리프로그램():
    UI=f"""-----학생 성적 관리 프로그램-----
1.학생 정보 입력
2.현재 작성된 학생 성적 목록 보기
3.현재 작성된 학생 성적 목록 저장
4.저장된 학생 성적 불러오기
5.종료

입력:"""
    student_list = []

    def __init__(self,name,birthday,quiz,mid,final,absent,assignment):
        self.name = name
        self.birthday = birthday
        self.quiz = quiz
        self.mid = mid
        self.final = final
        self.absent = absent
        self.assignment = assignment
        self.old = 2025 - int(str(birthday)[0:4])
        self.grade = self.make_grade(quiz,mid,final,absent,assignment)
        #^어떻게 작동하는지 잘생각해보기, 초기값을 각각의 단어로 받는지

    def __repr__(self):
        return f"""이름 : {self.name}
나이 : {self.old}살
생년월일 : {self.birthday}
퀴즈 점수 : {self.quiz}점
중간고사 점수 : {self.mid}점
기말고사 점수 : {self.final}점
과제 점수 : {self.assignment}점
결석일수 : {self.absent}일
학점 : {self.grade}
"""
    @classmethod
    def input(cls):
        name = input('학생 이름:')
        birthday = int(input('생년월일(ex 19990101):'))
        quiz = int(input('퀴즈 점수:')) 
        mid = int(input('중간고사 점수:'))
        final = int(input('기말고사 점수:')) 
        assignment = int(input('과제 점수:'))
        absent = int(input('결석일수:'))
        old = 2025 - int(str(birthday)[0:4])
        grade = cls.make_grade(quiz,mid,final,absent,assignment)
        cls.student_list.append(학생_성적_관리프로그램(name,birthday,quiz,mid,final,assignment,absent,old,grade))
        #왜 직접 넣지않고 인스턴스로 넣지??


    @classmethod
    def make_grade(quiz,mid,final,absent,assignment):
        cls.quiz = cls
    
    @classmethod
    def show(cls):
        pass
    
    @classmethod
    def save(cls):
        pass

    @classmethod
    def load(cls):
        pass
    
    @classmethod
    def off(cls):
        return True
    


def main():
    sg=학생_성적_관리프로그램
    동작기=[sg.input,sg.show,sg.save,sg.load,sg.off]
    run=0
    while not run:
        try:
            n=int(input(sg.UI))
            run=동작기[n-1]()
        except:
            print("잘못 입력 되었습니다.\n기능은 1~5까지만 있습니다.")
            continue
    else:
        print("학생 성적 관리 프로그램이 종료 됩니다.")

if __name__=="__main__":
    main()