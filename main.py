from kivy.app import App
from kivy.animation import Animation
from random import randint as rnd
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout

from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.label import Label

from kivymd.theming import ThemeManager

from kivy.lang import Builder

from kivymd.toast import toast
from kivymd.uix.stackfloatingbutton import MDStackFloatingButtons

score=1
Starttheme=[0,1,2,3,4]
click0=1
click1=1
click2=1
click3=1
click4=1

ColThemCheck1=.03,.87,.05,1
ColThemCheck2=.03,.87,.05,1
ColThemCheck3=.03,.87,.05,1
ColThemCheck4=.03,.87,.05,1
ColThemCheck5=.03,.87,.05,1

class ThemeList(Screen):
    def ColorShow(self):
        global ColThemCheck1, ColThemCheck2, ColThemCheck3, ColThemCheck4, ColThemCheck5
        self.ids.Theme1.md_bg_color=ColThemCheck1
        self.ids.Theme2.md_bg_color=ColThemCheck2
        self.ids.Theme3.md_bg_color=ColThemCheck3
        self.ids.Theme4.md_bg_color=ColThemCheck4
        self.ids.Theme5.md_bg_color=ColThemCheck5
    def Theme_check(self,x): #Проверка нажата ли тема
        global click0, click1, click2, click3, click4, ColThemCheck1, ColThemCheck2, ColThemCheck3, ColThemCheck4, ColThemCheck5
        if x==0:
            if click0 == 0:
                Starttheme.append(0)
                ColThemCheck1=self.ids.Theme1.md_bg_color=.03,.87,.05,1
                click0+=1
            elif click0==1 and len(Starttheme)>1:
                ColThemCheck1=self.ids.Theme1.md_bg_color=.91,.13,.12,1
                Starttheme.remove(0)
                click0-=1
        if x==1:
            if click1 == 0:
                Starttheme.append(1)
                ColThemCheck2=self.ids.Theme2.md_bg_color=.03,.87,.05,1
                click1+=1
            elif click1==1 and len(Starttheme)>1:
                Starttheme.remove(1)
                ColThemCheck2=self.ids.Theme2.md_bg_color=.91,.13,.12,1
                click1-=1
        if x==2:
            if click2 == 0:
                Starttheme.append(2)
                ColThemCheck3=self.ids.Theme3.md_bg_color=.03,.87,.05,1
                click2+=1
            elif click2==1 and len(Starttheme)>1:
                Starttheme.remove(2)
                ColThemCheck3=self.ids.Theme3.md_bg_color=.91,.13,.12,1
                click2-=1
        if x==3:
            if click3 == 0:
                Starttheme.append(3)
                ColThemCheck4=self.ids.Theme4.md_bg_color=.03,.87,.05,1
                click3+=1
            elif click3==1 and len(Starttheme)>1:
                Starttheme.remove(3)
                ColThemCheck4=self.ids.Theme4.md_bg_color=.91,.13,.12,1
                click3-=1
        if x==4:
            if click4 == 0:
                Starttheme.append(4)
                ColThemCheck5=self.ids.Theme5.md_bg_color=.03,.87,.05,1
                click4+=1
            elif click4==1 and len(Starttheme)>1:
                Starttheme.remove(4)
                ColThemCheck5=self.ids.Theme5.md_bg_color=.91,.13,.12,1
                click4-=1

    def close_popup(self):
        print (Starttheme)
        global popupWindow
        popupWindow.dismiss()

class MenuScreen(Screen):
    def show_popup(self): #Показать список тем
        global popupWindow
        show = ThemeList()
        popupWindow = Popup(title="Список тем:", content=show, size_hint=(0.95,0.8))
        show.ColorShow()
        popupWindow.open()
    def PlayType(self,x):
        global GameType
        q = QuizApp()
        if x == 1 :
            GameType=1
            self.manager.current = 'quiz'
            q.Playq()
        elif x == 2 :
            GameType=2
            self.manager.current = 'quiz'
            q.Playq()
        elif x == 3 :
            GameType=3
            self.manager.current = 'quiz'
            q.Playq()
        elif x == 4 :
            GameType=4
            self.manager.current = 'quiz'
            q.Playq()
        elif x == 5 :
            GameType=5
            self.manager.current = 'quiz'
            q.Playq()
        elif x == 6 :
            GameType=6
            self.manager.current = 'quiz'
            q.Playq()
        elif x == 7 :
            GameType=7
            self.manager.current = 'quiz'
            q.Playq()
        elif x == 8 :
            GameType=8
            self.manager.current = 'quiz'
            q.Playq()  #Типы игры

TrueAnswer2=0
GameType=0

class Quiz(Screen):
    def animate_the_button_red(self, widget, *args):
        anim = Animation(md_bg_color=(1,0,0,1),duration=0.5)
        anim += Animation(md_bg_color=(0.50,0.1,0.79,1), duration=0.5)
        anim.start(widget)
    def animate_the_button_green(self, widget, *args):
        anim = Animation(md_bg_color=(0.4,0.99,0.28,1),duration=0.5)
        anim += Animation(md_bg_color=(0.50,0.1,0.79,1),duration=0.5)
        anim.start(widget)

    def TextVkl(self):
        global Ans, Ans2, Ans3, Ans4, text1
        self.TextVkl2(Ans, Ans2, Ans3, Ans4, text1)
    def TextVkl2(self, Ans, Ans2, Ans3, Ans4, text1):
        self.ids.Label_text.text=text1
        self.ids.Ans.text=Ans
        self.ids.Ans2.text=Ans2
        self.ids.Ans3.text=Ans3
        self.ids.Ans4.text=Ans4

    def start_timer(self):
        global timet,event
        if GameType == 6 or GameType == 7 or GameType == 8 :
            if GameType==6:
                timet=60
            if GameType==7:
                timet=120
            if GameType==8:
                timet=180
            event=Clock.schedule_interval(self.StartTimer,1)
    def StartTimer(self,dt):
        global timet, event
        if timet==0:
            event.cancel()
            self.manager.current = 'menuscreen'
        if timet!=0:
            timet-=1
            self.ids.Label_timer.text=str(timet)

    def Score_scorer(self):
        global score
        score+=1
        text_score= ('Вопрос\nномер: ' +str(score))
        self.ids.Score_Label.text=text_score

    def Type_or_Score(self,variant):
        global score, GameType,TrueAnswer,TrueAnswer2
        if variant==1:
            if TrueAnswer==self.ids.Ans.text:
                self.animate_the_button_green(self.ids.Ans)
            else:
                self.animate_the_button_red(self.ids.Ans)
        elif variant==2:
            if TrueAnswer==self.ids.Ans2.text:
                self.animate_the_button_green(self.ids.Ans2)
            else:
                self.animate_the_button_red(self.ids.Ans2)
        elif variant==3:
            if TrueAnswer==self.ids.Ans3.text:
                self.animate_the_button_green(self.ids.Ans3)
            else:
                self.animate_the_button_red(self.ids.Ans3)
        elif variant==4:
            if TrueAnswer==self.ids.Ans4.text:
                self.animate_the_button_green(self.ids.Ans4)
            else:
                self.animate_the_button_red(self.ids.Ans4)
        if GameType == 1 and score == 10:
            self.manager.current = 'menuscreen'
            self.Restart_Score_and_timer()
        elif GameType == 2 and score == 20:
            self.manager.current = 'menuscreen'
            self.Restart_Score_and_timer()
        elif GameType == 3 and score == 30:
            self.manager.current = 'menuscreen'
            self.Restart_Score_and_timer()
        elif GameType == 4 and variant==1:
            if self.ids.Ans.text!=TrueAnswer:
                self.manager.current = 'menuscreen'
                self.Restart_Score_and_timer()
        elif GameType == 4 and variant==2:
            if self.ids.Ans2.text!=TrueAnswer:
                self.manager.current = 'menuscreen'
                self.Restart_Score_and_timer()
        elif GameType == 4 and variant==3:
            if self.ids.Ans3.text!=TrueAnswer:
                self.manager.current = 'menuscreen'
                self.Restart_Score_and_timer()
        elif GameType == 4 and variant==4:
            if self.ids.Ans4.text!=TrueAnswer:
                self.manager.current = 'menuscreen'
                self.Restart_Score_and_timer()
        elif GameType == 5 and variant==1:
            if self.ids.Ans.text!=TrueAnswer:
                TrueAnswer2+=1
                if TrueAnswer2==3:
                    self.manager.current = 'menuscreen'
                    self.Restart_Score_and_timer()
                    TrueAnswer2=0
        elif GameType == 5 and variant==2:
            if self.ids.Ans2.text!=TrueAnswer:
                TrueAnswer2+=1
                if TrueAnswer2==3:
                    self.manager.current = 'menuscreen'
                    self.Restart_Score_and_timer()
                    TrueAnswer2=0
        elif GameType == 5 and variant==3:
            if self.ids.Ans3.text!=TrueAnswer:
                TrueAnswer2+=1
                if TrueAnswer2==3:
                    self.manager.current = 'menuscreen'
                    self.Restart_Score_and_timer()
                    TrueAnswer2=0
        elif GameType == 5 and variant==4:
            if self.ids.Ans4.text!=TrueAnswer:
                TrueAnswer2+=1
                if TrueAnswer2==3:
                    self.manager.current = 'menuscreen'
                    self.Restart_Score_and_timer()
                    TrueAnswer2=0
        else:
            g=QuizApp()
            g.Playq()
            self.TextVkl()
            self.Score_scorer()
    def Restart_Score_and_timer(self):
        global score,timet
        score=1
        timet=0
        self.ids.Label_timer.text=''
        text_score=('Вопрос\nномер: '+str(score))
        self.ids.Score_Label.text=text_score

kv=Builder.load_string(open('Quizzz.kv',encoding='utf-8').read())

class QuizApp(App):

    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Indigo'

    def Playq(self):
        global Starttheme, Ans, Ans2, Ans3, Ans4, text1,TrueAnswer
        ThemeQuestions=[
        [['Вопрос 1 темы 1','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 2 темы 1','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 3 темы 1','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ']],

        [['Вопрос 1 темы 2','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 2 темы 2','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 3 темы 2','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ']],

        [['Вопрос 1 темы 3','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 2 темы 3','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 3 темы 3','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ']],

        [['Вопрос 1 темы 4','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 2 темы 4','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 3 темы 4','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ']],

        [['Вопрос 1 темы 5','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 2 темы 5','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ'],
        ['Вопрос 3 темы 5','Правильный ответ','Неправильный ответ','Неправильный ответ','Неправильный ответ']]
        ]


        St1 = Starttheme.copy() # Копия массива выбранных тем (b)
        Pl = rnd (0,len(St1)-1) # Выбирает номер конкретной темы (x)
        Pl = St1 [Pl] # Номер темы (x)
        QThem = len (ThemeQuestions [Pl]) # Кол-во вопросов в теме (c)
        QNum = rnd (0,QThem-1) # Порядковый номер массива вопроса (d)
        QnumK = ThemeQuestions [Pl] # Массив вопросов одной темы (copy)
        QnumK = QnumK[QNum] # Сам массив вопроса  (copy)
        QnumKcopy = QnumK # Копия массива вопроса (copy1)
        text1 = QnumK [0] # Текст вопроса

        TrueAnswer=QnumK[1] #Правильный ответ
        NumAns = rnd (1, len(QnumKcopy) - 1) # Порядковый номер 1 ответа
        Ans = str (QnumKcopy [NumAns]) # Ответ в первой кнопке
        QnumKcopy.pop (NumAns) #Удаляем использованный ответ

        NumAns2 = rnd (1, len(QnumKcopy) - 1) # Порядковый номер 2 ответа
        Ans2 = str (QnumKcopy [NumAns2]) # Ответ во второй кнопке
        QnumKcopy.pop (NumAns2) # Удаляем использованный ответ

        NumAns3 = rnd (1, len(QnumKcopy) - 1) # Порядковый номер 3 ответа
        Ans3 = str (QnumKcopy [NumAns3]) # Ответ в третьей кнопке
        QnumKcopy.pop (NumAns3)  # Удаляем использованный ответ

        NumAns4 = rnd (1, len(QnumKcopy) - 1) # Порядковый номер 4 ответа
        Ans4 = str (QnumKcopy [NumAns4]) # Ответ в четвертой кнопке
        QnumKcopy.pop (NumAns4) # Удаляем использованный ответ

        return Ans, Ans2, Ans3, Ans4, text1,TrueAnswer

    def Clean_Startheme(self):
        global Starttheme
        Starttheme=list()
        return Starttheme

    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='menuscreen'))
        sm.add_widget(Quiz(name='quiz'))
        return sm

if __name__ == '__main__':
    QuizApp().run()
