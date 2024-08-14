from brawl_stars_brawler_maker import brawler_maker

brawler = brawler_maker.Brawler(
    brawlername="FrostByte",
    description="A cybernetic warrior with ice-infused cybernetics, capable of manipulating ice and cold.",
    hp=4800,
    speed=770,
    icon="nita",
    rarity="epic",
    attack_name="Ice Shard Barrage",
    attack_description="Launches a volley of sharp ice shards, piercing through enemies.",
    reloadtime=1600,
    ammonumber=3,
    range=26,
    numberofprojectiles=1,
    spread=0,
    damage=500,
    projectile="CactusProjectile",
    ulti_name="Blizzard Dome",
    ulti_description="Creates a dome of blizzard, slowing and damaging enemies, while boosting her speed.",
    ulti_spread=80,
    ulti_range=20,
    ulti_numberofprojectiles=1,
    ulti_damage=200,
    ulti_projectile="CactusUltiProjectile"
)

brawler.generate_files()
brawler.export_csv_logic_to_apk()
