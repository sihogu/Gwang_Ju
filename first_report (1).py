import turtle as t
import pickle
import os

class 거북이_그림:
    UI=f"""@@@@거북이로 도형 그리기 프로그램@@@@
1.도형 정보 입력
2.도형 그리기
3.입력된 도형들 목록 보기
4.저장된 도형 보기
5.현재 볼 수 있는 도형 목록
6.종료

입력:"""
    도형_리스트 = []

    def __init__(self,이름,도형,변_길이,색상1,색상2): #인스턴스의 초기 값
        self.이름 = 이름
        self.도형 = 도형
        self.변_길이 = 변_길이
        self.색상1 = 색상1
        self.색상2 = 색상2
        
    def __repr__(self): #디버깅과 개발에 용이한 표현
        return f"""이름 : {self.이름}
도형 : {self.도형}각형
한 변의 길이 : {self.변_길이}
변의 색상 : {self.색상1}
면의 색상: {self.색상2}"""

    @classmethod
    def input_polygon(cls):
        이름 = input('그림_이름:')
        도형 = int(input('N각형(1이상의 정수):'))
        변_길이 = int(input('한 변의 길이:'))
        색상1 = input('변의 색상 \n(노란색, 파란색, 빨간색, 검정색, 하얀색, 분홍색, 초록색 중):')
        색상2 = input('면의 색상:')
        cls.도형_리스트.append(거북이_그림(이름,도형,변_길이,색상1,색상2))
        print('입력이 완료 되었습니다.')
    
    @classmethod
    def 목록출력(cls):
        if len(cls.도형_리스트) == 0:
            print('도형 정보를 먼저 입력해주세요\n')
            return
        print("목록출력")
        for i in cls.도형_리스트:
            print(i)
            print("-"*20)
        print("목록출력이 종료 되었습니다.")
        
    @classmethod
    def draw_polygon(cls):
        if len(cls.도형_리스트) == 0:
            print('도형 정보를 먼저 입력해주세요\n')
            return

        cls.이름 = cls.도형_리스트[-1].이름
        cls.도형 = cls.도형_리스트[-1].도형
        cls.색상1 = cls.translater(cls.도형_리스트[-1].색상1)
        cls.색상2 = cls.translater(cls.도형_리스트[-1].색상2)
        cls.변_길이 = cls.도형_리스트[-1].변_길이
        t.home()
        t.shape('turtle')
        t.color(cls.색상1,cls.색상2)
        t.begin_fill()
        for i in range(cls.도형):
            t.forward(cls.변_길이)
            t.left(360/cls.도형)
        t.end_fill()
        
        # 거북이 상태 저장
        t_state = {
            'position': t.position(),
            'heading': t.heading(),
            'pensize': t.pensize(),
            'pencolor': t.pencolor(),
            'fillcolor': t.fillcolor(),
            'isdown': t.isdown(),
            '변_길이': cls.변_길이,
            '도형': cls.도형,
            '색상1': cls.색상1,
            '색상2': cls.색상2
        }

        with open(f'{cls.이름}.pkl', 'wb') as f:
            pickle.dump(t_state, f)
        t.done()
        print('그림이 정상적으로 완성되었습니다.')
        
    @classmethod
    def load_polygon(cls):
        cls.이름 = input('불러올 그림 이름:')
        
        #t.hideturtle()  # 거북이를 숨깁니다.
        
        # 저장된 상태 로드
        try:
            with open(f'{cls.이름}.pkl', 'rb') as f:
                t_state = pickle.load(f)
        except:
            print('존재하지 않는 파일명입니다.')

        # 거북이 상태 복원
        """t.penup()
        t.setposition(t_state['position'])
        t.setheading(t_state['heading'])
        t.pensize(t_state['pensize'])
        t.pencolor(t_state['pencolor'])
        t.fillcolor(t_state['fillcolor'])
        if t_state['isdown']:
            t.pendown()"""
        try:
            t.color(t_state['색상1'], t_state['색상2'])
            t.begin_fill()
            for _ in range(t_state['도형']):
                t.forward(t_state['변_길이'])
                t.left(360 / t_state['도형'])
            t.end_fill()
            t.done()
            print('그림이 정상적으로 불러와졌습니다.')
        except:
            print('문제가 발생하였습니다. 프로그램 종료 후 다시 이용해 주세요.')

    @classmethod
    def translater(cls,korean):
        cls.color = {'노란색':'yellow',
                '파란색':'blue',
                '빨간색':'red',
                '검정색':'black',
                '하얀색':'white',
                '분홍색':'violet',
                '초록색':'green'}
        return cls.color[korean]
    
    @classmethod
    def 파일_목록(cls):
        print(os.listdir())
    
    @classmethod
    def 종료(cls):
        return True


#draw_polygon(이름, 변_길이, 도형, translater(색상1), translater(색상2))
#load_polygon(이름)

def main():
    dp=거북이_그림
    동작기=[dp.input_polygon,dp.draw_polygon,dp.목록출력,dp.load_polygon,dp.파일_목록,dp.종료]
    run=0
    while not run:
        try:
            n=int(input(dp.UI))
            run=동작기[n-1]()
        except:
            print("잘못 입력 되었습니다.\n기능은 1~6까지만 있습니다.")
            continue
    else:
        print("거북이 도형 그리기 프로그램이 종료 됩니다.")

if __name__=="__main__":
    main()