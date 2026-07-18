"""
Program's Entry Point for WRO2026 Senior
"""

from pybricks.parameters import Port, Color, Direction
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.hubs import PrimeHub

from huskylens import Huskylens, Block, ALGORITHM_COLOR_RECOGNITION
from drivebase import DriveBaseAPI, MissionMotor, PIVOT_LEFT, PIVOT_RIGHT

prime_hub = PrimeHub()
#husky = Huskylens(Port.E)
m1 = MissionMotor(Motor(Port.C))
m2 = MissionMotor(Motor(Port.D))
w = DriveBaseAPI(
    Motor(Port.A, Direction.COUNTERCLOCKWISE), 
    Motor(Port.B, Direction.CLOCKWISE), 
    ColorSensor(Port.F), 
    hub = prime_hub,
    straight_params = {
        30:  (3.2, 20.0, 0.07), -30:  (3.2, 20.0, 0.07),
        50:  (3.2, 20.0, 0.07), -50:  (3.2, 20.0, 0.07),
        75:  (3.6, 20.2, 0.15), -75:  (3.6, 20.2, 0.15),
        100: (3.8, 20.5, 0.22), -100: (3.8, 20.5, 0.22),
    },
    tagline_params = {
        30:  (0.65, 0.0, 0.065), -30:  (0.65, 0.0, 0.065),
        50:  (0.65, 0.0, 0.065), -50:  (0.65, 0.0, 0.065),
        75:  (0.65, 0.0, 0.065), -75:  (0.65, 0.0, 0.065),
        100: (0.65, 0.0, 0.065), -100: (0.65, 0.0, 0.065),
    },
    turn_params = {
        90:  (3.8 , 7.0 , 0.1),
    },
)

# (0,0)#1, (0,1)#2, (0,2), (0,3)
# (1,0)#5, (1,1)#6, (1,2), (1,3)
# (2,0)#3, (2,1)#4, (2,2), (2,3)
def getMosaicData(tiles: list[Block], ratio_tolerance: int, area_tolerance: int) -> list[list[int]] | None:
    filtered = [tile for tile in tiles if abs(tile.ratio() - ratio_tolerance) <= 1.0 and tile.area() <= area_tolerance]
    if len(filtered) < 12: return None
    sort_by_row = sorted(filtered, key = lambda tile: tile.y)
    return [[v.id for v in sorted(sort_by_row[i:i+4], key = lambda tile: tile.x)] for i in range(0, 12, 4)]
#SET M1 + back_move ; - front down
#SET M2 + KEEP
M1_DOWN = 400

def FirstMission():
    # w.runConcurrent(
    #     [w.ms(50),m1.move(75)],	#set 0
    #     m1.brake()
    # )

    w.runConcurrent(
        [w.ms(50)],
        [w.ms(100),m2.move(75)],
        m2.brake()	#set 0
        
    )
    w.run(
        [w.ms(500) , w.moveTank(-75 ,-75)],
        w.resetEncoder(),
        w.resetImu(),
        [w.degree(200), w.straight(50)],
        [w.heading(90), w.turn()],
        w.resetEncoder()
    )
    w.runConcurrent(
        m1.resetEncoder(),   
        [m1.degree(M1_DOWN),m1.move(-75)],
        m1.brake(),				#down
        m1.resetEncoder()
    )
    w.run(
        [w.degree(100), w.straight(50)],
        [w.degree(200), w.straight(75)],
        [w.degree(450), w.straight(100)],
        [w.degree(500), w.straight(75)],
        [w.degree(650), w.straight(50)],
        w.resetEncoder()
    )
    w.run(
        [ w.blackReflection(20), w.straight(75) ],
        [ w.all(w.blackReflection(20), w.ms(100)), w.straight(75) ],
        w.resetEncoder(),
        [ w.degree(200), w.straight(50)],
        [w.ms(20),w.brake()],
        w.resetEncoder()	#half
    )
    w.run(
        [w.ms(80), w.brake()],
        [w.heading(20), w.turn() ],
        w.resetEncoder(),
        [w.degree(60), w.straight(50)],
        [w.ms(20), w.brake()],
        [m1.degree(420),m1.move(100)],m1.hold(),
        w.resetEncoder(),
        m1.resetEncoder(), 		#backdown
        [w.heading(75), w.turn() ],		#turnblock
        [w.ms(20), w.brake()],
        w.resetEncoder(),
        [w.degree(100), w.straight(-50)],	
        [w.degree(200), w.straight(-75)],	
        [w.degree(650), w.straight(-100)],	
        [w.degree(720), w.straight(-50)],
    )

    w.run(
        w.resetEncoder(),
        [ w.blackReflection(20), w.straight(75) ],
        [w.heading(90), w.turn()],
        w.resetEncoder(),		#returntoline
        [w.degree(100), w.straight(50)],	
        [w.degree(600), w.straight(100)],
        [w.degree(700), w.straight(75)],
        [w.degree(850), w.straight(50)],
        w.resetEncoder(),
    )

    w.runConcurrent(
        [w.ms(2500)],
        m1.resetEncoder(),
        [m1.degree(430),m1.move(-75)],m1.brake(),
        m1.resetEncoder()
    )
    w.run(
        [w.ms(20),w.brake()],
        [w.heading(0),w.turn()],
        w.resetEncoder(),
        [w.degree(100),w.straight(50)],
        [w.degree(500),w.straight(75)],
        [w.degree(600),w.straight(50)],
        w.resetEncoder()
    )

    w.run(
        [ w.blackReflection(20), w.straight(75) ],
        w.resetEncoder(),
        [ w.degree(100) , w.straight(50)],
        [ w.degree(300) , w.straight(75)],
        [ w.degree(500) , w.straight(50)],
        [ w.heading(-90) , w.turn()],
        w.resetEncoder()
    )

    w.run(
        [w.degree(100),w.straight(-50)],
        [w.degree(200),w.straight(-75)],
        [w.degree(350),w.straight(-50)],
        [m1.degree(400), m1.move(100)],		#keep yellow
        w.resetEncoder(),
        m1.resetEncoder()
    )

    w.run(
        [ w.degree(200), w.straight(75) ],
        [ w.heading(-110), w.turn()],
        [w.degree(250),w.straight(75)],
        w.resetEncoder(),
        [ w.heading(-180), w.turn()],
    )

    w.run(	
        [ w.blackReflection(20), w.straight(100) ],
        [ w.all(w.blackReflection(20), w.straight(75)) ],
        [ w.all(w.blackReflection(20), w.straight(75)) ],
    )

    w.run(
        [w.ms(80),w.brake()],
        [w.heading(270), w.turn()],
        [ w.degree(100), w.straight(50)],
        [ w.degree(200), w.straight(75)],
        [ w.degree(400), w.straight(100)],
        [ w.degree(500), w.straight(75)],
        [ w.degree(600), w.straight(50)],
    #     [ w.all(w.blackReflection(20), w.straight(75)) ], #back to half
    )
    w.run(
        
    )
    # w.run(
    #     [w.ms(80),w.brake()],
    #     [w.degree(100) , w.striaght(-50)],
    #     [w.degree(200) , w.striaght(-50)],
    #     [w.degree(300) , w.striaght(-75)],
    #     w.resetencoder()
        
    # )
    # w.runConcurrent(
    #     [w.ms(600)],
    #     [m1.degree(100), m1.move(75)],
    #     m1.resetEncoder()	
    # )

    # w.run(
    #     [w.blackReflection(20), w.straight(50)]	,
    #     [w.heading(-180),w.turn()],
    #     [w.degree(100),w.stright(50)],
    #     [w.degree(1400),w.stright(75)],
    #     [w.degree(1500),w.stright(50)],
    #     w.resetEncoder()
    #     [w.heading(0), w.turn()],
    #     [w.degree(150),w.straight(-50)],	 #SET ZERO FOR MOSAIC
    #     w.resetEncoder()
    # )
def mosaicSection():
    w.runConcurrent( #set 0 m2 
        [w.ms(400), m2.move(75)],
        m2.resetEncoder(),
        m2.hold()
    )

    w.runConcurrent( #set 0 m1 
        [w.ms(1000)],
        [w.ms(400), m1.move(75)],
        m1.resetEncoder(),
        m1.hold()
    )
    w.run(
        [w.ms(1000), w.moveTank(-50,-50)],
        [w.ms(50), w.brake() ],
        w.resetImu(),
        w.resetEncoder(),
        [ w.heading(45), w.turn(PIVOT_RIGHT , kp=8 ,ki=1.5, kd=0.24) ],
        [ w.heading(0), w.turn(PIVOT_LEFT, kp=8.2 ,ki=1.5, kd=0.24) ]
    )
    w.runConcurrent(
        m2.resetEncoder(), 
        [m2.degree(67), m2.move(-100)],
        m2.hold(),
    )
    
    w.run(
        [w.ms(80),w.brake()],
        [w.blackReflection(20),w.straight(50)]
    )
    w.runConcurrent(
        m1.resetEncoder(),  
        [m1.degree(320),m1.move(-75)],
        m1.brake()
    )

def keep(left_or_right):
    w.run(
        [ w.heading(-110 if left_or_right == PIVOT_RIGHT else -70), w.turn(left_or_right) ], w.brake(),
    )

    w.runConcurrent(
        [ m2.degree(90), m2.move(-100) ], m2.brake()
    )

    w.runConcurrent(
        [ w.ms(50)],m1.resetEncoder(),
        [ m1.degree(290), m1.move(100) ],
        m1.resetEncoder(),
        m1.brake(),
    )
    w.run( # KEEP
        [ w.ms(250) ],
        [ w.heading(-90), w.turn() ],
        [ w.ms(50), w.brake() ],
        w.resetEncoder(),
        [ w.degree(200), w.straight(50) ],
        w.brake(),
        m1.resetEncoder(),
        [ m1.degree(50), m1.move(-100) ],
        [ m1.degree(90), m1.move(-75) ],
        m1.brake(),
        m1.move(-10),
        w.resetEncoder()
    )

    w.run( # RETURN TOORIGINAL POSITION
        [ w.ms(50) ],
        [ w.degree(160), w.straight(-75) ],
        [ w.ms(50), w.brake() ]
    )
    
    w.run( # SET0 M2, RETURN M1, M2 TO ORIGINAL POSITION
        [ w.ms(80) ],

        [ m1.degree(290), m1.move(-100) ],
        [ w.ms(50), m1.move(-100) ],
        m1.brake(),

        [ w.ms(300), m2.move(100) ],
        m2.hold(),
    )

YELLOW = 0
BLUE = 1
GREEN = 2
WHITE = 3

BRAKE_TIME = 20
M2_PICK = 69
M1_DOWN = 290
class moveToDestinationEx3:
    def __init__(self, pick_queue):
        self.picked = 0
        self.current_pos = -1
        self.pick_queue = pick_queue
        self.pick_map = [ 0, 0, 0, 0 ]

    def gotoMid(self):
        middle = 1.5
        next_dist = middle - self.pick_queue[self.picked-1]

        if next_dist > 0:
            sign = 1
            angle = 0
        if next_dist < 0:
            sign = -1
            angle = -180

        w.run(
            [ w.blackReflection(20), w.straight(-50) ],
            w.resetEncoder(),
            [ w.degree(30), w.straight(-50)],
            [ w.ms(BRAKE_TIME), w.brake() ],
            [ w.heading(angle), w.turn() ],
            [ w.blackReflection(20), w.straight(-75 if self.pick_queue[self.picked-1] == GREEN else 75) ],
            [ w.ms(10), w.brake() ],
            w.resetEncoder(),
            # [ w.degree(50), w.straight(50) ],
            [ w.heading(90 if sign == 1 else -270), w.turn() ],
            [ w.ms(10), w.brake() ],
            w.resetEncoder(),
        )

        w.runConcurrent(
            [ m2.degree(M2_PICK), m2.move(-75) ],
            m2.hold(),
            [ w.ms(300) ],
            [ w.ms(50), m2.move(100) ],
            m2.move(30),
        )
        
        w.run(
            [ w.degree(250), w.tagline(75, 15, sign) ],
            [ w.ms(BRAKE_TIME), w.brake() ],
            w.resetEncoder(),
            [ m2.degree(90), m2.move(-100) ],m2.hold()
        )

        w.runConcurrent(
            [ m2.degree(140), m2.move(-100) ],
            m2.hold(),
        )

        w.runConcurrent(
            m1.resetEncoder(),
            [ w.ms(50) ],
            [ m1.degree(150), m1.move(100) ],
            [ m1.degree(290), m1.move(75) ],
            m1.resetEncoder(),
            m1.hold(),
        )

        w.run(
            [ w.ms(550) ],
            [ w.degree(225), w.straight(-50) ],
            w.brake(),
            w.resetEncoder(),
        )

        w.runConcurrent(
            [ m1.degree(290), m1.move(-75) ],
            m1.hold(),
        )

        w.run(
            [w.ms(600)],
            [ w.degree(325), w.tagline(50, 15, sign) ],
            [ w.degree(425), w.straight(75) ],
        )

        w.runConcurrent(
            m2.move(100)
        )

        w.run(
            [ w.degree(525), w.straight(50) ],
            [ w.ms(200), w.straight(30) ],
            [ w.ms(BRAKE_TIME), w.brake() ],
            w.resetEncoder(),
            w.resetImu(90),
            [ w.degree(15), w.straight(-50) ],
            [ w.ms(BRAKE_TIME), w.brake() ],
            m1.resetEncoder(),
            w.resetEncoder(),
            [ m1.degree(90), m1.move(100) ],
            m1.move(-10),
            [ w.degree(130), w.straight(50) ],
            [ w.ms(BRAKE_TIME), w.brake() ],
            w.resetEncoder(),
            [ m2.degree(140), m2.move(50) ],
            [ w.ms(100), m2.brake() ],
            [ w.ms(300), m2.move(100) ],
            m2.brake(),
            m1.move(-100),

            [ w.heading(-90), w.turn() ],
            [ w.ms(BRAKE_TIME), w.brake() ],
            w.resetEncoder(),
            m1.brake(),
            [ w.degree(25), w.straight(-50) ],
            [ w.degree(50), w.straight(-75) ],
            [ w.degree(125), w.straight(-100) ],
            [ w.ms(200), w.straight(-30) ],
            [ w.ms(BRAKE_TIME), w.brake() ],
            w.resetEncoder(),
            w.resetImu(-90)
        )

        w.runConcurrent( #SET0 M2
            [ w.ms(300), m2.move(-75) ], 
            m2.resetEncoder(),
            m2.hold(),
            [ m2.degree(M2_PICK), m2.move(75) ],
            m2.brake(),
        )

        w.runConcurrent( #SET0 M1
            [ w.ms(300), m1.move(75) ],
            m1.resetEncoder(),
            m1.hold(),
            [ m1.degree(100), m1.move(-100) ],
            [ m1.degree(M1_DOWN), m1.move(-50) ],
            m1.brake(),
        )

        w.run(
            [ w.degree(50), w.straight(50) ],
            [ w.degree(100), w.straight(75) ],
            [ w.degree(825), w.straight(100) ],
            [ w.degree(875), w.straight(75) ],
            [ w.degree(925), w.straight(50) ],
            [ w.blackReflection(20), w.straight(30) ],
            [ w.ms(BRAKE_TIME), w.brake() ],
        )

        self.current_pos = middle

    def gotoNext(self):
        next_color = self.pick_queue[self.picked]
        next_dist = next_color - self.current_pos
        distance = abs(next_dist)
        sign = 0
        angle = -90

        if next_dist > 0:
            sign = 1
            angle = 0
        if next_dist < 0:
            sign = -1
            angle = -180

        # INITIALLY TURN AND ACCELS
        if distance != 0:
            w.run(
                [ w.heading(angle), w.turn()], # here
                [ w.ms(BRAKE_TIME), w.brake() ],
                w.resetEncoder(),
                [ w.degree(30), w.straight(50) ],
                w.resetEncoder(),
            )
            if self.current_pos != 1.5 :
                w.run(
                    [w.degree(25),w.straight(50)],
                    w.resetEncoder()
                )
        # MOVE TO DESTINATION
        if distance == 4:
            w.run(
                [ w.blackReflection(20), w.straight(75) ],
                [ w.all(w.blackReflection(20), w.ms(50)), w.straight(100) ],
                [ w.all(w.blackReflection(20), w.ms(50)), w.straight(100) ],
                [ w.all(w.blackReflection(20), w.ms(50)), w.straight(75) ],
            )
        if distance == 3:
            w.run(
                [ w.blackReflection(20), w.straight(75) ],
                [ w.all(w.blackReflection(20), w.ms(50)), w.straight(100) ],
                [ w.all(w.blackReflection(20), w.ms(50)), w.straight(75) ],
            )
        if distance == 2:
            w.run(
                [ w.blackReflection(20), w.straight(75) ],
                [ w.all(w.blackReflection(20), w.ms(50)), w.straight(75) ],
            )
        if distance == 1:
            w.run(
                [ w.ms(100)],
                [ w.blackReflection(20) , w.straight(75) ],
            )

        if distance != 0:
            if sign == -1:
                w.run(
                    w.resetEncoder(),
                    [w.degree(80),w.straight(50)],
                    [w.ms(BRAKE_TIME),w.brake()],
                    w.resetEncoder()
                )
            w.run(
                w.resetEncoder(),
                [w.ms(50),w.brake()],
                [w.degree(40),w.moveTank(-70 * sign, 35 * sign)],
                [ w.heading(-90), w.turn() ],
                [ w.ms(BRAKE_TIME), w.brake() ],
                w.resetEncoder()
            )

        w.run(
            [ w.degree(25), w.straight(-50) ],
            [ w.degree(50), w.straight(-75) ],
            [ w.blackReflection(20), w.straight(-50) ],
            [ w.ms(BRAKE_TIME), w.brake() ],
            w.resetEncoder()
        )

        w.run(
            [ m2.degree(M2_PICK), m2.move(-100) ],
            m2.hold()
        )


        counter = self.pick_map[next_color]
        row = counter // 2
        deg_in = [ 20 , 150, 240 ] #แก้
        deg_out_even = [ 0, 100, 210 ]
        deg_out_odd = [ 0, 70, 180 ]
        
        print(f"row = {row}")
        if counter % 2 == 0:
            w.run(
                w.resetEncoder(),
                [ w.degree(25), w.straight(50) ],
                [ w.degree(160 + deg_in[row]), w.straight(75) ],
                [ w.degree(200 + deg_in[row]), w.straight(50) ],
            )
  
        if counter % 2 != 0:    
            w.run(
                w.resetEncoder(),
                [ w.degree(25), w.straight(50) ],
                [ w.degree(50 + deg_in[row]), w.straight(75) ],
                [ w.degree(80 + deg_in[row]), w.straight(50) ],

                [ w.heading(-71), w.turn() ],
                [ w.ms(BRAKE_TIME), w.brake() ],
                w.resetEncoder(),
                [ w.degree(25), w.straight(50) ],
                [ w.degree(100), w.straight(75) ],
                [ w.degree(120), w.straight(50) ],
            )

        w.runConcurrent(
            [ w.ms(500), m2.move(100) ],
            m2.move(30),
        )

        if counter % 2 == 0:
            w.run(
                w.resetEncoder(),
                [ w.degree(25), w.straight(-50) ],
                [ w.degree(40 + deg_out_even[row]), w.straight(-75) ],
                [ w.degree(75 + deg_out_even[row]), w.straight(-50) ],
                [ w.ms(BRAKE_TIME), w.brake() ],
            )
        
        if counter % 2 != 0:
            w.run(
                w.resetEncoder(),
                [ w.degree(25), w.straight(-50) ],
                [ w.degree(50), w.straight(-75) ],
                [ w.degree(120), w.straight(-50) ],
                [ w.ms(BRAKE_TIME), w.brake() ],
                [ w.heading(-90), w.turn() ],
                [ w.ms(BRAKE_TIME), w.brake() ],
            )

            if counter // 2 != 0:
                w.run(
                    w.resetEncoder(),
                    [ w.degree(20), w.straight(-50) ],
                    [ w.degree(deg_out_odd[row]), w.straight(-75) ],
                    [ w.degree(25 + deg_out_odd[row]), w.straight(-50) ],
                    [ w.ms(BRAKE_TIME), w.brake() ],
                )
            else:
                w.run(
                    w.resetEncoder(),
                    [ w.degree(deg_out_odd[row]), w.straight(-50) ],
                    [ w.ms(BRAKE_TIME), w.brake() ],
                )
        # w.run(
        #     [w.untilStdin("w")]
        # )
        self.pick_map[next_color] += 1
        self.current_pos = next_color
        self.picked += 1

def tester():

    w.run(
        [w.degree(2000),w.tagline(50 , 15 ,telemetry=True)]
    )
    # w.run(
    #     w.resetEncoder(),
    #     [ w.degree(80), w.moveTank(-70, 35)],
    #     [ w.heading(-90), w.turn(PIVOT_LEFT , kp=8.0 )], # here
    #     [ w.ms(BRAKE_TIME), w.brake() ],
    # )
    # w.run(
    #     [ w.heading(-90) , w.turn(telemetry=True) ],
    #     [ w.ms(50) , w.brake() ],
    #     w.resetEncoder(),
    #     [ w.degree(400) , w.straight(75) ] 
    # )

        # [w.heading(30),w.turn(telemetry=True)]
        # [ w.heading(30), w.turn(PIVOT_LEFT,kp=3.3,kd=0.025 ,telemetry=True) ]
        # [ w.heading(-30), w.turn(PIVOT_LEFT,kp=3.34,kd=0.028 ,telemetry=True) ]
        # [ w.heading(90), w.turn(PIVOT_LEFT,kp=3.38,kd=0.025 ,telemetry=True) ]
        # [ w.heading(-90), w.turn(PIVOT_LEFT,kp=3.38,kd=0.025 ,telemetry=True) ]
        # [ w.heading(30), w.turn(PIVOT_RIGHT,kp=3.3,kd=0.033 ,telemetry=True) ]
        # [ w.heading(-30), w.turn(PIVOT_RIGHT,kp=3.2,kd=0.04 ,telemetry=True) ]
        # [ w.heading(90), w.turn(PIVOT_RIGHT,kp=3.2,kd=0.036 ,telemetry=True) ]
        # [ w.heading(-90), w.turn(PIVOT_RIGHT,kp=3.4,kd=0.04 ,telemetry=True) ]
 
def main():
    # tester()
    FirstMission()
    # mosaicSection()
    # # test = moveToDestinationEx3([ YELLOW , YELLOW , YELLOW , YELLOW , YELLOW , YELLOW ])
    # test = moveToDestinationEx3([ WHITE , BLUE , YELLOW , WHITE , GREEN , BLUE ])
    # test.gotoNext()
    # test.gotoNext()
    # keep(PIVOT_RIGHT)
    # test.gotoNext()
    # test.gotoNext()
    # keep(PIVOT_LEFT)
    # test.gotoNext()
    # test.gotoNext()
    # test.gotoMid()
    # # test.gotoHome()

    print(f"charging current: {w._hub.charger.current()}")
    print(f"battery voltage:  {w._hub.battery.voltage()}")

main()