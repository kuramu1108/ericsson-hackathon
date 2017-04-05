from enum import Enum


class SensorFamily(Enum):
    """Sensor Types avaialble through the api."""

    WASP = 'wasp'
    EMBED = 'embed'
    WEATHER = 'weather'
    LOGINS = 'logins'
    PEOPLE = 'people'


class WaspUnit(Enum):
    """Available Wasp Unit Identifiers."""

    ES_B_08_423_7BE2 = 'ES_B_08_423_7BE2'
    ES_A_06_195_3E87 = 'ES_A_06_195_3E87'
    ES_B_11_429_3E90 = 'ES_B_11_429_3E90'
    ES_B_12_431_7BC2 = 'ES_B_12_431_7BC2'
    ES_B_02_412_3E68 = 'ES_B_02_412_3E68'
    ES_B_09_424_B74C = 'ES_B_09_424_B74C'
    ES_B_04_414_7C00 = 'ES_B_04_414_7C00'
    ES_B_06_419_7C09 = 'ES_B_06_419_7C09'
    ES_B_12_430_44DE = 'ES_B_12_430_44DE'
    ES_B_06_418_7BED = 'ES_B_06_418_7BED'
    ES_C_13_302_C88E = 'ES_C_13_302_C88E'
    ES_B_09_425_3E8D = 'ES_B_09_425_3E8D'
    ES_A_13_276_7C44 = 'ES_A_13_276_7C44'
    ES_B_11_428_3EA4 = 'ES_B_11_428_3EA4'
    ES_B_08_422_7BDC = 'ES_B_08_422_7BDC'
    ES_A_04_159_7B7E = 'ES_A_04_159_7B7E'
    ES_B_10_427_7B90 = 'ES_B_10_427_7B90'
    ES_B_01_411_7E39 = 'ES_B_01_411_7E39'
    ES_B_04_415_7BD1 = 'ES_B_04_415_7BD1'
    ES_B_05_416_7C15 = 'ES_B_05_416_7C15'
    ES_B_05_417_7C13 = 'ES_B_05_417_7C13'
    ES_B_10_426_7E1E = 'ES_B_10_426_7E1E'
    ES_B_07_421_7C17 = 'ES_B_07_421_7C17'
    ES_B_07_420_7E1D = 'ES_B_07_420_7E1D'
    ES_A_09_298_7BC5 = 'ES_A_09_298_7BC5'
    ES_A_09_226_44DF = 'ES_A_09_226_44DF'
    ES_A_07_207_44FA = 'ES_A_07_207_44FA'
    ES_A_06_291_CE30 = 'ES_A_06_291_CE30'
    ES_A_05_181_7BDA = 'ES_A_05_181_7BDA'
    ES_A_10_234_3E9E = 'ES_A_10_234_3E9E'
    ES_A_11_245_CE2B = 'ES_A_11_245_CE2B'
    ES_A_07_293_3E72 = 'ES_A_07_293_3E72'
    ES_A_03_141_CE3A = 'ES_A_03_141_CE3A'
    ES_A_03_151_CE38 = 'ES_A_03_151_CE38'
    ES_A_03_153_CE2A = 'ES_A_03_153_CE2A'
    ES_A_12_301_7BB6 = 'ES_A_12_301_7BB6'
    ES_A_06_292_7BBF = 'ES_A_06_292_7BBF'
    ES_A_05_175_CE2E = 'ES_A_05_175_CE2E'
    ES_A_04_163_7C58 = 'ES_A_04_163_7C58'
    ES_A_07_294_7BBC = 'ES_A_07_294_7BBC'
    ES_A_11_300_7BCD = 'ES_A_11_300_7BCD'


class PeopleUnit(Enum):
    """Available people counters."""

    # Note, these people counters are the most active in B11, so we'll
    # assign them to fire exits to simulate alot of activity during a fire
    FIRE_1 = 'PC0216-JonesStEntrance'
    FIRE_2 = 'PC0007-WattleStB10Entrance'
    FIRE_3 = 'PC0214-BroadwayEastEntrance'
    PC02_15_IN = ' PC02.15 (In)'
    PC02_15_OUT = ' PC02.15 (Out)'
    PC02_16_IN = ' PC02.16 (In)'
    PC02_16_OUT = ' PC02.16 (Out)'


class WaspSubCode(Enum):
    """Available Wasp Unit Sub codes."""

    BATTERY = 'BAT'
    LUMINOSITY = 'LUM'
    TEMPERATURE = 'TCA'
    HUMIDITY = 'HUMA'
    OXYGEN = 'O2'
    AIR_POLLUTANTS = 'AP2'
    HYDROCARBONS = 'VOC'
    CARBON_DIOXIDE = 'CO2'


class EmbedUnit(Enum):
    """Available Embedded Sensor Identifiers."""

    ESD00_1 = 'ESD00_1'
    ESD06_2 = 'ESD06_2'
    ESD12_1 = 'ESD12_1'
    ESD12_2 = 'ESD12_2'
    ESD13_1 = 'ESD13_1'
    ESDB3_2 = 'ESDB3_2'


class EmbedSubCode(Enum):
    """Available Embedded Sensor sub codes."""

    SG_06C_103B = 'SG.06C.103B'
    SG_06C_103BR = 'SG.06C.103BR (Ohms)'
    SG_06C_109B = 'SG.06C.109B'
    SG_06C_109BR = 'SG.06C.109BR (Ohms)'
    SG_06C_120B = 'SG.06C.120B'
    SG_06_120BR = 'SG.06.120BR (Ohms)'
    CI_06S_R245L = 'CI.06S.R245L (mV)'


class WeatherUnit(Enum):
    """Available Weather Sensor Identifiers."""

    WIND_DIR        = 'WD'
    AIR_TEMP        = 'AT'
    SOLAR_RADIATION = 'SR'
    RAIN_GUAGE      = 'RG'
    UVA_RADIATION   = 'UV'
    WDIR_COSINE     = 'WC'
    WDIR_SINE       = 'WS'
    BATTERY_VOLTAGE = 'BV'
    LOAD_CURRENT    = 'LC'
    SOLAR_VOLTAGE   = 'SV'
    CHARGE_CURRENT  = 'CC'
    PEAK_WIND_GUST  = 'PW'
    WIND_SPEED_INST = 'IWS'
    WIND_DIR_INST   = 'IWD'
    NW_WIND_SPEED   = 'NW'
    EW_WIND_SPEED   = 'EW'
    RAIN_TOTAL      = 'RT'
    COMMS           = 'Co'


class LoginUnit(Enum):
    """Available PCLab Login Unit Identifiers."""

    E1_04201 = 'E1-04201'
    E1_05204 = 'E1-05204'
    E1_05300 = 'E1-05300'
    E1_053L0 = 'E1-053L0'
    E1_053V0 = 'E1-053V0'
    E1_05402 = 'E1-05402'
    E1_06101 = 'E1-06101'
    E1_06102 = 'E1-06102'
    E1_06103 = 'E1-06103'
    E1_061V2 = 'E1-061V2'
    E1_07403 = 'E1-07403'
    E1_07404 = 'E1-07404'
    E1_07405 = 'E1-07405'
    E1_07406 = 'E1-07406'
    E1_08409 = 'E1-08409'
    E1_09405 = 'E1-09405'
    E1_10104 = 'E1-10104'
    E1_11300 = 'E1-11300'
    E1_11302 = 'E1-11302'
    E1_11403 = 'E1-11403'
    E1_B1100 = 'E1-B1100'
    E1_B1102 = 'E1-B1102'
    E1_B1103 = 'E1-B1103'
    E1_B11V2 = 'E1-B11V2'
    E1_B11V3 = 'E1-B11V3'
    E1_B1203 = 'E1-B1203'
    E1_B1204 = 'E1-B1204'
    E1_B1400 = 'E1-B1400'
    E1_B1401 = 'E1-B1401'
    E1_B1402 = 'E1-B1402'
    E1_B1403 = 'E1-B1403'
    E1_B14V0 = 'E1-B14V0'
    E1_B14V1 = 'E1-B14V1'
    E1_B14V2 = 'E1-B14V2'
    E1_B14V3 = 'E1-B14V3'
