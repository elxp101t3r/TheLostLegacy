import time
import threading
from playsound import playsound
def bgMusic():
  playsound('bg_m.ogg')
music_thread = threading.Thread(target=bgMusic)
music_thread.start()
print('''
                                 ____                                         
                              .-"    `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____        fsc   
''')
def theStory(text, t_speed=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(t_speed)
    print()

intro = 'In the msytical land of Eldoria, a legend had been passed through generations.\n'
theStory(intro)
intro_1= 'A legend of unimaginable riches hidden within the treacherous Enigma Forest.\n'
theStory(intro_1)
print('''
                                          .__ ._       \_.          
                                     _, _.  '  \/   \.-  /            
                                      \/     .-_`   // |/     \,      
                     .-""""-.          \.   '   \`. ||  \.-'  /       
                    F        Y        .-.`-(   _/\ V/ \\//,-' >-'   ._,
                   F          Y   .__/   `. \.   ' J   ) ./  / __._/  
                  J         \, I    '   _/ \  \  | |  / /  .'-'.-' `._,
           (       L   \_.--.| \_.      ' .___ `\: | / .--'.-'"     \ 
         \ '\    .  L   /    \\/        ._/`-.`  \ .'.' .'---./__   ' 
    \__  '\ ) \._/   `-.__. ` \\_. '   .---.  \     /  /  ,   `  `    
  --'  \\  ): // \,            `-.`__.'     `- \  /   / _/-.---.__.- . 
     _.-`.'/ /'\_, ._     >--.-""'____.--"`_     '   /.'..' \   \   _/`
 _ .---._\ \'/ '__./__.-..  / .-|(    x_.-'___  |   :' /    _..---_' \
 .:' /`\ `. `..'.--'\      /.' /`-`._  `-,'   ` '   I '_.--'__--..___.--._.-
     `  `. `\/'/  _.   _.-'      _.____./ .-.--""-. .-"    ' _..-.---'   \
  -._ .--.\ / /-./     /   .---'-//.___. .-'       \__ .--.  `    `.     '`-
 ,--'/.-. ^.   .-.--.  ` _/    _//     ./   _..   .'  `.    \ \    |_.
    /' | >.   ' | \._.-       '    _..'  `.' . `.       )    | |\  `          
  ./ \ \'  ) c| /  \     \_..  .--'    ,\ \_/`  :    )  (`-. `.|`\\            
   \'  / ,-.  | ` ./`  ._/ `\\'.--.,-((  `.`.__ |   _/   \    |)  `--._/`     
______'\   |  < __________  //'  //  _)   )/-._`.  (,-')  )  / \_.    /\. _____
a:f        |  |        .__./    //  '\  |//    `.\ '\ (  (  <`   ._  '
           >  |      _.  /   ..-\ _    _/ \_.  \ `\    \_ `---.-'__   
        . /  `-   _.'        /   `   _/|       J  /`     `-,,-----.`-.
            '  .:'          '`      '          < `   f  I //        `�\_,
              '                         \.     J        I/\_.        ./
         __/                            `:     I  .:    K  `          `
         \/ )                            `,   J         L             
          )_(_                             .  F  .-'    J             
         /    `.                           .  I  (.   . I _.-.._      
   '    <'    \ )                     _.---.J/      :'   L -'         
 .:.     \. _.->/                        _.-'_.)     ` `-.`---.,_.    
:<        (    \                    .--""   .F' J) `.`L.__`-.___      
.:        |-'\_.|                          Y ..Z     ))   `--'  `-    
.         ) | > :                            . '    :'                
          / ) L_J                            .x,.
          L_J .,                             .:<.,  
        .'`   `                               :J.,` 
                                           . ;.+K,:.
                                               .,L+.,     
''')
intro_2='''It was said that whoever could decipher the ancient riddles and navigate the\ndangers of the forest would discover the Lost Legacy..\nA treasure of immeasurable worth.\n'''
theStory(intro_2)
intro_3='You are a brave adventurer who has heard the tales and accepted the challenge.\n'
print('''
           
                            / : \
                            |===|
                            >._.<
                        .=-<     >-=.
                       /.'`(`-+-')'`.\
                     _/`.__/  :  \__.'\_
                    ( `._/\`. : .'/\_.' )
                     >-(_) \ `:' / (_)-<
                     | |  / \___/ \  | |
                     )^( | .' : `. | )^(
                    |  _\|`-._:_.-'| \  |
                    "-<\)| :  |  : |  "-"
                      (\\| : / \ : |
                        \\-:-| |-:-')
                         \\:_/ \_:_/
                         |\\_| |_:_|
                         (;\\/ \__;)
                         |: \\  | :|
                         \: /\\ \ :/
                         |==| \\|==|
                        /v-'(  \\`-v\
                       // .-'   \\. \\
                       `-'       \\`-'  
                                  \|
 
''')
theStory(intro_3)
intro_4='Equiped with only a map, a latern, and your wits.\n'
theStory(intro_4)
print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/      
''')
intro_5='you venture into the Enigma Forest, shrouded in mystery and danger.\n'
theStory(intro_5)
print('''
          <|
           A             
          /.\       
     <|  [""M#      
      A   | #              
     /.\ [""M#             
    [""M# | #  U"U#U                 
     | #  | #  \ .:/    
     | #  | #___| #     
     | "--'     .-"     
   |"-"-"-"-"-#-#-##    
   |     # ## ######     
    \       .::::'/     
     \      ::::'/      
   :8a|    # # ##      
   ::88a      ###       
  ::::888a  8a ##::.    
  ::::::888a88a[]::::
 :::::::::SUNDOGa8a::::. ..              
 :::::8::::888:Y8888:::::::::...      
::':::88::::888::Y88a______________________________________________________
:: ::::88a::::88a:Y88a                                  __---__-- __
' .: ::Y88a:::::8a:Y88a                            __----_-- -------_-__
  :' ::::8P::::::::::88aa.                   _ _- --  --_ --- __  --- __--
.::  :::::::::::::::::::Y88as88a...s88aa.
''')
main_story = 'As you enter the forest, you face your first choice..\n'
theStory(main_story)
choice = input('1. Follow the winding river deeper into the forest or 2. Venture into the dark cave entrance to your left?1 or 2?\n')
if choice == '1':
    main_story = 'You decide to follow the winding river,\n hoping it will lead you to clues \nabout the treasures location.\n'
    theStory(main_story)
    main_story = 'The path is serene at first...\nBut as you go deeper, the forest becames denser and more ominous.\n'
    theStory(main_story)
    choice = input('1. Continue following the river\nor\n2. Leave the river and cut through the dense underbrush?\n')
elif choice == '2':
    theStory('With a brave heart, you enter the dark cave.\n')
    theStory('The air is damp, and the walls seem to close in around you.\n')
    theStory('Torch in hand, you venture deeper into the caves eerie depths.')
    theStory('What will you do?\n')
    theStory('1. Go further into the cave\n')
    theStory('2. Decide to retreat and return to the forest\n')
    choice = input()
    if choice == '1':
      theStory('You brave the caves darkness and continue deeper.\n')
      theStory('You emerge into a cavern bathed in an eerie blue light\n')
      theStory('In the center of the cavern, you find a chest with mystical symbols.\n')
      theStory('What will you do?\n')
      theStory('1. Approach the chest cautiously\n')
      theStory('2. Leave the cavern and head back to forest\n')
      choice = input()
      if choice == '1':
        theStory('The chest contains the Lost Legacy treasure!\n')
        theStory('Congratulations! You have found the Lost Legacy!\n')
      elif choice == '2':
        theStory('You leave the cavern and return to the forest.\n')
      else:
        theStory('Invalid Choice.')      