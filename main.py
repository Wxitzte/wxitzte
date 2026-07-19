from config import w, m1, m2, prime_hub, BACK_Degree, BACKDI_Degree, FRONT_Degree, BACK_UP, BACK_DOWN, FRONT_DOWN, FRONT_UP, PIVOT_LEFT, PIVOT_RIGHT, Huskylens, Block, ALGORITHM_COLOR_RECOGNITION, getMosaicData


def getMosaicData(tiles: list[Block], ratio_tolerance: int, area_tolerance: int) -> list[list[int]] | None:
    filtered = [tile for tile in tiles if abs(tile.ratio() - ratio_tolerance) <= 1.0 and tile.area() <= area_tolerance]
    if len(filtered) < 12: return None
    sort_by_row = sorted(filtered, key = lambda tile: tile.y)
    return [[v.id for v in sorted(sort_by_row[i:i+4], key = lambda tile: tile.x)] for i in range(0, 12, 4)]

def main():
    print(f"charging current: {w._hub.charger.current()}")
    print(f"battery voltage:  {w._hub.battery.voltage()}")

main()
