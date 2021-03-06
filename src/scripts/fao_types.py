"""Constants for loading the FAO data from CSV files and
to assist with type conversion to match the Impex types"""

# FAO parts, identifiers for the CSV files
FAO_PARTS = [
    "crops",
    "livestock_primary",
    "livestock_processed",
    "seafood"
]

# FAO **substrings** of subtypes to explicitly
# convert them to match Impex subtypes.
FAO_TO_IMPEX_TYPE = {
    r"^meat_": "",  # remove "meat_" prefix
    "gooseberries": "currants_and_gooseberries",
    "currants": "currants_and_gooseberries",
    "beans_green": "beans_fresh",
    "broad_beans_horse_beans_dry": "beans_dry",
    "sheep": "sheep_goat",
    "goat": "sheep_goat",
    "horse": "equine",
    r"^milk.+$": "milk_cream",
    "cream_fresh": "milk_cream",
    r"^whey.+$": "whey",
    r"^butter.+$": "butter",
    r"^cheese.+$": "cheese",
    r"^eggs.+$": "eggs",
    r"^honey.+$": "honey",
    r"^.*peppers.*$": "peppers",
}

