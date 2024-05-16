define slow_dissolve = Dissolve(1.0)
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

 
# Определение персонажей игры
define e = Character('', color="#c8ffc8")
define k = Character('Коля', color="#5b6908")
define i = Character('Илья', color="#000000")
define o = Character('Оля', color="#3d000a")
define s = Character('Саша', color="#220038")
define d = Character('Дед Митрофан', color="#dd0a62")
define m = Character('Мужик', color = "#3b2e03")
define l = Character('Леший', color = "#025c18")
define p = Character('Прохор', color = "#3b2e03")
# Определение функций для мини-игры
image Kolya = "Kolya.png"
image SashaM = "Malenkaya Sasha.png"
image Sasha = "Vzroslaya Sasha.png"
image Olya = "Olya.png"
image Ded Mitrofan = "Ded Mitrofan.png"
image Myzhik = "Myzhik.png"
image Leshiy = "Leshiy.png"
image friends = "friends.png"
image Zadnik lug = "1.png"
image Ilustraciya Les= "2.png"
image Lesnaya tropa 1 = "3.png"
image Izba = "4.png"
image Stol v izbe = "5.png"
image Dark = "7.png"
image Izba vnytri = "6.png"
image Pugalka strashilka = "8.png"
image Gorodskaya izba vnytri = "9.png"
image Ymivalnik = "10.png"
image Gorodskaya izba vhod = "11.png"
image Ylica goroda= "12.png"
image Lesnaya tropa 2 = "13.png"
image Slavyanskaya kachalka = "14.png"
image Kamen podnyal Kamen = "15.png"
image Lesnaya tropa 3 = "16.png"
image Polyana = "17.png"
image Dyb = "18.png"
image Kryzhka kosti = "19.png"
image Konec1 = "20.png"
image pong1="field.png"
image c5 = "Cubes 5.png"
image c8 = "Cubes 8.png"
image c9 = "Cubes 9.png"
image c12 = "Cubes 12.png"
image Portal = "Portal.png"
image Malenkaya Sasha Speaking:
    "Malenkaya Sasha Speaking.png"
    pause .5
    "Malenkaya Sasha.png"
    pause .5
    repeat
image Sasha Speaking:
    "Vzroslaya Sasha Speaking.png"
    pause .5
    "Vzroslaya Sasha.png"
    pause .5
    repeat
image Olya Speaking:
    "Olya Speaking.png"
    pause .5
    "Olya.png"
    pause .5
    repeat
image Kolya Speaking:
    "Kolya Speaking.png"
    pause .5
    "Kolya.png"
    pause .5
    repeat
image Ded Mitrofan Speaking:
    "Ded Mitrofan Speaking.png"
    pause .5
    "Ded Mitrofan.png"
    pause .5
    repeat
image Myzhik Speaking:
    "Myzhik Speaking.png"
    pause .5
    "Myzhik.png"
    pause .5
    repeat
image Leshiy Speaking:
    "Leshiy Speaking.png"
    pause .5
    "Leshiy.png"
    pause .5
    repeat

# Музыка и звуки
define audio.forest = "sounds/Forest.ogg"
define audio.gym = "sounds/GYM.ogg"
define audio.oak = "sounds/WiseOak.ogg"
define audio.horror = "sounds/Horror.ogg"
define audio.birds = "sounds/Birds.ogg"
define audio.howl = "sounds/Howl.ogg"
define audio.washing = "sounds/Washing.ogg"
define audio.town = "sounds/Town.ogg"
define audio.door = "sounds/Door.ogg"
define audio.menu = "sounds/Menu.ogg"
define audio.house = "sounds/House.ogg"

init python:
    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 12
            self.PADDLE_HEIGHT = 95
            self.PADDLE_X = 240
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_TOP = 70
            self.COURT_BOTTOM = 1050

            # Some displayables we use.
            self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery

            # The speed of the computer.
            self.computerspeed = 370.0

            # The position, delta-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 800.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy
                if not self.stuck:
                    renpy.sound.play("beep.opus", channel=0)
                

            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy
                if not self.stuck:
                    renpy.sound.play("beep.opus", channel=0)
                

            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True
                        
                    if hit:
                        renpy.sound.play("boop.opus", channel=1)
                        self.bspeed *= 1.10
                    

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
            int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "Дед Митрофан"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "Илья"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()
    def r():
        import random
        return random.randint(1, 4) 
    


screen pong():

    default pong = PongDisplayable()

    add "pong1"
    
    add pong

    text "Илья":
        xpos 240
        xanchor 0.5
        ypos 25
        size 40

    text "Дед Митрофан":
        xpos (1880 - 240)
        xanchor 0.5
        ypos 25
        size 40

    if pong.stuck:
        text "Click to Begin":
            xalign 0.5
            ypos 50
            size 40

label play_pong:

    window hide  # Hide the window and quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

if _return == "Илья":
    show Ded Mitrofan Speaking at left
    with moveinleft
    d "Справился-таки! Ай да юнец! Дай руку пожму!"
    hide Ded Mitrofan Speaking
    show Ded Mitrofan at left
    e "Я опустил камень на землю. И протянул руку деду Митрофану. Старик так сжал мою кисть, что я подумал, что он сейчас, как жернова, перемелет мне все кости."
    hide Ded Mitrofan
    show Ded Mitrofan Speaking at left
    d "Ну, ты знаешь, что делать дальше. Вон, там другой молодняк идёт, мне пора."
    hide Ded Mitrofan Speaking
    show Ded Mitrofan at left
    i "Хорошо!"
    hide Ded Mitrofan 
    with moveoutleft
    return
else:
    show Ded Mitrofan at left
    with moveinleft
    d "Хлипкие нынче молодцы! Ну и ладно, я не думал, что ты поднимешь, возьми камень поменьше и пробуй снова."
    $ renpy.jump("play_pong")  


label start:

    scene Zadnik lug

    play music birds volume 0.8

    e "Палящее июньское солнце постепенно начинает скрываться за горизонтом, на небе становятся видны первые звёзды. "

    e "Хотя мы и гуляли почти у самой реки, было довольно тепло. Бесконечный луг, усеянный касатиками, не хотел нас отпускать, хотя назойливые комары уже начинали напоминать, что пора бы возвращаться домой."

    e "Как назло, всё это происходило в самый разгар нашей игры. Сегодня мы почти весь вечер играли в «жмурки». Участь «воды», как правило, доставалась Саше, пухленькой девочке шести лет от роду. "

    e "Мне и самому было тогда шесть, но я был одним из самых резвых детей среди ровесников, а потому в играх, требующих ловкости или скорости, я почти не проигрывал. "

    e "Сегодняшний день не был исключением. За весь вечер я ещё ни разу не водил. Всего нас было четверо: я, Саша, Коля и Оля. "

    e "Коля был нашим с Сашей ровесником, а вот Оле, старшей сестре Коли, было уже восемь. Родители отправили её присмотреть за нами. "
    
    e "Водил Коля. Оля завязала ему глаза, раскрутила его и отбежала, после чего Коля стал пытаться поймать кого-нибудь из нас, ориентируясь только по звукам. "

    e "Я в очередной раз хлопнул в ладоши, и только я собирался отпрыгнуть в сторону, чтобы избежать столкновения, с отозвавшимся на мой хлопок Колей, как вдруг…"

    e "… как вдруг я услышал страшный вой со стороны леса. От этого воя меня бросило в дрожь. Я понял, что не могу пошевелить и пальцем. Дыхание участилось, а в глазах потемнело."

    scene Ilustraciya Les

    e "Я уже начал терять сознание, как вдруг меня сбили с ног. Коля побежал на мой хлопок, споткнулся и упал, прихватив с собой меня. Эта неожиданность привела меня в чувства."
    with vpunch
    scene Zadnik lug
    with slow_dissolve
    $ renpy.vibrate(0.5)
    show Kolya Speaking at left
    with moveinleft
    k "Прости. Я споткнулся, а ты мне под руку попался."
    hide Kolya Speaking
    show Kolya at left

    play sound howl
    with hpunch
    i "Вы слышали?"
    hide Kolya at left
    with moveoutleft
    

    scene Zadnik lug

    with dissolve

    show Kolya at center
    with moveinbottom
    show SashaM at left
    with moveinleft
    show Olya at right
    with moveinright
    e "Все вопросительно на меня посмотрели."
    hide Kolya at center
    with moveoutbottom
    hide SashaM at left 
    with moveoutleft
    hide Olya at right
    with moveoutright
    scene Zadnik lug
    with dissolve
    show Olya Speaking at left 
    with moveinleft
    o "Что слышали?"
    hide Olya Speaking
    show Olya at left 
    i "Вой в лесу."
    hide Olya
    show Olya Speaking at left 
    o "Не было никакого воя. Может, ты плохо себя чувствуешь?"
    hide Olya Speaking
    show Olya at left 
    i "Сейчас я чувствую себя хорошо. Но только что…"
    hide Olya
    show Olya Speaking at left 
    o "Что?"
    hide Olya Speaking
    show Olya at left 
    i "Ничего."

    show Malenkaya Sasha Speaking at center

    with moveinleft

    s "В любом случае, теперь ты должен водить."
    hide Malenkaya Sasha Speaking
    show SashaM at center

    e "Действительно. Хоть и случайно, но Коля меня запятнал. И всё же, что это был за вой в лесу?"
    hide SashaM
    with moveoutright
    hide Olya
    with moveoutleft
    e "Во всяком случае, сейчас я на этот вопрос не отвечу. Мы продолжили. Мне завязали глаза, раскрутили, и сказали досчитать до двадцати. Настало время испытать свои силы в качестве воды в «жмурках»."
    
    with vpunch
    $ renpy.vibrate(0.5)
    e "Со всех сторон послышались негромкие хлопки. Два, как мне показалось, ближайших хлопка раздавались с двух противоположных сторон. На чей же хлопок мне пойти?"

    with hpunch
    $ renpy.vibrate(0.5)
    scene Zadnik lug

    

    e "Выберите направление, в котором хотите пойти."
    
    menu:
        "Влево":
            with vpunch
            $ renpy.vibrate(0.5)
            e "Я рванул влево, и тут же споткнулся."
            e "Я снял повязку. Навернулся я несильно, но ладошку ободрал."
            show Olya Speaking at right
            with moveinright
            o "Не сильно болит?"
            hide Olya Speaking
            show Olya at right
            i "Немного."
            hide Olya
            show Olya Speaking at right
            o "Ладно, тогда идём домой, там всё и обработаем."
            hide Olya Speaking
            with moveoutleft
            e "И без этого уже пора было бы возвращаться. Все уже порядком наигрались, потому никто сильно не расстроился."

        "Вправо":
            e "Я прыгнул вправо, и тут же схватил кого-то. Это был Коля."
            with vpunch
            $ renpy.vibrate(0.5)
            show Kolya Speaking at left
            with moveinleft
            k "Но я только водил. Давай ещё раз."
            hide Kolya Speaking
            show Kolya at left
            i "Ладно, давай."
            e "Коля был редкостным плаксой, потому я и согласился. Мне бы и хотелось настоять на своём мнении, но я знал, что в таком случае он просто заревёт и откажется играть, после чего игра закончится, и мы пойдём домой."
            e "Но, к несчастью для Коли, и второй раз мной пойман был именно он."
            hide Kolya
            show Kolya Speaking at left
            k "Ты подглядываешь!"
            hide Kolya Speaking
            show Kolya at left
            i "Не подглядываю! Просто ты тормоз!"
            hide Kolya 
            show Kolya Speaking at left
            k "Я? Да сам ты тормоз!"
            hide Kolya Speaking
            show Kolya at left
            i "Если я тормоз и быстрее тебя, то кто ты?"
            show Olya Speaking at right
            with moveinright
            o "Прекратите! Раз вы так себя ведёте, мы идём домой."
            hide Kolya
            with moveoutright
            hide Olya Speaking
            with moveoutright

    scene Lesnaya tropa 1
    e "Мы шли с луга по заросшей тропинке, кругом уже ухали совы. В траве стрекотали кузнечики."

    scene Izba
    e "Когда мы пришли, только в нашей избе ещё горел свет. Мы вошли внутрь."

    play sound door
    # play music house volume 0.35
    stop music

    scene Stol v izbe
    e "Родители Коли и Оли уже накрывали на стол. Сегодня подавали: запечённые свиные рёбрышки, разогретые щи, и главное блюдо вечера – испечённые на сале блины со сметаной."
    show Olya Speaking at center
    with moveinleft
    o "Сначала мясо и щи, а потом блины!"
    hide Olya Speaking
    show Olya
    e "Пришлось поступить, как повелела Оля."
    hide Olya 
    with moveoutleft
    e "После ужина все стали готовиться ко сну."

    scene Dark
    with slow_dissolve
    e "Мы с Сашей приехали в эту деревню на лето..."
    e "Жизнь здесь не остановилась, а, скорее, задремала."

    scene Izba vnytri
    e "Сама же Оля расположилась на нарах. Я с Сашей и Колей лёг на полатях."
    e "Было тепло и тихо, но я не мог уснуть. Мне не давал покоя вой в лесу."
    e "Стоило мне повернуться на бок и открыть глаза…"

    play sound horror

    scene Pugalka strashilka
    
    e "… как почти перед самым моим лицом предстал тёмный силуэт, с двумя огромными яркими глазами. "
    s "Илья, вставай!"
    with vpunch
    $ renpy.vibrate(0.5)
    scene Gorodskaya izba vnytri
    with slow_dissolve
    show Sasha at center
    with moveinbottom
    stop sound
    e "Я проснулся у себя дома."
    e "Возле нар стояла Саша и хмуро смотрела на меня."
    hide Sasha
    show Sasha Speaking
    s "Ты хоть сегодня на занятия пойдёшь?"
    hide Sasha Speaking
    show Sasha
    i "Сколько сейчас?"
    hide Sasha
    show Sasha Speaking
    s "Уже половина восьмого."
    hide Sasha Speaking
    show Sasha
    i "Вот же!"
    hide Sasha
    with moveoutleft
    e "Саша вышла из комнаты. Я наспех надел порты, натянул косоворотку и побежал к умывальнику."

    scene Ymivalnik
    play sound washing
    e "Ополоснув лицо и прополоскав рот, я побежал к выходу, где меня ждала Саша."

    scene Gorodskaya izba vhod
    with dissolve
    play music birds

    show Sasha
    with moveinleft
    s "Идём быстрее!"
    hide Sasha 
    with moveoutright
    
    scene Ylica goroda
    with flashbulb
    e "Мы направились в сторону академии. Это было лучшее учебное заведение во всём княжестве. В академии обучали грамоте, рассказывали о местных растениях и зверях, показывали, как готовить отвары из различных трав. "
    e "Юношей учили работе с различными инструментами и военному делу а девушек – шитью и прочим вещам, необходимым в быту. Простыми словами – академия готовила русичей ко взрослой жизни."
    e "К счастью, академия находилась не так уж и далеко, так что добрались мы вовремя. Сегодня у нас проходила лекция по травничеству."
    e "…"

    scene Lesnaya tropa 2
    e "После занятий я, как обычно направился на тренировку. Наш зал находился в лесу. Местные мужики сами из того, что попадалось под руку, смогли создать место, где можно было бы из обычного чахлика превратиться в настоящего богатыря."
    e "Заведовал всем дед Митрофан. Крепкий мужик лет пятидесяти с хвостиком. Дед Митрофан ещё в молодости подковы гнул, а сейчас он известен как самый сильный мужик в городе. "
    e "Раньше он был купцом, но дело своё оставил сыну и решил посвятить оставшуюся часть жизни приобщению молодых к здоровому образу жизни."

    scene Slavyanskaya kachalka
    with slow_dissolve
    play music gym volume 0.4

    show Ded Mitrofan Speaking
    with moveinbottom
    d "Ну здорово, юнец!"
    hide Ded Mitrofan Speaking
    show Ded Mitrofan
    i "И здоровее видали! Как ты, дед Митрофан?"
    hide Ded Mitrofan
    show Ded Mitrofan Speaking
    d "Как видишь, живее всех живых."
    hide Ded Mitrofan Speaking
    show Ded Mitrofan
    i "Смотрю, с каждым днём народу к тебе ходит всё больше и больше."
    hide Ded Mitrofan
    show Ded Mitrofan Speaking
    d "А тебе камней жалко?"
    hide Ded Mitrofan Speaking
    show Ded Mitrofan
    i "Чего их жалеть, камни эти? Но, думаю, площадку скоро придётся расширять."
    hide Ded Mitrofan
    show Ded Mitrofan Speaking
    d "Ничего, расширим, всем места хватит! Подсобишь, если понадобится?"
    hide Ded Mitrofan Speaking
    show Ded Mitrofan
    i "С радостью! Ну ладно, давай к делу. Что ты приготовил на сегодня?"
    hide Ded Mitrofan
    show Ded Mitrofan Speaking
    d "Сегодня я для тебя подготовил такую штуку."
    hide Ded Mitrofan Speaking
    with moveoutright
    scene Kamen podnyal Kamen
    e "Дед Митрофан взял булыжник, а затем подбросил его вверх ракеткой."
    show Ded Mitrofan Speaking at left
    with moveinleft
    d "Будем друг другу булыжник кидать, кто пропустит удар, тот проиграл. Попробуешь?"
    hide Ded Mitrofan Speaking
    show Ded Mitrofan at left
    i "Попробую."
    hide Ded Mitrofan Speaking
    show Ded Mitrofan at left
    e "Это далеко не самый большой булыжник деда Митрофана, но лёгким его не назовёшь. Пуда четыре в нём точно будет."
    e "Я закинул булыжник на ракетку и игра началась:"
    call play_pong() from _call_play_pong
    # Игра поднятие булыжника
    
    scene Lesnaya tropa 2

    with slow_dissolve

    play music birds

    e "Тренировка пролетела незаметно. Я попрощался с Дедом Митрофаном и поплёлся домой."
    e "Я шёл по лесной тропе, как вдруг…"
    e "Из ниоткуда появился смуглый мужик в чудной одежде и диковинном головном уборе."
    show Myzhik Speaking
    with moveinbottom
    m "Слушай, друг милый, не хочешь заработать денег?"
    hide Myzhik Speaking
    show Myzhik
    i "И что нужно от меня?"
    hide Myzhik
    show Myzhik Speaking
    m "Да ничего особенного. Ты просто сыграешь с Лешим в игру. Выиграешь – он тебе втройне воздаст, проиграешь – ну, извиняй."
    hide Myzhik Speaking
    show Myzhik
    i "Какой ещё Леший? "
    hide Myzhik
    show Myzhik Speaking
    e "На вид деловой мужик, а чушь несёт, будто у него белая горячка."
    e "Мужик загадочно улыбнулся."
    hide Myzhik
    show Myzhik Speaking
    m "Самый настоящий Леший! В лесу который обитает. Только он не злой совсем, как о нём детям рассказывают."
    hide Myzhik Speaking
    show Myzhik
    i "И с чего мне тебе верить?"
    hide Myzhik
    show Myzhik Speaking
    m "Не хочешь – не верь. Я тебе сказал, а ты решай: идти или не идти."
    hide Myzhik Speaking
    show Myzhik
    e "Выглядит этот мужик весьма необычно для наших мест – я многих в городе знаю, а его вижу впервые. Хотя кажется он вполне приличным человеком. С одной стороны, меня мучает чувство опасности, с другой – от любопытства тоже никуда не денешься."
    e "Так что же мне делать?"
    menu:
        "Идти":
            show Myzhik
            with moveinbottom
            i "Ладно, заинтересовал ты меня. Пойду, посмотрю, что там за Леший у вас водится."
            hide Myzhik
            show Myzhik Speaking
            m "Тогда ступай за мной!"
            hide Myzhik Speaking
            with moveoutright
            scene Lesnaya tropa 3
            e "Он повёл меня по тропинке, которую я раньше в этом лесу не встречал. Я часто хожу по этому лесу, а потому для меня было удивительно, что здесь есть места, о которых я не знаю."
            scene Polyana
            e "Вскоре мы вышли на поляну. Посреди поляны рос могучий многовековой дуб, обвешенный огромной цепью, по которой неспешно прогуливался тощий облезлый чёрный кот. "
            scene Dyb
            play music oak
            e "Под дубом сидело существо размером с двух дедов Митрофанов: кожа была белая, как береста, на груди были выцарапаны какие-то подобия портретов. Телосложением существо было крепкое. "
            e "На бледном лице красовался огромный нос и два жёлтых глаза. Это лицо, изображавшее безумную улыбку, тут же направило взгляд в нашу сторону."
            show Leshiy Speaking
            with moveinbottom
            l "Смотрите-ка! У нас новый гость! Друг милый, подходи, давай сыграем!"
            scene Polyana
            e "По коже пробежал мороз, но бежать уже было поздно. Раньше я думал, что подобная нечисть – лишь выдумки, созданные для того, чтобы дети осторожнее были. Мы с мужиком подошли к дубу."
            scene Dyb
            with dissolve
            show Myzhik Speaking at left
            with moveinleft
            show Leshiy at right
            with moveinright
            m "Леший, развлеки молодца, как умеешь."
            hide Myzhik Speaking
            show Myzhik at left
            hide Leshiy
            show Leshiy Speaking at right
            l "Не переживай, Прохор, развлеку я гостя, как надо!"
            hide Myzhik
            with moveoutleft
            l "Как тебя звать, друг милый?"
            hide Leshiy Speaking
            show Leshiy at right
            i "Ильёй меня звать."
            hide Leshiy
            show Leshiy Speaking at right
            l "Ильёй? Чудесное имя! Ну что же, на что сыграем?"
            hide Leshiy Speaking
            show Leshiy at right
            i "Ты правила сначала объясни, а потом играть будем."
            scene Kryzhka kosti
            with dissolve
            show Leshiy Speaking at right
            with moveinright
            l "Ай да малый! Ну слушай: вот кружка, в ней лежит две кости, у каждой кости шесть граней, у каждой грани по четыре равные стороны. "
            l "На каждой грани выделаны углубления: от одного до шести. Общее число соответствует общему числу углублений на гранях, которые будут смотреть кверху."
            l "Если пополам общее число делится нацело – твоя победа, нет – моя. Ставить можно всё, что захочешь: хоть кошку, хоть себя. Выиграешь – воздам втройне. А проиграешь – не обижайся."
            hide Leshiy Speaking
            show Leshiy at right
            i "Давай попробуем."
            hide Leshiy
            show Leshiy Speaking at right
            l "Ставка – один червонец."
            hide Leshiy Speaking
            show Leshiy at right
            i "Идёт."
            show c8:
                xalign 0.75
                yalign 1.3
                
 
            hide Leshiy
            show Leshiy Speaking at right
            l "Поздравляю!"
            hide c8
            l "Следующая ставка – ты сам. Выиграешь – я тебе подарю верного слугу. Проиграешь – пеняй на себя."
            menu:
                "Соглашаться":
                    i "Я согласен."
                    $ player_roll = r()
                    if (player_roll == 1):
                        show c5:
                            xalign 0.75
                            yalign 1.3
                    if (player_roll == 2):
                        show c9:
                            xalign 0.75
                            yalign 1.3
                    if (player_roll == 3):
                        show c8:
                            xalign 0.75
                            yalign 1.3
                    if (player_roll == 4):
                        show c12:
                            xalign 0.75
                            yalign 1.3
                    if (player_roll < 3):
                        show Leshiy Speaking at right
                        l "Мои соболезнования!"
                        scene Dark
                        with vpunch
                        $ renpy.vibrate(0.5)
                        e "Вдруг я потерял сознание."
                        window hide
                        pause
                        scene Konec1
                        with flashbulb
                        e "Я очнулся в каком-то тёмном туннеле. Вдруг в глаза мне ударил ослепительно яркий свет."
                        e "Что-то в конце ужасно манило меня."
                        e "Я пошёл на свет, и..."
                        return
                    l "Ну что же! Поздравляю, жди завтра подарочек от меня, а пока всё: ступай домой, выспись отдохни."
                    l "Прохор, проводи молодца!"
                    scene Dyb
                    with dissolve
                    show Myzhik Speaking at left
                    with moveinleft
                    p "Хорошо!"
                    hide Leshiy
                    with moveinright
                    hide Myzhik Speaking
                    with moveoutleft
                    scene Lesnaya tropa 2
                    with dissolve
                    show Portal at right
                    with flashbulb
                    show Myzhik at left
                    with moveinleft
                    e "Прохор вывел меня к тому месту, где мы с ним встретились, поклонился, и, как только я моргнул, таинственным образом исчез."
                    show Myzhik at right
                    with moveinleft
                    
                    hide Myzhik 
                    with flashbulb 
                    hide Portal
                    with flashbulb
                    
                    scene Lesnaya tropa 2
                    e "Да уж, сегодня я много всего повидал. Кому скажу – не поверят. Леший, кажется чувствовал моё существо лучше меня: как только скрылся Прохор, я почувствовал, что меня ужасно клонит в сон."
                "Не соглашаться":
                    hide Leshiy speaking
                    show Leshiy at right
                    i "Я не согласен."
                    hide Leshiy
                    show Leshiy Speaking at right
                    l "Что же! Ступай домой, выспись отдохни. До новых встреч!"
                    l "Прохор, проводи молодца!"
                    hide Leshiy speaking
                    show Leshiy at right
                    show Myzhik Speaking at left
                    with moveinleft
                    p "Хорошо!"
                    hide Myzhik Speaking
                    with moveoutleft
                    scene Lesnaya tropa 2
                    with dissolve
                    play music birds
                    
                    show Portal at right
                    with flashbulb
                    show Myzhik at left
                    with moveinleft
                    e "Прохор вывел меня к тому месту, где мы с ним встретились, поклонился, и, как только я моргнул, таинственным образом исчез."
                    show Myzhik at right 
                    with moveinleft 
                    
                    hide Myzhik 
                    with flashbulb 
                    hide Portal
                    with flashbulb
                    
                    
                    
                    scene Lesnaya tropa 2
                    e "Да уж, сегодня я много всего повидал. Кому скажу – не поверят. Леший, кажется чувствовал моё существо лучше меня: как только скрылся Прохор, я почувствовал, что меня ужасно клонит в сон."

        "Не идти":
            e "В друг на меня накатила какая-то ужасная усталость. Я понял, что перетренировался сегодня и надо срочно возвращаться домой."
    scene Gorodskaya izba vnytri
    play sound door
    stop music
    e "Кое-как я выбрался из леса, еле-еле добрался до избы и сразу свалился на нары. Почти мгновенно меня окутал сон."

