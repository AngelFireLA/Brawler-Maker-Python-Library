### Brawl Stars Brawler Maker: Unleash Your Creativity

**Brawl Stars Brawler Maker** is an innovative Python package designed to empower the Brawl Stars community with the ability to create custom brawlers and integrate them into the game. This package provides an extensive toolkit for modders of all skill levels, from beginners to experienced developers, to modify game files and bring their unique brawler concepts to life. Whether you're looking to introduce a new character with special abilities or tweak existing ones, Brawl Stars Brawler Maker offers a user-friendly and comprehensive platform to make your vision a reality.

#### Key Features:

- **Custom Brawler Creation:** Easily define brawler characteristics such as name, description, health points (HP), speed, attack and super abilities, including range, reload time, damage, and much more.
- **Intuitive Modding Process:** Modify game files to add your custom brawlers without the hassle of navigating through complex file structures. The toolkit handles the intricacies, allowing you to focus on creativity.
- **APK Export and Signing:** Generate and export your modded version of the game as an APK file, ready for installation on Android devices. Optional APK signing is available for a seamless installation experience.
- **Support for Customization:** With additional resources like predefined projectile types, rarities, and speed constants, the toolkit caters to both novice and seasoned modders, providing essential elements to customize your brawler to the fullest.

#### Getting Started:

The Brawl Stars Brawler Maker is straightforward to use. To create your custom brawler, you simply need to instantiate a `Brawler` object with your desired parameters, such as brawler name, stats, abilities, and appearance. Then, use the `generate_files` method to modify the necessary game files and `export_csv_logic_to_apk` to compile and export your modded game.

Here's a quick example to get you started:

```python
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
    projectile="MummyProjectile",
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
```

This example showcases how to create a brawler named FrostByte, complete with custom abilities and characteristics, then integrate it into the game.

#### Documentation and Support:

The Brawl Stars Brawler Maker package includes additional resources such as `projectiles.py`, `rarities.py`, and `speeds.py` to assist less experienced modders with predefined constants. These files are entirely optional but can simplify the process of setting up brawler attributes.

For a detailed understanding of all the features and functionalities offered by Brawl Stars Brawler Maker, including how to use the additional resources and customize your brawler further, please refer to the comprehensive documentation provided within the package.

Whether you're a seasoned modder looking to push the boundaries of Brawl Stars or a newcomer eager to create your first custom brawler, Brawl Stars Brawler Maker is your go-to toolkit. Unleash your creativity and transform the way you play Brawl Stars today!

## Brawl Stars Brawler Maker: Code Documentation

The Brawl Stars Brawler Maker library provides a comprehensive suite of tools designed for modding the game Brawl Stars, allowing users to create custom brawlers with unique characteristics and abilities. This documentation covers the core functionalities, including class definitions, methods, and usage examples to guide both novice and advanced modders through the process of creating and exporting custom brawlers.

### Core Class: `Brawler`

The `Brawler` class is the centerpiece of the Brawl Stars Brawler Maker package, encapsulating all the properties and methods needed to define a custom brawler and modify the game files accordingly.

#### Constructor: `__init__(self, brawlername, description, rarity, attack_name, attack_description, ulti_name, ulti_description, speed, hp, icon, range, reloadtime, ammonumber, damage, spread, numberofprojectiles, projectile, ulti_projectile, ulti_damage, ulti_spread, ulti_numberofprojectiles, ulti_range)`

- **Parameters:**
  - `brawlername`: String. The name of the brawler.
  - `description`: String. A short description of the brawler.
  - `rarity`: String. The rarity level of the brawler. Must be one of the predefined rarity levels.
  - `attack_name`: String. The name of the brawler's main attack.
  - `attack_description`: String. Description of the main attack.
  - `ulti_name`: String. The name of the brawler's ultimate ability.
  - `ulti_description`: String. Description of the ultimate ability.
  - `speed`: Integer. The movement speed of the brawler.
  - `hp`: Integer. The hit points (health) of the brawler.
  - `icon`: String. The name of the icon used for the brawler, must be one of the predefined brawler names.
  - `range`: Integer. The range of the main attack.
  - `reloadtime`: Integer. The reload time of the main attack.
  - `ammonumber`: Integer. The ammo number for the main attack.
  - `damage`: Integer. The damage dealt by the main attack.
  - `spread`: Integer. The spread of the main attack projectiles.
  - `numberofprojectiles`: Integer. The number of projectiles fired in the main attack.
  - `projectile`: String. The projectile type for the main attack.
  - `ulti_projectile`: String. The projectile type for the ultimate ability.
  - `ulti_damage`: Integer. The damage dealt by the ultimate ability.
  - `ulti_spread`: Integer. The spread of the ultimate ability projectiles.
  - `ulti_numberofprojectiles`: Integer. The number of projectiles for the ultimate ability.
  - `ulti_range`: Integer. The range of the ultimate ability.

- **Functionality:** Initializes a new `Brawler` instance with specified attributes. Validates the provided attributes against predefined criteria and constraints.

#### Method: `generate_files(self, csv_logic_folder_path, localization_folder_path, directly_modify=False, warning=True, debug=True)`

- **Purpose:** Modifies the game's CSV files to include the custom brawler's data.
- **Parameters (all optional):**
  - `csv_logic_folder_path`: String. Path to the game's `csv_logic` folder.
  - `localization_folder_path`: String. Path to the game's `localization` folder.
  - `directly_modify`: Boolean. If `True`, modifies the CSV files directly. If `False`, duplicates the folders before modification.
  - `warning`: Boolean. If `True` and `directly_modify` is `True`, displays a warning message before proceeding when modifying the original files.
  - `debug`: Boolean. If `True`, prints debug messages during the operation.
- **Functionality:** Adds the custom brawler's data to the game's `texts.csv`, `cards.csv`, `characters.csv`, `skins.csv`, `skin_confs.csv`, and `skills.csv` files, either by directly modifying the original files or by working on duplicates.

#### Static Method: `export_csv_logic_to_apk(csv_logic_folder_path=None, localization_folder_path=None, destination_folder=None, apk_mega_link="...", existing_apk_path=None, sign=False, debug=True)`

- **Purpose:** Compiles the modified game files into an APK, ready for installation.
- **Parameters (all optional):**
  - `csv_logic_folder_path`: String. Path to the modified `csv_logic` folder.
  - `localization_folder_path`: String. Path to the modified `localization` folder.
  - `destination_folder`: String. Path where the APK should be saved.
  - `apk_mega_link`: String. Custom Mega.nz link to the base APK if not using the default.
  - `existing_apk_path`: String. Path to an existing base APK to be modified.
  - `sign`: Boolean. Whether to sign the APK. Requires Java to be installed.
  - `debug`: Boolean. If `True`, prints debug messages during the operation.
- **Functionality:** Downloads the base APK if necessary, integrates the modified game files, and exports the result as an APK file. Optionally signs the APK for installation.

### Additional Resources

The package includes three optional resources to aid less experienced modders: `projectiles.py`, `rarities.py`, and `speeds.py`. These modules provide convenient constants for common game elements like projectile types, brawler rarities, and movement speeds, simplifying the process of setting up custom brawler attributes.

- **`projectiles.py`**: Contains predefined projectile type constants.
- **`rarities.py`**: Lists available rarity levels for brawlers.
- **`speeds.py`**: Offers predefined constants for brawler speeds.

### Example Usage

```python
from brawl_stars_brawler_maker import brawler_maker

# Define a new custom brawler
brawler = brawler_maker.Brawler(
    brawlername="ExampleBrawler",
    description="This is an example custom brawler.",
    rarity="epic",
    attack_name="Example Attack",
    # Additional parameters omitted for brevity...
)

# Generate game files for the custom brawler
brawler.generate_files()

# Export the modified game as an APK
brawler.export_csv_logic_to_apk()
```

This documentation provides an overview of the Brawl Stars Brawler Maker package's capabilities. By following the guidelines and examples provided, modders can create and share their unique brawlers within the Brawl Stars community, enhancing the game experience for themselves and others.