from config import w, m1, m2, prime_hub, BACK_Degree, BACKDI_Degree, FRONT_Degree, BACK_UP, BACK_DOWN, FRONT_DOWN, FRONT_UP, PIVOT_LEFT, PIVOT_RIGHT, Huskylens, Block, ALGORITHM_COLOR_RECOGNITION, getMosaicData

def start():
    w.run(
        [ w.ms(500), w.moveTank(-50, -50) ],
        [ w.ms(20),w.brake()],
        w.resetEncoder(),
        w.resetImu(),
        w.resetEncoder(),
    )
    w.runConcurrent(
        []# set zero
    )
    w.runConcurrent(
        []# set zero
    )
    w.run(
        [ w.degree(100), w.straight(50) ],
        [ w.degree(200), w.straight(75) ],
        [ w.degree(450), w.straight(100) ],
        [ w.degree(500), w.straight(75) ],
        [ w.degree(650), w.straight(50) ],
   )
    #HALF
    w.run(
        [ w.blackReflection(20), w.straight(75) ],
        [ w.all(w.blackReflection(20), w.ms(100)), w.straight(75) ],
        [ w.ms(20),w.brake() ],
        w.resetEncoder(),	
    )

    #KEEP 2
    w.run(
        [ w.heading(45), w.turn() ],
        [ w.ms(20), w.brake() ],
        w.resetEncoder(),
        [ m1.degree(BACK_Degree),m1.move(BACK_DOWN * 75) ],m1.hold(),
        m1.resetEncoder(),
    )

    #RETURN TO LINE
    w.run(
        [ w.blackReflection(20), w.straight(50) ],
        w.resetEncoder(),
        [ w.heading(0), w.turn() ],
        [ w.ms(20), w.brake() ],
        w.resetEncoder(),
    )

    w.run(
        [ w.degree(100), w.straight(50) ],	
        [ w.degree(600), w.straight(100) ],
        [ w.degree(700), w.straight(75) ],
        [ w.degree(850), w.straight(50) ],
        [ w.heading(-90), w.turn() ],
        [ w.ms(20),w.brake() ],
        w.resetEncoder(),
    )
    
    w.runConcurrent(
        [ w.degree(200) ],
        [ m1.degree(BACK_Degree),m1.move(BACK_UP * 75) ],m1.hold(),
        m1.resetEncoder(),
    )

    w.run(
        [ w.degree(100), w.straight(50) ],
        [ w.degree(600), w.straight(75) ],
    )    

    w.run(
        [ w.blackReflection(20),w.straight(75) ],
        [ w.degree(900), w.straight(75) ],
        [ w.degree(1000), w.straight(50) ],
        [ w.ms(20),w.brake() ],
        w.resetEncoder(),
    )

    w.run(
        [ w.heading(-180), w.turn() ],
        [ w.ms(20), w.brake() ],
        w.resetEncoder(),
        [ w.degree(100), w.straight(-50) ],
        [ w.degree(250), w.straight(-75) ],
        [ w.degree(350), w.straight(-50) ],
        [ w.ms(20),w.brake() ],
        w.resetEncoder(),
        #KEEP YELLOW
        [ m1.degree(BACK_Degree),m1.move(BACK_DOWN * 75) ],m1.hold(),
        m1.resetEncoder(),
        [ w.heading(-160),w.turn() ],
        [ w.heading(-200),w.turn() ],
        [ w.heading(-180),w.turn() ],
        [ w.degree(200), w.straight(50) ],
        [ w.heading(90), w.turn() ],
    )

    w.run(
        [ w.blackReflection(20), w.straight(75) ],
        [ w.all(w.blackReflection(20), w.ms(100)), w.straight(75) ],
        [ w.ms(20), w.brake() ],
        [ m1.degree(BACK_Degree),m1.move(BACK_UP * 75) ],m1.hold(),
        m1.resetEncoder(),
    )
    w.run(
        [ w.heading(-180), w.turn() ],
        [ w.degree(200), w.straight(-50) ],
        [w.ms(20),w.brake()],
        w.resetEncoder(),
        [ m1.degree(BACKDI_Degree),m1.move(BACK_UP * 75) ],m1.hold(),
        [ w.degree(90), w.straight(-50) ],
        [ m1.degree(BACK_Degree - BACKDI_Degree),m1.move(BACK_DOWN * 50) ],m1.hold(),
    )
    #RETURN TO KEEP YELLOW
    w.run(
        [ w.degree(290), w.straight(50) ],
        [ w.heading(90), w.turn() ],
        [ m1.degree(BACK_Degree - (BACKDI_Degree - BACK_Degree)),m1.move(BACK_DOWN * 75) ],m1.hold(),
    )
    #KEEP 3
    w.run(
        [ w.blackReflection(20), w.straight(75) ],
        [ w.heading(-180), w.turn(PIVOT_LEFT) ],
        [ w.ms(20), w.brake() ],
        w.resetEncoder(),
        [ w.degree(100), w.straight(50) ],
        [ w.degree(350), w.straight(100) ],
        [ w.degree(400), w.straight(75) ],
        [ w.degree(500), w.straight(50) ],
        [ w.ms(20),w.brake() ],
        w.resetEncoder(),
    )

    w.run(
        [ w.degree(300), w.moveTank(70, 35) ],
        [w.blackReflection(20), w.straight(75)],
        [ w.ms(20),w.brake() ],
        [ w.degree(100), w.straight(-50) ],
        [ w.ms(20),w.brake() ],
        [ w.heading(-90), w.turn() ],
        [ w.ms(20),w.brake() ],
        w.resetEncoder(),
    )

    w.run(
        [ w.blackReflection(20), w.straight(75) ],
        [ w.ms(20),w.brake() ],
        [w.heading(90), w.turn()], 
        [ w.ms(20),w.brake() ],
        w.resetEncoder(),
    )

    w.run(
        [ w.degree(100), w.straight(-50) ],
        [ w.degree(200), w.straight(-75) ],
        [ w.degree(300), w.straight(-50) ],
        [ w.ms(20),w.brake() ],
        [ m1.degree(BACK_Degree),m1.move(BACK_UP * 75) ],m1.hold(),
    )
    #-------------------CHECKING MOSAIC-------------- don't do



def main():
    start()
main()