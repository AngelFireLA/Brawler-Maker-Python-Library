import csv
import os
import random
from zipfile import ZipFile
import shutil
import apk_signer
from mega import Mega

mega = Mega()

brawler_names_list = ['shelly', 'colt', 'bull', 'brock', 'rico', 'spike', 'barley', 'jessie', 'nita', 'dynamike',
                      'el_primo', 'mortis', 'crow', 'poco', 'bo', 'piper', 'pam', 'tara', 'darryl', 'penny', 'frank',
                      'gene', 'tick', 'leon', 'rosa', 'carl', 'bibi', 'eight_bit', 'sandy', 'bea', 'emz', 'mister_p',
                      'max', 'jacky', 'gale', 'nani', 'sprout', 'surge', 'colette']

projectiles_dict = {
    "shelly main attack": "ShotgunGirlProjectile",
    "colt main attack": "GunslingerProjectile",
    "bull main attack": "BullDudeProjectile",
    "brock main attack": "RocketGirlProjectile",
    "rico main attack": "TrickshotDudeProjectile",
    "spike main attack": "CactusProjectile",
    "barley main attack": "BarkeepProjectile",
    "jessie main attack": "MechanicProjectile1",
    "nita main attack": "ShamanProjectile",
    "dynamike main attack": "TntDudeProjectile",
    "el_primo main attack": "PrimoDefProjectile",
    "crow main attack": "CrowProjectile",
    "poco main attack": "DeadMariachiProjectile",
    "bo main attack": "BowDudeProjectile",
    "piper main attack": "SniperProjectile",
    "pam main attack": "MinigunDudeProjectile",
    "tara main attack": "BlackHoleProjectile",
    "darryl main attack": "BarrelBotProjectile",
    "penny main attack": "ArtilleryDudeProjectile",
    "frank main attack": "HammerDudeProjectile",
    "gene main attack": "HookProjectile",
    "tick main attack": "ClusterBombProjectile",
    "leon main attack": "LeonDefProjectile",
    "rosa main attack": "RosaProjectile",
    "carl main attack": "WhirlwindProjectile",
    "eight_bit main attack": "ArcadeProjectile",
    "sandy main attack": "SandstormProjectile",
    "bea main attack": "BeeSniperProjectile",
    "emz main attack": "MummyProjectile",
    "mister_p main attack": "SpawnerDudeProjectile",
    "max main attack": "SpeedyProjectile",
    "gale main attack": "BlowerProjectile",
    "nani main attack": "ControllerProjectile",
    "sprout main attack": "WallyProjectile",
    "surge main attack": "PowerLevelerProjectile",
    "colette main attack": "PercenterProjectile",
    "shelly super": "ShotgunGirlUltiProjectile",
    "colt super": "GunslingerUltiProjectile",
    "brock super": "RocketGirlUltiProjectile",
    "rico super": "TrickshotDudeUltiProjectile",
    "spike super": "CactusUltiProjectile",
    "barley super": "BarkeepUltiProjectile",
    "dynamike super": "TntDudeUltiProjectile",
    "mortis super": "UndertakerUltiProjectile",
    "poco super": "DeadMariachiUltiProjectile",
    "tara super": "BlackHoleUltiProjectile",
    "frank super": "HammerDudeUltiProjectile",
    "gene super": "HookDudeProjectile",
    "tick super": "ClusterBombSummonProjectile",
    "bibi super": "BaseballUltiProjectile",
    "sandy super": "SandstormUltiProjectile",
    "bea super": "BeeSniperUltiProjectile",
    "gale super": "BlowerUltiProjectile",
    "nani super": "ControllerUltiProjectile",
    "sprout super": "WallyUltiProjectile",
}

rarity_list = ["rare", "common", "epic", "super_rare", "mega_epic", "legendary"]
default_apk_name = "BrawlStarsOfflineV29"


class Brawler:
    def __init__(self, brawlername, description, rarity,
                 attack_name, attack_description, ulti_name,
                 ulti_description, speed, hp, icon, range,
                 reloadtime, ammonumber,
                 damage, spread, numberofprojectiles, projectile, ulti_projectile, ulti_damage, ulti_spread, ulti_numberofprojectiles, ulti_range):
        self.brawlername = brawlername
        self.capbrawlername = brawlername.upper()
        self.description = description
        self.rarity = rarity
        self.attack_name = attack_name
        self.attack_description = attack_description
        self.ulti_name = ulti_name
        self.ulti_description = ulti_description
        self.speed = speed
        self.hp = hp
        self.icon = icon
        self.range = range
        self.reloadtime = reloadtime
        self.ammonumber = ammonumber
        self.damage = damage
        self.spread = spread
        self.numberofprojectiles = numberofprojectiles
        self.projectile = projectile
        self.ulti_projectile = ulti_projectile
        self.ulti_damage = ulti_damage
        self.ulti_spread = ulti_spread
        self.ulti_numberofprojectiles = ulti_numberofprojectiles
        self.ulti_range = ulti_range


        try:
            if self.rarity not in rarity_list:
                raise ValueError(
                    f"Invalid rarity, please select a rarity from this list : {rarity_list} or select the rarity of your choice using brawl_stars_brawler_maker.rarities.RARITY_OF_YOUR_CHOICE")
            if self.icon not in brawler_names_list:
                raise ValueError(f"Invalid icon name, list of valid icons : {brawler_names_list}")
            if self.projectile not in list(projectiles_dict.values()):
                raise ValueError(
                    f"Invalid projectile for attack, please select a projectile from this list : {list(projectiles_dict.values())} or select more easly the projectile of your choice using brawl_stars_brawler_maker.projectiles.PROJECTILE_OF_YOUR_CHOICE")
            if self.ulti_projectile not in list(projectiles_dict.values()):
                raise ValueError(
                    f"Invalid projectile for SUPER, please select a projectile from this list : {list(projectiles_dict.values())} or select more easly the projectile of your choice using brawl_stars_brawler_maker.projectiles.PROJECTILE_OF_YOUR_CHOICE")
            if not 0 < int(self.speed) <= 9999:
                raise ValueError(f"Invalid speed, please select a speed value between 0 and 9999")
            if not 0 < int(self.hp) <= 39999:
                raise ValueError(f"Invalid hp, please select a hp value between 0 and 39999")
            if not 0 < int(self.range) <= 9999:
                raise ValueError(f"Invalid range, please select a range value between 0 and 9999")
            if not 0 < int(reloadtime) <= 9999:
                raise ValueError(f"Invalid reload time, please select a reload time value between 0 and 9999")
            if not 0 < int(self.ammonumber) <= 30:
                raise ValueError(f"Invalid ammo number, please select an ammo number value between 0 and 30")
            if not 0 <= int(self.spread) <= 999:
                raise ValueError(f"Invalid spread, please select a spread value between 0 and 999")
            if not 0 < int(self.numberofprojectiles) <= 999:
                raise ValueError(
                    f"Invalid number of projectiles, please select a number of projectiles value between 0 and 999")
            if not 0 < self.ulti_range <= 9999:
                raise ValueError(f"Invalid super range, please select a super range value between 0 and 9999")
            if not 0 <= int(self.ulti_spread) <= 999:
                raise ValueError(f"Invalid super spread, please select a spread value between 0 and 999")
            if not 0 < int(self.ulti_numberofprojectiles) <= 999:
                raise ValueError(
                    f"Invalid number of projectiles, please select a number of projectiles value between 0 and 999")
        except ValueError as e:
            print("An Error as occured, please verify that all your values are correct :")
            print(e)
            exit()

    def generate_files(self, csv_logic_folder_path=None, localization_folder_path=None, directly_modify=False, warning=True, debug=True):
        """
        Modify the csv files to add the brawlers
        :param csv_logic_folder_path: the path for the csv_logic folder whose file you want to modify, will use BS V29's files if not specified
        :param localization_folder_path: the path for the localization folder whose file you want to modify, will use BS V29's files if not specified
        :param directly_modify: Set to true if you want the script to directly modify the csv files instead of duplicating them first
        :param warning: If directly_modify is activated, will show a warning message before modifying the csv files
        :param debug: if you want to see messages in the console
        :return:
        """
        print("Starting file generation")
        print()

        # Default paths within the package
        package_directory = os.path.dirname(os.path.abspath(__file__))  # Gets the directory where the script is located
        default_csv_logic_path = os.path.join(package_directory, "default_files", "default_files/csv_logic")
        default_localization_path = os.path.join(package_directory, "default_files", "default_files/localization")

        # Use default paths if none provided
        if csv_logic_folder_path is None:
            csv_logic_folder_path = default_csv_logic_path
            if debug: print(f"Using default csv_logic folder at {csv_logic_folder_path}")
        if localization_folder_path is None:
            localization_folder_path = default_localization_path
            if debug: print(f"Using default localization folder at {localization_folder_path}")

        if directly_modify and warning:
            input(
                "Warning, this will modify directly your files, if you want to make a backup please stop this script, otherwise press enter to continue")
        else:
            current_folder = os.getcwd()
            #duplicates csv_logic folder
            if os.path.exists(os.path.join(current_folder, 'default_files/csv_logic')):
                raise FileExistsError(
                    "A csv_logic folder already exists in this folder, please delete it or choose another folder")
            shutil.copytree(os.path.join(current_folder, "default_files/csv_logic"), csv_logic_folder_path)
            csv_logic_folder_path = os.path.join(current_folder, "default_files/csv_logic")
            if debug: print("successfully duplicated target csv_logic folder to current folder")

            #duplicates localization folder
            if os.path.exists(os.path.join(current_folder, 'default_files/localization')):
                raise FileExistsError(
                    "A localization folder already exists in this folder, please delete it or choose another folder")
            shutil.copytree(os.path.join(current_folder, "default_files/localization"), localization_folder_path)
            localization_folder_path = os.path.join(current_folder, "default_files/localization")
            if debug: print("successfully duplicated target localization folder to current folder")


        filename = os.path.join(localization_folder_path, 'texts.csv')
        with open(filename, 'a', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([''])
            csv_writer.writerow(['TID_' + self.capbrawlername, self.brawlername])
            csv_writer.writerow(['TID_' + self.capbrawlername + '_DESC', self.description])
            csv_writer.writerow(['TID_' + self.capbrawlername + '_WEAPON', self.attack_name])
            csv_writer.writerow(['TID_' + self.capbrawlername + '_WEAPON_DESC', self.attack_description])
            csv_writer.writerow(['TID_' + self.capbrawlername + '_ULTI', self.ulti_name])
            csv_writer.writerow(['TID_' + self.capbrawlername + '_ULTI_DESC', self.ulti_description])
        if debug: print("Done modifying texts.csv")

        filename = os.path.join(csv_logic_folder_path, 'cards.csv')
        brawlernumber = random.randint(1500, 9999)
        with open(filename, 'a', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(
                ['', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', '', ''])
            csv_writer.writerow(
                [self.brawlername + '_unlock', 'sc/ui.sc', '', self.brawlername, '', '', '0', '', 'unlock', '',
                 '',
                 '', '', self.rarity,
                 '', '', '', '', '', '', brawlernumber, ''])
            csv_writer.writerow(
                [self.brawlername + '_hp', 'sc/ui.sc', 'health_icon', self.brawlername, '', '', '1', '', 'hp', '',
                 '',
                 '', '',
                 'common', 'TID_ARMOR', 'TID_ARMOR', '', '', 'genicon_health', '', '', ''])
            csv_writer.writerow(
                [self.brawlername + '_abi', 'sc/ui.sc', 'attack_icon', self.brawlername, '', '', '2', '', 'skill',
                 self.brawlername + 'Weapon', '', '', '', 'common', 'TID_' + self.capbrawlername + '_WEAPON',
                 'TID_STAT_DAMAGE', '', '', 'genicon_damage', '', '', ''])
            csv_writer.writerow(
                [self.brawlername + '_ulti', 'sc/ui.sc', 'ulti_icon', self.brawlername, '', '', '3', '', 'skill',
                 self.brawlername + 'Ulti', '', '', '', 'common', 'TID_' + self.capbrawlername + '_ULTI',
                 'TID_STAT_DAMAGE', '', '', 'genicon_damage', '', '', ''])
        if debug: print("Done modifying cards.csv")

        ultichargemul = random.randint(90, 150)
        ultichargeultimul = random.randint(90, 150)

        filename = os.path.join(csv_logic_folder_path, 'characters.csv')
        with open(filename, 'a', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([''])
            csv_writer.writerow(
                [self.brawlername, '', '', 'bull', self.brawlername + 'Weapon', self.brawlername + 'Ulti', '',
                 self.speed, self.hp, '', '', '', '',
                 '', '', '', '12', '', ultichargemul, ultichargeultimul, "Hero", '', self.brawlername + 'Default',
                 '',
                 '', '',
                 '', '', '', 'takedamage_gen', 'death_shotgun_girl', 'Gen_move_fx', 'reload_shotgun_girl',
                 'No_ammo_shotgungirl', 'Dry_fire_shotgungirl', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '',
                 '', '', '30', '', '80', '80', '', '', '35', '116', '210', '284', '90', '175', '260', '', '', '', '-25',
                 '40', '120', 'Medium', '-48', '', '450', '', '', 'TID_' + self.capbrawlername, '', 'sc/ui.sc',
                 'hero_icon_' + self.icon, '0', 'human', 'footstep', '25', '250', '200', '', '', '1', '3', '2', '', '',
                 '',
                 '',
                 '', '', '', '', '', 'ShellyTutorial', '', '', '', '', '', '3', '3', '3'])

        if debug: print("Done modifying characters.csv")

        filename = os.path.join(csv_logic_folder_path, 'skins.csv')
        with open(filename, 'a', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([''])
            csv_writer.writerow(
                [self.brawlername + 'Default', self.brawlername + 'Default', '', '', '', '', '', '', '', '', '',
                 '',
                 '', '', '',
                 'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr', 'shelly_v2_01.pvr'])
        filename = os.path.join(csv_logic_folder_path, 'skin_confs.csv')
        with open(filename, 'a', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([''])
            csv_writer.writerow(
                [self.brawlername + 'Default', self.brawlername, 'shelly_geo.scw', '', '', 'shelly_base_cam.scw',
                 'shelly_intro_pose.scw',
                 '', 'ShellyIdle', 'ShellyWalk', 'ShellyPrimary', 'ShellySecondary', 'ShellyRecoil', '', 'ShellyRecoil',
                 '',
                 'ShellyReload', 'ShellyPushback', 'ShellyWin', 'ShellyWinloop', 'ShellyLose', 'ShellyLoseloop',
                 'ShellyIdle',
                 'ShellyWin', 'ShellyWinloop', 'ShellyWin', 'ShellyIdle', 'ShellyIdle', 'ShellyProfile', 'ShellyIntro',
                 '',
                 '',
                 '', '', '', 'ShellyFace', 'ShellyFace', 'ShellyHappy', 'ShellyFace', 'ShellySad', 'ShellySadLoop',
                 'ShellyFace', 'ShellyHappy', 'ShellyFace', 'ShellyHappy', 'ShellyStill', 'ShellyStill', '', '', '',
                 'true',
                 'true', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '',
                 '',
                 '', '', '', '', '', ', '', ', '', '', '', ''])
        if debug: print("Done modifying skins.csv and skin_confs.csv")

        filename = os.path.join(csv_logic_folder_path, 'skills.csv')
        with open(filename, 'a', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([''])
            csv_writer.writerow(
                [self.brawlername + "Weapon", 'Attack', 'true', 'true', 'true', '', '50', '150', '',
                 self.range, '', '',
                 '', '', self.reloadtime, self.ammonumber, self.damage, '', '50',
                 self.spread, '', self.numberofprojectiles, '',
                 'true', '', '', '', '', '', '', '', '', self.projectile, '', '', '', '', '', '', '', '',
                 'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])
        with open(filename, 'a', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([''])
            csv_writer.writerow(
                [self.brawlername + "Ulti", 'Attack', 'true', 'true', 'true', '', '50', '150', '',
                 self.range, '', '',
                 '', '', '', '', self.damage, '', '50', self.spread, '',
                 self.numberofprojectiles, '',
                 'true', '', '', '', '', '', '', '', '', self.ulti_projectile, '', '', '', '', '', '', '', '',
                 'sc/ui.sc', 'rapid_fire_button', 'rico_def_atk', '', '', '', '', '', '', '', '', '', '', '', ''])
        if debug: print("Done modifying skills.csv.csv")
        print()
        print("Done generating the csv files !")

    @staticmethod
    def export_csv_logic_to_apk(csv_logic_folder_path=None, localization_folder_path=None, destination_folder=None, apk_mega_link="https://mega.nz/file/cANAhBya#8wFHevhnng_a09IMWPet9BihJaJd3nLDHaEhGqgmIM4", existing_apk_path=None, sign=False, debug=True):
        """
        :param csv_logic_folder_path: the path of the csv_logic folder you want to make the apk from
        :param localization_folder_path: the path of the localization folder you want to make the apk from
        :param destination_folder: the path of the folder where you want the apk to be generated
        :param apk_mega_link: if you have a custom base apk, otherwise don't change the value if possible
        :param existing_apk_path: path of an existing apk if you already have the apk download
        :param sign: if you want to sign the apk, let it to False by default if you don't have java installed
        :param debug: If you want to see messages in the console
        :return:
        """
        print("Starting APK export")
        if existing_apk_path is not None:
            apk_name = os.path.basename(existing_apk_path).replace('.apk', '')
        else:
            apk_name = default_apk_name
        if debug: print("No csv_logic folder specified, assuming it's inside the current folder")
        if csv_logic_folder_path is None:
            csv_logic_folder_path = os.path.join(os.getcwd(), "default_files/csv_logic")
        if not os.path.exists(csv_logic_folder_path):
            raise FileNotFoundError("csv_logic folder not found")

        if debug: print("No localization folder specified, assuming it's inside the current folder")
        if localization_folder_path is None:
            localization_folder_path = os.path.join(os.getcwd(), "default_files/localization")
        if not os.path.exists(localization_folder_path):
            raise FileNotFoundError("localization folder not found")

        if debug: print("No destination folder specified, exporting to the current folder")
        if destination_folder is None:
            destination_folder = os.getcwd()

        if not os.path.exists(destination_folder+f"/{apk_name}.apk") and existing_apk_path is None:
            try:
                if debug: print("Starting to download APK")
                mega.download_url(apk_mega_link, dest_filename=f"{apk_name}.apk",
                                  dest_path=destination_folder)

            except PermissionError:
                pass
            if debug: print("Finish downloading APK")
        if debug: print("Copying APK into ZIP...")
        if existing_apk_path is None:
            shutil.copy(os.path.join(destination_folder, apk_name + ".apk"), os.path.join(destination_folder, apk_name + ".zip"))
        else:
            shutil.copy(existing_apk_path, os.path.join(destination_folder, apk_name + ".zip"))
        if debug: print("Done copying APK into ZIP")
        if os.path.exists(os.path.join(destination_folder, apk_name + "/assets/csv_logic")):
            if debug: print("Found existing apk folder, removing it...")
            shutil.rmtree(os.path.join(destination_folder, apk_name))
            if debug: print("Done removing existing apk folder")
        if debug: print("Extracting ZIP into folder...")
        with ZipFile(apk_name + ".zip", 'r') as zipp:
            zipp.extractall(os.path.join(destination_folder, apk_name))
            if debug: print("Done extracting ZIP into folder")

        zipp.close()
        if debug: print("Deleting obsolete ZIP")
        os.remove(apk_name + ".zip")
        if debug: print("Done deleting obsolete ZIP")
        if debug: print("Copying CSV logic files...")
        try:
            for file in os.listdir(csv_logic_folder_path):
                shutil.copy(os.path.join(csv_logic_folder_path, file), os.path.join(destination_folder, apk_name, "assets/csv_logic", file))
        except PermissionError:
            raise PermissionError("File Permission Error : couldn't transfer the csv files to the apk.")

        if os.path.exists(os.path.join(destination_folder, apk_name + " - Brawler Maker" + ".zip")):
            if debug: print("Found existing resulting zip, removing it...")
            os.remove(os.path.join(destination_folder, apk_name + " - Brawler Maker" + ".zip"))
            if debug: print("Done removing existing resulting zip")

        if debug: print("Creating resulting zip...")
        shutil.make_archive(os.path.join(destination_folder, apk_name + " - Brawler Maker"), "zip",
                            os.path.join(destination_folder, apk_name))
        if debug: print("Done creating resulting zip")
        if debug: print("Renaming resulting zip to apk...")
        os.rename(os.path.join(destination_folder, apk_name + " - Brawler Maker" + ".zip"),
                  apk_name.replace(' ', '-') + "-BrawlerMaker" + ".apk")
        if debug: print("Done renaming resulting zip to apk")
        if debug: print("Deleting obsolete folder...")
        shutil.rmtree(os.path.join(destination_folder, apk_name))
        if debug: print("Done deleting obsolete folder")
        if sign:
            if debug: print("Signing apk...")
            apk_signer.sign_apk(os.path.join(destination_folder, apk_name + "-BrawlerMaker.apk"))
            if debug: print("Done signing apk")
            if debug: print("Deleting unsigned apk...")
            os.remove(os.path.join(destination_folder, apk_name+"-BrawlerMaker.apk"))
            if debug: print("Done deleting unsigned apk")
        print("Done exporting csv logic to apk")