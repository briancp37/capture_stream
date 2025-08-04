CFB26_ATTRS = {
    "NAME": "Name",
    "YEAR": "Year",
    "POS": "Position",
    "OVR": "Overall",
    "SPD": "Speed",
    "STR": "Strength",
    "AGI": "Agility",
    "ACC": "Acceleration",
    "AWR": "Awareness",
    "CTH": "Catching",
    # Ball carrier traits:
    "BTK": "Break Tackle",
    "TRK": "Trucking",
    "COD": "Change of Direction",
    "BCV": "Ball Carrier Vision",
    "SFA": "Stiff Arm",
    "SPM": "Spin Move",
    "JKM": "Juke Move",
    "CAR": "Carrying (ball security / turnover tendency)",
    "JMP": "Jumping",
    # Quarterback throwing attributes:
    "THP": "Throw Power",
    "SAC": "Short Throw Accuracy",
    "MAC": "Medium Throw Accuracy",
    "DAC": "Deep Throw Accuracy",
    "RUN": "Throw on the Run Accuracy",
    "TUP": "Throw Under Pressure Accuracy",
    "BSK": "Break Sack",
    "PAC": "Play Action Accuracy",
    # Receiver route running & catching:
    "SRR": "Short Route Running",
    "MRR": "Medium Route Running",
    "DRR": "Deep Route Running",
    "CIT": "Catch In Traffic",
    "SPC": "Spectacular Catch",
    "RLS": "Release (getting off the line)",
    # Blocking attributes:
    "PBK": "Pass Blocking",
    "PBP": "Pass Block Power",
    "PBF": "Pass Block Finesse",
    "RBK": "Run Blocking",
    "RBP": "Run Block Power",
    "RBF": "Run Block Finesse",
    "IBK": "Impact Blocking",
    # Defensive skills:
    "PRC": "Play Recognition",
    "TAK": "Tackle",
    "POW": "Power (tackle strength)",
    "PMV": "Power Moves",
    "FMV": "Finesse Moves",
    "BSH": "Block Shedding",
    "PUR": "Pursuit",
    "MCV": "Man Coverage",
    "ZCV": "Zone Coverage",
    "PRS": "Press (line coverage at the line)",
    # Kicking/punting:
    "KPW": "Kick Power",
    "KAC": "Kick Accuracy",
    "RET": "Return Ability"
}


CROP_LOCATIONS = {
    'WEEKLY_SCHEDULE': {
        'week': {},
        'games': {}
    },
    'ROSTER': {
        'page_title': {'x': 40, 'y': 20, 'w': 500, 'h': 40},
        'table_data': {'x': 60, 'y': 265, 'w': 860, 'h': 349},
        'attr_height': {'x': 60, 'y': 343, 'w': 860, 'h': 11}
    },
    'SCORES_SCHEDULE': {
        'page_title': {'x': 40, 'y': 20, 'w': 500, 'h': 40},
        'table_data': {'x': 60, 'y': 265, 'w': 860, 'h': 349},
        'attr_height': {'x': 60, 'y': 343, 'w': 860, 'h': 11}
    }
}

MOUNTED_DIR = "/Users/brianpennington/git/cfb/cfb_shared"
TEAM_SCHEDULE_PATHS = [
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011138_000006.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011140_000007.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011142_000008.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011142_000009.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011142_000010.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011142_000011.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011142_000012.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011142_000013.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011142_000014.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011142_000015.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011142_000016.jpg"
]

SCORES_SCHEDULE_PATHS = [
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011153_000042.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011153_000043.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011153_000044.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011155_000045.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011155_000046.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011155_000047.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011155_000048.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011155_000049.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011155_000050.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011155_000051.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011155_000052.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011158_000053.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011158_000054.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011158_000055.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011158_000056.jpg",
    "/Users/brianpennington/mnt/cfb_shared/screenshots/frame_20250804_011158_000057.jpg"
]

TOP_25_PATHS = [
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011204_000075.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011204_000076.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011205_000077.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011205_000078.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011205_000079.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011205_000080.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011205_000081.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011205_000082.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011206_000083.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011206_000084.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011207_000085.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250804_011207_000086.jpg"
]


GOING_RIGHT_PATHS = [
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185847_000003.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185852_000004.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185852_000005.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185852_000006.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185852_000007.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185852_000008.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185854_000009.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185854_000010.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185854_000011.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185854_000012.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185854_000013.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185854_000014.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185854_000015.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185856_000016.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185856_000017.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185856_000018.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185856_000019.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185856_000020.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185856_000021.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185856_000022.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185856_000023.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185858_000024.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185858_000025.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185858_000026.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185858_000027.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_185858_000028.jpg"
]


# DOWN_PATHS = [
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000008.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000010.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000011.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000012.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000013.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000014.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000015.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000016.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000017.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000018.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000019.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000020.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000021.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000022.jpg
# ]

# RIGHT_PATHS = [
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210349_000034.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210349_000035.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210349_000036.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210349_000037.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000039.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000040.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000041.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000043.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000044.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000045.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210353_000046.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210353_000048.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210353_000049.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210355_000050.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210355_000051.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210355_000053.jpg
# ]
# UP_PATHS = [
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210355_000055.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000056.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000057.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000058.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000059.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000060.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000061.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000062.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000063.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000064.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000065.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000066.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000067.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000068.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000069.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000070.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000071.jpg
# ]

# LEFT_PATHS = [
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210402_000079.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210403_000088.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210404_000089.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210404_000090.jpg
#     /Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210404_000091.jpg
# ]

DOWN_PATHS = [
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000008.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000010.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000011.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000012.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000013.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210342_000014.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000015.jpg", 
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000016.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000017.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000018.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000019.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000020.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000021.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210344_000022.jpg",
]

RIGHT_PATHS = [
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210349_000034.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210349_000035.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210349_000036.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210349_000037.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000039.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000040.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000041.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000043.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000044.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210351_000045.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210353_000046.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210353_000048.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210353_000049.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210355_000050.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210355_000051.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210355_000053.jpg",
]

UP_PATHS = [
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210355_000055.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000056.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000057.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000058.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000059.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000060.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000061.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000062.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000063.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210357_000064.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000065.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000066.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000067.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000068.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000069.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000070.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210359_000071.jpg",
]

LEFT_PATHS = [
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210402_000079.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210403_000088.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210404_000089.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210404_000090.jpg",
    "/Users/brianpennington/git/cfb/capture_stream/mtn/cfb_shared/screenshots_4dir/frame_20250802_210404_000091.jpg",
]

MAC_IP = "192.168.1.179"
JETSON_IP="192.168.1.62"