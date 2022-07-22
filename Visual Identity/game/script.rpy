define n = Character("Niko", color="#ff8e2b")
define a = Character("Asaba", color="#481780")
define h = Character("Hada Sensei", color="#ad0505")
define m = Character("Megumi", color="#cf199e")
define Hausis = ""
define Treppe = False
define Dach = False
define Klassenzimmer = False

label start:
    scene bg treppe
    default p = "Spieler"
    $ p = renpy.input("Wie heißt du?")
    play music "audio/bgm emotional piano.mp3" fadein 1.0 volume 0.25
    scene bg schulweg

label scene1_1:
    n "Hey [p], warte!"
    p "Immer das gleiche mit Niko..."
    show niko delighted
    n "Da bin ich!"
    n "Nur fünf Minuten zu spät."
    p "Das nächste mal mach ich nicht so langsam."
    show niko annoyed
    n "Nicht fair!"
    "Niko und ich kennen und jetzt seit der dritten Klasse."
    "Sie ist damals neu dazugezogen in unsere Nachbarschaft."
    "Meine Mutter meinte ich soll mich mit ihr anfreunden"
    "und jetzt sind wir hier. Auf dem Weg zur Schule..."

label scene1_2:
    scene bg eingang
    show niko delighted 
    n "Hast du schon davon gehört?"
    p "Von was?"
    n "Es werden wieder ziemlich viele neue Schüler zu uns an die Schule wechseln!"
    p "Echt?"
    n "Jap!"

# Entscheidung 1: Neue verarschen
menu: 
    "Lust die Neuen zu verarschen?":
        jump choice1_1
    "Die sehen verloren aus... wollen wir schnell helfen?":
        jump choice1_2


label choice1_1:
    show niko annoyed
    n "Hey, sei nicht so fies!"
    jump scene2

label choice1_2:
    show niko laugh 
    n "Auf jeden Fall!"
    jump scene2

    
label scene2: 
    scene bg gang rechts    
    show niko normal 
    n "Ähm.."
    p"Was ist jetzt?"
    show niko laugh
    n "Was machst du heute in der Mittagspause?"
    p "Essen, warum?"
    n "Eventuell..."
    p "Was?"
    show niko sad
    n "... ich hab vielleicht mein Mittagessen vergessen..."
    p "Aha und jetzt?"
    show niko smile
    n "Naja..."
    n "Kann ich was von dir abhaben später?"
    
# Entscheidung 2: Essen vergessen
menu:
    "Ja klar! Magst du Sandwiches?":
        jump choice2_1
    "Ähm... ich kann dir sonst auch Geld leihen falls du dir was in der Cafeteria zu Essen kaufen möchtest":
        jump choice2_2
    "Ist mir doch egal. Denk doch selber dran.":
        jump choice2_3

label choice2_1:
    show niko laugh
    n "Und wie!"
    jump scene3
label choice2_2:
    show niko annoyed
    n "Alles gut passt schon, ich frag mal eine Freundin..."
    jump scene3
label choice2_3:
    show niko angry
    n "Hey!"
    jump scene3

label scene3:
    show niko normal
    n "Hast du später auch Mathe beim Müller?"
    p "Jap."
    n "Weißt du was?"
    p "Hm?"
    n "Es geht mega das Gerücht rum in der Parallelklasse..."
    show niko annoyed
    n "Der Lehrer ist mega streng und macht super gerne Überraschungsteste!"
    p "Echt jetzt?"
    n "Jap. Megumi ist sogar mal durchgefallen!"
    p "Megumi?"
    p "Die Streberin aus der Parallelklasse?"
    n "Ja... och man ich mach mir total Sorgen..."
    show niko normal 
    n "Immerhin haben wir jetzt erst Deutsch."
    show niko laugh
    n "Bis später!"

label scene4:
    scene bg klassenzimmer
    play music "audio/bgm background.mp3" fadein 1.0 volume 0.15
    h "So heute besprechen wir die Hausaufgaben von letzter Woche."
    h "Wer möchte vorlesen?"
    "..."
    "Niemand meldet sich..."
    h "Ich weiß es ist morgens, aber einer muss den Anfang machen!"
    "..."
    "Kein Wunder so früh wie es ist..."
    show hada delighted
    h "[p]!"

# Entscheidung 3: Falsche Hausis vorlesen
menu: 
    "Lese die Hausaufgabe von vor zwei Wochen vor":
        jump scene5
    "Entschuldigung...":
        $ Hausis = "Entschuldigt"
        jump choice4_1


label scene5:
    p "Früh um 8 Uhr: In Deutschland klingeln landauf landab die Schulglocken und zwingen unausgeschlafene
Jugendliche, sich auf Mathematik oder Englisch, auf Geografie oder Grammatik zu konzentrieren..."
    show hada annoyed
    p "...Mein Fazit steht fest: Ich bin entschieden für einen späteren Schulbeginn, denn ich merke selbst, wie
schwer es mir fällt, am frühen Morgen dem Unterricht zu folgen."
    h "Du hast Recht, das Frühaufstehen steht dir nicht."
    h "Das war die falsche Aufgabe, [p]."
    h "Die Erörterung war vor zwei Wochen fällig. Die Aufgabe auf heute war eine Gedichtsanalyse."
    show hada angry1
    h "Denkst du ich hätte das nicht bemerkt?"
    show hada angry2
    h "Für wie dumm hältst du mich eigentlich?"
    h "Zeig mir die Hausaufgabe oder es gibt Nachsitzen!"

#Entscheidung 4: Schule ist scheiße
menu:
    "Entschuldigen Sie":
        $ Hausis = "Entschuldigt"
        jump choice4_1

    "Warum sollte ich?":
        jump choice4_2
    
label choice4_1:
    p "Entschuldigung, ich habe die Hausaufgabe zuhause vergessen..."
    show hada annoyed
    h "Das gibt einen Strich."
    h "Ich will deine Gedichtsanalyse morgen sehen."
    show hada normal
    h "Wer liest jetzt vor?"
    h "Diesmal aber bitte die richtige Hausaufgabe."
    jump scene6_2

label choice4_2:
    show hada angry1
    p "Ja ist doch wahr!"
    p "Wofür sollte ich so früh aufstehen nur um im Unterricht fast einzuschlafen?"
    p "Kein Mensch braucht verdammte Gedichtsanalysen!"
    show hada angry2
    h "Das wars! Nachsitzen!"
    h "Geh in der Pause zum Sekretariat."

label scene6_1:
    scene bg treppe
    p "Nachsitzen..."
    p "Das ist so ein Dreck!"
label scene6_2:
    scene bg treppe
    "Endlich Pause!"
    "Das nächste Fach ist Mathe."
    "Ich laufe mal zum nächsten Klassenzimmer..."
    scene bg klassenzimmer2
    "Auf dem Lehrerpult liegt ein Stapel Papiere..."
    p "Ich schaue mir das mal genauer an."
    p "Oh... ein Mathe-Test."
    p "Hm... zwei Mathe-Tests. "

# Entscheidung 5: Test fotografieren
menu:  
    "Mach ein Foto von den Tests":
        $ test = "Foto"
        jump scene7
    "Schreibe dir die Testfragen auf":
        $ test = "Aufgeschrieben"
        jump scene7
    "Lege die Tests wieder zurück":
        $ test = "Zurück"
        jump scene7

label scene7:
    "Verdammt, ich höre Schritte..."
    "Ich sollte schnell hier raus und in die Pause."
    scene bg gang rechts
    play music "audio/bgm angry.mp3" fadein 1.0 volume 0.25
    show asaba smirk
    a "Hey schaut euch mal [p] an!"
    a "[p] hat sich gerade in Deutsch übel blamiert!"
    a "Hahahaha!"
    a "Wie kann man denn so rumlaufen?"
    p "Wir tragen alle die gleiche Uniform du Idiot."
    show asaba angry
    a "Ich sehe trotzdem besser aus!"
    p "Ein Spiegel würde dir auch mal gut tun."
    show asaba angry2
    a "Pass auf was du sagst!"
    show asaba angry

# Entscheidung 6: In die Eier
menu:
    "Lass mich in Ruhe...":
        jump choice6_1
    "Halt die Fresse!":
        jump choice6_2
    "Das nächste Mal bin ich nicht so nett.":
        jump choice6_3

label choice6_1:
    p "Lass mich in Ruhe."
    show asaba smirk
    a "Hmpf."
    a "Dir ist nicht mehr zu helfen."
    p "Was hast du gesagt?"
    a "Tja so ein Loser wie du kommt niemals an mich heran."
    jump scene8

label choice6_2:
    p "Halt die Fresse!"
    show asaba surprised
    a "Was hast du zu mir..."
    "Jetzt reichts mir ich trete ihm in die Eier!"
    show asaba angry2
    p "Das nächste Mal bin ich nicht so nett!"
    a "Du Arsch das tut weh!"
    a "Du kannst mich mal!"
    jump scene8

label choice6_3:
    p "Das nächste mal bin ich nicht so nett."
    show asaba smirk
    a "Jaja, sicher."
    a "Was willst du denn machen?"
    a "Mich schlagen?"
    "Am besten da hin wo´s wehtut!"
    jump scene8

label scene8:
    if test == "Foto":
        p "Ich habe hier etwas das dich interessieren könnte..."
        show asaba angry
        a "Ich interessiere mich für nichts was aus deinem Mund kommt."
        p "Sicher?"
        p "Noch nicht einmal den Mathe-Test den wir nach der Pause schreiben?"
        show asaba surprised
        a "Den was?!"
        p "Mathe-Test."
        p "Hier auf meinem Handy sind alle Fragen."
        show asaba angry
        a "Her damit!"
        p "Nicht hier."
        scene bg dach1
        show asaba normal
        a "Also jetzt sind wir alleine."
        a "Gib mir den Test."
        p "Hm was bekomme ich dann dafür?"
        show asaba angry
        a "Was willst du?"
        a "Du weißt ich darf den Test nicht durchfallen!"
    else:
        jump scene10 # ohne Test 

# Entscheidung 7: Bezahlung für Test
menu:
    "Eine Entschuldigung":
        jump choice7_1
    "Dein Taschengeld für den Monat":
        jump choice7_2
    "Knie dich hin und flehe mich an":
        jump choice7_3

label choice7_1:
    a "Ja okay."
    a "´Tschuldige."
    p "Also lass mich jetzt in Ruhe."
    a "Krieg ich jetzt den Test?"
    jump scene9

label choice7_2:
    show asaba angry2
    a "Den Monat?!"
    p "Willst du den Test oder nicht?"
    show asaba angry
    a "Von mir aus."
    a "Kannst mich mal."
    p "Schön mit dir Geschäfte zu machen."
    a "Gleichfalls du Arsch..."
    jump scene9

label choice7_3:
    show asaba smile2
    a "Hab ich das gerade richtig gehört?"
    p "Ja."
    p "Flehe mich an und du bekommst den Test."
    show asaba angry2
    a "Was ist mit dir los?"
    p "Ich habe Spaß dich leiden zu sehen."
    a "..."
    show asaba angry
    a "Bekomme ich BITTE den Test?"
    p "Auf die Knie."
    show asaba surprised
    a "Das ist doch jetzt nicht dein Ernst?"
    p "Doch. Also los."
    scene bg dach1
    a "..."
    a "Bekomme ich jetzt den Test?"
    p "Flehe richtig."
    a "[p], bekomme ich bitte den Mathe-Test."
    jump scene9

label scene9:
    show asaba angry
    p "Soll ich´s dir dann per Chat schicken?"
    show asaba smirk
    a "Was sonst, per Mail du Idiot?"

# Entscheidung 8: Welcher Test?
menu:
    "Schicke ihm den richigen Mathe-Test":
        jump choice8_1
    "Schicke ihm den falschen Mathe-Test":
        $ foto = "falsch"
        jump choice8_1
    "Schicke ihm nichts.":
        jump choice8_2

label choice8_1:
    p "Ich habs dir geschickt."
    show asaba angry
    a "Danke."
    jump scene10

label choice8_2:
    p "Du solltest dankbar sein."
    show asaba angry2
    a "Für was denn?"
    p "Den Test."
    a "..."
    p "Chance verpasst."
    show asaba angry
    a "Schickst du mir den Test noch?"
    p "Nö."
    show asaba angry2
    a "Hey! Was soll das?"
    p "Wenn du die ganze Lust darauf hast ein Arsch zu sein kann ich auch einer sein."
    a "Fick dich!"
    jump scene10

label scene10:
    scene bg toilette
    play music "audio/bgm chill.wav" fadein 1.0 volume 0.25
    p "Ich brauch ne Pause vor den nervigen Leuten..."
    show hada annoyed
    h "[p]!"
    h "Es ist Pause, geh raus."
    p "Darf ich nicht auf Toilette?"
    h "Die gibt es auch unten."
    p "Muss das sein?"
    if Hausis == "Entschuldigt":
        h "Ja. Also hop, hop."
        jump scene11
    else: 
        h "Willst du noch eine Stunde länger nachsitzen?"
        p "Nein"
        h "Also hop, hop."
    

label scene11:
    scene bg gang links
    "Ich habe keine Lust raus zu den Anderen zu gehen..."
    "Warum liegt hier einfachso ein Rucksack rum?"

label scene12:
    show meg sleepy
    m "Hi!"
    m "[p], stimmts?"
    p "Kennst du mich?"
    show meg smile2
    m "Ich bin in der Parallelklasse."
    m "Ich bin Megumi."
    "Ah die Streberin."
    p "Hi?"
    m "Du hast nicht zufälligerweise mein Epipen gesehen oder?"
    p "Denke nicht."
    p "Wie sieht der denn aus?"
    m "Naja, das ist so ein großer Stift eigentlich..."
    m "Der hat so ein gelbes Etikett und eine blaue und eine orangene Seite."
    p "Denke nicht, dass ich den gesehen habe."
    m "Meine Eltern bringen mich um..."
    m "Das Ding ist super teuer!"
    "Klingt interessant..."
    p "Ja dann kann ich dir gerne suchen helfen."
    "Ich mach alles um nicht raus gehen zu müssen!"
    m "Wirklich?"
    m "Danke!"

label Suchen:
    scene bg gang links
    "Wo soll ich hin?"

menu:    
    "Dach" if Dach == False:
        $ Dach = True
        jump scene13

    "Klassenzimmer" if Klassenzimmer == False:
        $ Klassenzimmer = True
        jump scene14

    "Treppenhaus"  if Dach == True and Klassenzimmer == True:
        $ Treppe = True
        jump scene15


label scene13:
    scene bg dach2
    "Wow was für eine schöne Aussicht."
    "Auch wenn ich hier manchmal chille, hab ich da nie drauf geachtet."
    "Aber scheint als wäre der Stift nicht hier."
    "Zurück ins Gebäude."
    jump Suchen

label scene14:
    scene bg klassenzimmer
    "Hab ich mir schon gedacht..."
    "Die Teste sind weg."
    "Interessant was manche Leute für komisches Zeug in ihren Taschen haben."
    "Hinter dem Lehrerpult ist auch nichts."
    jump Suchen

label scene15:
    scene bg treppe
    "Hier war ich vorher schon."
    "Hoffentlich kommt jetzt niemand..."
    show hada annoyed
    h "Hab ich nicht gerade gesagt du sollst runter in die Pause?"
    p "Ja, aber..."
    h "Kein aber."
    p "Ich helfe Megumi etwas zu suchen."
    show hada delighted
    h "Ach wirklich?"
    h "Seit wann bist du denn mit Megumi befreundet?"
    h "Ihr seid doch in ganz anderen Klassen."
    p "Seit zwei Minuten."
    p "Sie meinte der Stift wäre ihr wichtig."
    show hada annoyed
    h "Ein Stift?"
    h "Eine dümmere Ausrede hatte ich noch nie."
    h "Ich begleite dich diesmal raus."

label scene16:
    scene bg eingang
    show hada angry2
    h "Und jetzt mach deine Pause!"
    show hada annoyed
    h "Oder das was davon übrig ist..."
    hide hada annoyed
    "So nervig!"
    "Diese Frau lässt mich auch nicht in Ruhe!"
    "Warum ist es Pflicht in der Pause raus zu gehen?"
    "Das ist total unnötig."
    "Oh was ist das da?"
    "Ist das dieser Stift der so teuer sein soll?"
    "Sieht komisch aus..."
    play music "audio/bgm drama.mp3" fadein 1.0 volume 0.25
    show niko shocked
    n "Hey [p]!"
    n "Hast du Megumis Epipen gesehen?"

# Entscheidung 9: Stift einstecken?

menu:
    "Stecke den Stift ein":
        jump scene17_1

    "Gib Niko den Stift":
        jump scene17_2

label scene17_1:
        p "Warum die Eile?"
        n "Hast du oder hast du nicht?"
        p "Nein."
        show niko annoyed
        p "Warum?"
        n "Megumi wurde von einer Biene gestochen!"
        p "Hä?"
        n "Sie ist allergisch gegen Bienen!"
        p "Und was hat das mit dem Stift zu tun?"
        n "Der Epipen?"
        show niko angry
        n "Der kann sie vor dem Sterben retten!"
        p "Der Stift?"
        n "Das ist ein Epipen!"
        show niko annoyed
        n "Und ja, eigentlich hat sie den immer dabei falls was passiert!"
        n "Ich hab gehört der Krankenwagen ist schon unterwegs."
        n "Aber bis man sie gefunden hat, ist schon ihr ganzer Hals angeschwollen!"
        "Deswegen ist der Stift also so wertvoll?"
        "Sie hat eine tödliche Allergie gegen Bienen?"
        "Ich habe schon gesagt, dass ich den Stift nicht habe."
        "Ich müsste zugeben, dass ich gelogen habe..."

# Entscheidung 10: Redemption?
menu:
    "Gib zu gelogen zu haben":
        jump scene18_1
    "Behalte den Stift":
        jump scene18_2

label scene18_1:
    p "Hey Niko?"
    n "Was?"
    p "Vielleicht.. "
    show niko angry
    n "Sag schnell!"
    n "Oder willst du, dass sie stirbt?"
    show niko shocked
    p "Ich habe den Epipen."
    p "Ich hab ihn gerade gefunden als du gekommen bist."
    n "HADA SENSEI!!!"
    n "[p] hat den Epipen gefunden!"
    show niko shocked at left
    show hada delighted at right
    h "[p] danke, jetzt muss ich schnell zu Megumi!"
    hide hada delighted
    hide niko sad
    show niko sad
    n "Warum hast du dann gelogen?"
    p "Weiß nicht..."
    p "Sorry..."
    show niko annoyed
    n "Wir reden später."
    jump scene20

label scene18_2:
    p "Dann... lass und schnell weitersuchen!"
    n "Ich war schon überall!"
    p "Dann schauen wir nochmal."
    show niko shocked
    n "Hörst du das?"
    n "Ich glaub der Krankenwagen kommt!"
    h "Alle Schüler gehen jetzt sofort zurück in ihre Klassenzimmer!"
    h "Keine Ausnahmen!"
    "Ach jetzt soll ich zurück rein?"
    jump scene21

label scene19:
    p "Den was?"
    show niko annoyed
    n "Epipen!"
    n "Megumi wurde von einer Biene gestochen!"
    p "Hä?"
    n "Sie ist allergisch gegen Bienen!"
    p "Und was hat das mit dem Stift zu tun?"
    n "Der Epipen?"
    show niko angry
    n "Der kann sie vor dem Sterben retten!"
    p "Der Stift?"
    n "Das ist ein Epipen!"
    show niko annoyed
    n "Und ja, eigentlich hat sie den immer dabei falls was passiert!"
    n "Ich hab gehört der Krankenwagen ist schon unterwegs."
    n "Aber bis man sie gefunden hat, ist schon ihr ganzer Hals angeschwollen!"
    p "Oh krass!"
    show niko shocked
    p "Ja ich hab ihn gerade hier gefunden."
    n "Ernsthaft?"
    n "Das ist heftiges Timing!"
    n "HADA SENSEI!!!"
    n "[p] hat den Epipen gefunden!"
    show niko shocked at left
    show hada delighted at right
    h "[p] danke, jetzt muss ich schnell zu Megumi!"
    jump scene20

label scene20:
    play music "audio/bgm atmosphere.mp3" fadein 1.0 volume 0.25
    scene bg klassenzimmer
    h "\"Durchsage an alle Schüler:\""
    h "\"Wie alle mitbekommen haben, hatte eine Mitschülerin von euch eine schwere allergische Reaktion.\""
    h "\"Danke an alle, die mitgeholfen haben beim Suchen.\""
    h "\"Ganz besonders möchte ich mich aber bei [p] bedanken.\""
    h "\"Dank seiner großen Zivilcourage wird die Schülerin überleben.\""
    h "\"Ich wünsche noch einen angenehmen Schultag.\""

    return 

label scene21:
    scene bg klassenzimmer
    play music "audio/bgm atmosphere.mp3" fadein 1.0 volume 0.25
    h "\"Durchsage an alle Schüler:\""
    h "\"Wie alle mitbekommen haben, hatte eine Mitschülerin von euch eine schwere allergische Reaktion.\""
    h "\"Danke an alle, die mitgeholfen haben beim Suchen.\""
    h "\"Die Schülerin befindet sich jetzt im Krankenhaus.\""
    h "\"Ob die Schülerin bald wieder zu uns kommt, ist noch nicht gewiss.\""
    h "\"Wer sich belastet fühlt, kann gerne den Schulpsychologen in Anspruch nehmen.\""
    h "\"Ich wünsche noch einen angenehmen Schultag.\""

    return