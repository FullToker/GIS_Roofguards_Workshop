"""
Created by Yushuo
2025.01.08

The class of the data object
"""

import numpy as np
from datetime import datetime
import pandas as pd


class System:
    items = []

    def __init__(self, did: int, name: str, lat: float, long: float):
        self.did = did
        self.name = name
        self.lat = lat
        self.long = long

    def open_xls(self, inpath):
        data = pd.read_excel(inpath)
        assert not data.empty, "cannot open the xls file"

        print(data)
        print(data.size)
        print(data.iloc[0])

        date_obj = datetime.strptime(date_str, "%d.%m.%Y %H:%M:%S")


class Item:
    def __init__(self):
        pass

    def get_value(self, timestamp: str, temp: float, snowload: int) -> None:
        pass

    def get_extraInfo(self, network: float, upperLimit: int, lowerLimit: int):
        self.network = network
        self.upperLimit = upperLimit
        self.lowerLimit = lowerLimit


if __name__ == "__main__":

    test = System(
        did=12095, name="PP313-112", lat=48.1148111111111, long=11.5541305555556
    )
    test.open_xls(
        "../Roofguards_Samples/WG_ Probedatensatz SchneelastWächter 1_3, Fa. UGM in 81371 München/01.12.2022_31.05.2023 357973044940762_2022-12-01.xls"
    )
    pass
