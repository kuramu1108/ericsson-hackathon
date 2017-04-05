from .types import SensorFamily
from .types import WaspUnit
from .types import WaspSubCode
from .types import EmbedUnit
from .types import EmbedSubCode
from .types import WeatherUnit
from .types import LoginUnit
from .types import PeopleUnit

class PersonSensor():

    def __init__(self, family, unit):
        self.family = family
        self.unit = unit

class FireSensor():

    def __init__(self, family, unit, subCode):
        self.family = family
        self.unit = unit
        self.subCode = subCode


class SensorGroup():
    """Blah."""

    def __init__(self, family, units, subCodes):
        """Constructor."""
        self.family = family
        self.units = units
        self.subCodes = subCodes


WASP_GROUP = SensorGroup(SensorFamily.WASP,
        [WaspUnit.ES_B_08_423_7BE2, WaspUnit.ES_A_06_195_3E87, WaspUnit.ES_B_11_429_3E90, WaspUnit.ES_B_12_431_7BC2, WaspUnit.ES_B_02_412_3E68, WaspUnit.ES_B_09_424_B74C, WaspUnit.ES_B_04_414_7C00, WaspUnit.ES_B_06_419_7C09, WaspUnit.ES_B_12_430_44DE, WaspUnit.ES_B_06_418_7BED,
        WaspUnit.ES_C_13_302_C88E, WaspUnit.ES_B_09_425_3E8D,
        WaspUnit.ES_A_13_276_7C44, WaspUnit.ES_B_08_422_7BDC, WaspUnit.ES_A_04_159_7B7E, WaspUnit.ES_B_10_427_7B90, WaspUnit.ES_B_01_411_7E39, WaspUnit.ES_B_04_415_7BD1,
        WaspUnit.ES_B_07_421_7C17, WaspUnit.ES_B_07_420_7E1D,
        WaspUnit.ES_A_09_298_7BC5, WaspUnit.ES_A_09_226_44DF,
        WaspUnit.ES_A_07_207_44FA, WaspUnit.ES_A_06_291_CE30,
        WaspUnit.ES_A_05_181_7BDA, WaspUnit.ES_A_10_234_3E9E,
        WaspUnit.ES_A_11_245_CE2B, WaspUnit.ES_A_07_293_3E72,
        WaspUnit.ES_A_03_141_CE3A, WaspUnit.ES_A_03_151_CE38,
        WaspUnit.ES_A_03_153_CE2A, WaspUnit.ES_A_12_301_7BB6,
        WaspUnit.ES_A_06_292_7BBF, WaspUnit.ES_A_05_175_CE2E,
        WaspUnit.ES_A_04_163_7C58, WaspUnit.ES_A_07_294_7BBC,
        WaspUnit.ES_A_11_300_7BCD],
        [WaspSubCode.BATTERY,
        WaspSubCode.LUMINOSITY,
        WaspSubCode.TEMPERATURE,
        WaspSubCode.HUMIDITY,
        WaspSubCode.OXYGEN,
        WaspSubCode.AIR_POLLUTANTS,
        WaspSubCode.HYDROCARBONS,
        WaspSubCode.CARBON_DIOXIDE])

EMBED_GROUP = SensorGroup(SensorFamily.EMBED,
        [EmbedUnit.ESD00_1,
        EmbedUnit.ESD06_2,
        EmbedUnit.ESD12_1,
        EmbedUnit.ESD12_2,
        EmbedUnit.ESD13_1,
        EmbedUnit.ESDB3_2],
        [EmbedSubCode.SG_06C_103B,
        EmbedSubCode.SG_06C_103BR,
        EmbedSubCode.SG_06C_109B,
        EmbedSubCode.SG_06C_109BR,
        EmbedSubCode.SG_06C_120B,
        EmbedSubCode.SG_06_120BR,
        EmbedSubCode.CI_06S_R245L])

WEATHER_GROUP = SensorGroup(SensorFamily.WEATHER,
        [WeatherUnit.WIND_DIR, WeatherUnit.AIR_TEMP,
        WeatherUnit.SOLAR_RADIATION, WeatherUnit.RAIN_GUAGE,
        WeatherUnit.UVA_RADIATION, WeatherUnit.WDIR_COSINE,
        WeatherUnit.WDIR_SINE, WeatherUnit.BATTERY_VOLTAGE,
        WeatherUnit.LOAD_CURRENT, WeatherUnit.SOLAR_VOLTAGE,
        WeatherUnit.CHARGE_CURRENT, WeatherUnit.PEAK_WIND_GUST,
        WeatherUnit.WIND_SPEED_INST, WeatherUnit.WIND_DIR_INST,
        WeatherUnit.NW_WIND_SPEED, WeatherUnit.EW_WIND_SPEED,
        WeatherUnit.RAIN_TOTAL, WeatherUnit.COMMS], [])

LOGINS_GROUP = SensorGroup(SensorFamily.LOGINS,
        [LoginUnit.E1_04201, LoginUnit.E1_05204, LoginUnit.E1_05300,
        LoginUnit.E1_053L0, LoginUnit.E1_053V0, LoginUnit.E1_05402,
        LoginUnit.E1_06101, LoginUnit.E1_06102, LoginUnit.E1_06103,
        LoginUnit.E1_061V2, LoginUnit.E1_07403, LoginUnit.E1_07404,
        LoginUnit.E1_07405, LoginUnit.E1_07406, LoginUnit.E1_08409,
        LoginUnit.E1_09405, LoginUnit.E1_10104, LoginUnit.E1_11300,
        LoginUnit.E1_11302, LoginUnit.E1_11403, LoginUnit.E1_B1100,
        LoginUnit.E1_B1102, LoginUnit.E1_B1103, LoginUnit.E1_B11V2,
        LoginUnit.E1_B11V3, LoginUnit.E1_B1203, LoginUnit.E1_B1204,
        LoginUnit.E1_B1400, LoginUnit.E1_B1401, LoginUnit.E1_B1402,
        LoginUnit.E1_B1403, LoginUnit.E1_B14V0, LoginUnit.E1_B14V1, LoginUnit.E1_B14V2, LoginUnit.E1_B14V3], [])

PEOPLE_GROUP = SensorGroup(SensorFamily.PEOPLE,
        [PeopleUnit.FIRE_1, PeopleUnit.FIRE_2, PeopleUnit.FIRE_3], [])
