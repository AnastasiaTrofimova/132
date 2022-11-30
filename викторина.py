def f ():
    voprosi = ['Как с французкого языка перевдится quatre?','Как на француском сказать полиция?','Как переводится с французкого языка Je n’ai fait rien de mal?','Как переводится "красный" на французкий язык?','Как на французком сказать "четверг"?']
    otveti = ['Четыре', 'police','Я не сделал ничего плохого','rouge','jeudi']
    z=v=0
    for i in range (len(voprosi)):
        print (voprosi[i])
        answer1 =input()
        if answer1 == otveti[i]:
            print('Правильный ответ')
            z=z+1
        else:
            print('Неверный ответ')
            v+=1
        print(f'Верных - {z}, Неверных-{v}')
d=1
while d==1:
       f()
       d=int(input('НАЧАТЬ ЗАНОВО (нажать 1, если хотите)'))
    
    
