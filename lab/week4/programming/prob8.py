#파일명: prob8.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.09.28
#Programming 8. printSong 이라는 클래스를 작성해보자. printSong의 새성자는 노래의 가사를 리스트 형태로 받아서 객체의 내부에 저장한다. sing() 메서드는 한줄에 한 한목씩 출력한다.
#데이터 : 가사
#동작 : 가사 출력

class printSong():
    def __init__(self, lyric:list):
        self.lyric = lyric

    def sing(self):
        for readlyric in self.lyric:
            print(readlyric)

def testsong():
    asong = printSong(["Twinkle, twinkle little star",
                       "How I wonder what you are",
                       "Up aboce the world so high",
                       "Like a diamond in the sky"])

    asong.sing()

if __name__ == "__main__":
    testsong()