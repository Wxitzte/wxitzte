"""
Program's Entry Point for WRO2026 Senior
"""
from pybricks.parameters import Port, Color, Direction
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.hubs import PrimeHub

from huskylens import Huskylens, Block, ALGORITHM_COLOR_RECOGNITION
from drivebase import DriveBaseAPI, MissionMotor, PIVOT_LEFT, PIVOT_RIGHT

BACK_Degree = 0
FRONT_Degree = 0
BACKDI_Degree = 0

BACK_DOWN = -1
BACK_UP = 1
FRONT_DOWN = -1
FRONT_UP = 1


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
    pturn_params = {
        90:  (8.0 , 1.5 , 0.24),
    },
)

def getMosaicData(tiles: list[Block], ratio_tolerance: int, area_tolerance: int) -> list[list[int]] | None:
    filtered = [tile for tile in tiles if abs(tile.ratio() - ratio_tolerance) <= 1.0 and tile.area() <= area_tolerance]
    if len(filtered) < 12: return None
    sort_by_row = sorted(filtered, key = lambda tile: tile.y)
    return [[v.id for v in sorted(sort_by_row[i:i+4], key = lambda tile: tile.x)] for i in range(0, 12, 4)]

if __name__ == "__main__":
    print("Robot configuration loaded successfully!")
    prime_hub.speaker.beep()
