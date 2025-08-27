from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class MonsterHunterWildsArchipelagoOptions:
    monster_hunter_wilds_include_Hard_Hunts: MonsterHunterWildsIncludeHardHunts

class MonsterHunterWildsGame(Game):
    name = "MONSTER HUNTER WILDS"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = MonsterHunterWildsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Hunt High Rank Version of a Monster",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label = "Use an Enviromental Trap against a Monster",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label = "Can only eat a Meal close to a Large Monster",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label = "Hunt a Monster Solo",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label = "Hunt a Monster Primarily using an Artian Weapon",
                data= dict(),
            ),
            GameObjectiveTemplate(
                label = "Complete a Hunt without the use of Healing Items",
                data = dict(),
            )
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label = "Hunt a MONSTER",
                data = {
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Hunt any Large Monster at the LOCATION",
                data = {
                    "LOCATION": (self.locations, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 4,
            ),
            GameObjectiveTemplate(
                label = "Hunt a Tempered MONSTER",
                data = {
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3,
            ),
            GameObjectiveTemplate(
                label = "Capture a MONSTER",
                data = {
                    "MONSTER": (self.monsters, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight = 3,
            ),
            GameObjectiveTemplate(
                label = "Carve the following tail: TAIL",
                data= {
                    "TAIL": (self.tails, 1)

                },
                is_time_consuming=False,
                is_difficult=False,
                weight = 3,
            ),
            GameObjectiveTemplate(
                label = "Power Clash with a PCMONSTER then slay or capture it",
                data = {
                    "PCMONSTER": (self.pcmonsters, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label = "Inflict 3 Wounds on a MONSTER then slay or capture it",
                data = {
                    "MONSTER": (self.monsters, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
        ]
        
        if self.include_hard_monsters:
         templates.append(
         GameObjectiveTemplate(
            label = "Hunt a HARDMONSTER",
            data = {
                "HARDMONSTER": (self.hardMonsters, 1),
            },
                is_time_consuming = False,
                is_difficult = True,
                weight = 4,
            ),
         ),
         templates.append(
         GameObjectiveTemplate(
            label = "Carve the following tail: HARDTAIL",
            data = {
                    "HARDTAIL": (self.hardTails, 1)
            },
                is_time_consuming=False,
                is_difficult=True,
                weight = 3,
            ),
        ),
        templates.append(
        GameObjectiveTemplate(
            label = "Power Clash with a HPCMONSTER then slay or capture it",
            data = {
                "HPCMONSTER": (self.hpcmonsters, 1)
            },
                is_time_consuming=False,
                is_difficult=True,
                weight = 2,
            ),
        ),
        templates.append(
        GameObjectiveTemplate(
            label = "Complete a Multi-Monster Hunt at the LOCATION",
            data = {
                "LOCATION": (self.locations, 1)
            },
                is_time_consuming=True,
                is_difficult=True,
                weight = 2,
            ),
        ),
                
        return templates
    
    @property
    def include_hard_monsters(self) -> bool:
        return bool(self.archipelago_options.monster_hunter_wilds_include_Hard_Hunts.value)
    
    @staticmethod
    def monsters() -> List[str]:
        return [
            "Ajarakan",
            "Balahara",
            "Blangonga",
            "Chatacabra",
            "Congalala",
            "Doshaguma",
            "Gravios",
            "Guardian Doshaguma",
            "Guardian Ebony Odogaron",
            "Guardian Fulgur Anjanath",
            "Guardian Rathalos",
            "Gypceros",
            "Hirabami",
            "Lala Barina",
            "Mizutsune",
            "Nerscylla",
            "Quematrice",
            "Rathalos",
            "Rathian",
            "Rompopolo",
            "Xu Wu",
            "Yian Kut-Ku",
        ]
    
    #Power Clash Monsters
    @staticmethod
    def pcmonsters() -> List[str]:
        return[
            "Ajarakan",
            "Blangonga",
            "Chatacabra",
            "Doshaguma",
            "Guardian Doshaguma",
            "Guardian Ebony Odogaron",
            "Xu Wu",
        ]
    
    #Hard Power Clash Monsters
    @staticmethod
    def hpcmonsters() -> List[str]:
        return[
            "Arkveld",
            "Uth Duna",
            "Seregios",
            "Lagiacrus",
        ]

    @staticmethod
    def hardMonsters() -> list[str]:
        return[
            "Arch-Tempered Uth Duna",
            "Tempered Uth Duna",
            "Tempered Rey Dau",
            "Arch-Tempered Rey Dau",
            "Tempered Nu Udra",
            "Tempered Jin Dahaad",
            "Tempered Gore Magala",
            "Tempered Lagiacrus",
            "Tempered Seregios",
            "Tempered Arkveld",
            "Zoh Shia",
            #"Omega Planettes", ~Impliment when released~
        ]
    
    @staticmethod
    def locations() -> list[str]:
        return[
            "Windward Plains",
            "Scarlet Forest",
            "Oilwell Basin",
            "Iceshard Cliffs",
            "Ruins of Wyveria",
            "Wounded Hollow",
        ]
    
    @staticmethod
    def tails() -> List [str]:
        return[
            "Balahara Tail",
            "Blangonga Tail",
            "Guardian Ebony Tail",
            "Guardian Fulgur Tail",
            "Guardian Rathalos Tail",
            "Gypceros Tail",
            "Mizutsune Tail",
            "Quematrice Tail",
            "Rathalos Tail",
            "Rathian Tail",
            "Xu Wu Tentacle",
        ]
    @staticmethod
    def hardTails() -> List[str]:
        return[
            "Arkveld Tail",
            "Gore Magala Tail",
            "Jin Dahaad Tail",
            "Lagiacrus Tail",
            "Nu Udra Tentacle",
            "Rey Dau Tail",
            "Zoh Shia Cystaltail",

        ]

class MonsterHunterWildsIncludeHardHunts(Toggle):
    """
    Indicates whether to include harder hunts and tasks
    """

    display_name = "Monster Hunter Wilds Include Hard Hunts"
