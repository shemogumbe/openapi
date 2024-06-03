from enum import Enum

class TradeModel_attributes_marketDeliveryProfileName(str, Enum):
    Baseload = "Baseload",
    Peaks = "Peaks",
    Offpeaks = "Offpeaks",
    SuperPeaks = "SuperPeaks",
    ExtendedPeaks = "Extended-Peaks",
    ShortOffPeaks = "Short-OffPeaks",
    WD1 = "WD1",
    WD2 = "WD2",
    WD3 = "WD3",
    WD4 = "WD4",
    WD5 = "WD5",
    WD6 = "WD6",
    WE1 = "WE1",
    WE2 = "WE2",
    WE3 = "WE3",
    WE4 = "WE4",
    WE5 = "WE5",
    WE6 = "WE6",
    WD1_plus_WD2 = "WD1+WD2",
    WD3_plus_WD4 = "WD3+WD4",
    WD3_plus_WD5 = "WD3+WD5",
    WD3_plus_WD6 = "WD3+WD6",
    WD3_plus_WD4_plus_WD5 = "WD3+WD4+WD5",
    WD3_plus_WD4_plus_WD5_plus_WD6 = "WD3+WD4+WD5+WD6",
    WD1_plus_WD2_plus_WE1_plus_WE2 = "WD1+WD2+WE1+WE2",
    WD3_plus_WD4_plus_WE3_plus_WE4 = "WD3+WD4+WE3+WE4",
    WE1_plus_WE2 = "WE1+WE2",
    WE3_plus_WE4 = "WE3+WE4",
    WE3_plus_WE4_plus_WE5 = "WE3+WE4+WE5",
    WD1_plus_WE1 = "WD1+WE1",
    WD2_plus_WE2 = "WD2+WE2",
    WD3_plus_WE3 = "WD3+WE3",
    WD4_plus_WE4 = "WD4+WE4",
    WD5_plus_WE5 = "WD5+WE5",
    WD6_plus_WE6 = "WD6+WE6",
    WD3_plus_WD4_plus_WD5_plus_WD6_plus_WE3_plus_WE4_plus_WE5_plus_WE6 = "WD3+WD4+WD5+WD6+WE3+WE4+WE5+WE6",
    WE3_plus_WE4_plus_WE5_plus_WE6 = "WE3+WE4+WE5+WE6",
    WeekendsBaseload = "Weekends Baseload",
    WeekendsPeaks = "Weekends Peaks",
    WeekendsOffpeaks = "Weekends Offpeaks",
    WeekendsExtendedPeaks = "Weekends Extended-Peaks",
    WeekendsShortOffPeaks = "Weekends Short-OffPeaks",

