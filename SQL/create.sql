DROP DATABASE IF EXISTS theDBGame;
CREATE DATABASE IF NOT EXISTS theDBGame;

USE theDBGame;

-- CREATIONS --
CREATE TABLE IF NOT EXISTS World(
worldID int NOT NULL,
name varchar(20),
color enum("red", "blue", "green", "yellow"),
rating enum("1", "2", "3", "4", "5"),
fruit enum("apple", "peach", "cherry", "orange", "coconut"),
season enum("spring", "summer", "fall", "winter"),
weather enum("rainy","sunny", "cloudy", "foggy"),
timeOfDay timestamp,
CONSTRAINT pk_world PRIMARY KEY (worldID)
);

CREATE TABLE IF NOT EXISTS Structure(
structureID int NOT NULL,
developmentLevel enum("1", "2", "3"),
CONSTRAINT pk_structure PRIMARY KEY (structureID)
);

CREATE TABLE IF NOT EXISTS Creature(
creatureID int NOT NULL,
name varchar(20),
isDonated boolean,
rarity enum("1", "2", "3", "4", "5"),
timeOfDay timestamp,
season enum("spring", "summer", "fall", "winter"),
CONSTRAINT pk_creature PRIMARY KEY (creatureID)
);

CREATE TABLE IF NOT EXISTS Player(
playerID int NOT NULL,
name varchar(20),
birthday date,
hairColor varchar(20),
eyeColor varchar(20),
isWorldRep boolean,
CONSTRAINT pk_Player PRIMARY KEY (playerID)
);

CREATE TABLE IF NOT EXISTS NPC(
NPCID int NOT NULL,
name varchar(20),
CONSTRAINT pk_npc PRIMARY KEY (NPCID)
);

CREATE TABLE IF NOT EXISTS Item(
itemID int NOT NULL,
name varchar(20),
buyPrice int,
salePrice int,
CONSTRAINT pk_item PRIMARY KEY (itemID)
);

CREATE TABLE IF NOT EXISTS Villager(
NPCID int NOT NULL,
name varchar(20),
personality enum("lazy", "jock", "cranky", "smug", "normal", "peppy", "snooty", "big sister"),
gender enum("male", "female"),
birthday date,
species enum("cat", "dog", "horse", "octopus", "bird", "elephant"),
CONSTRAINT fk_NPC FOREIGN KEY (NPCID) REFERENCES NPC(NPCID)
);

CREATE TABLE IF NOT EXISTS Fish(
creatureID int NOT NULL,
size float,
shadowsize enum("1", "2", "3", "4", "5"),
difficulty enum("1", "2", "3", "4", "5"),
spawnPoint enum("pier", "ocean", "river", "inlet"),
CONSTRAINT fk_fish_creature FOREIGN KEY (creatureID) REFERENCES Creature(creatureID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Bug(
creatureID int NOT NULL,
speed enum("1", "2", "3", "4", "5"),
spawnpoint enum("tree", "treeStump", "ground", "air", "light", "trash"),
CONSTRAINT fk_bug_creature FOREIGN KEY (creatureID) REFERENCES Creature(creatureID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Fossil(
creatureID int NOT NULL,
isExamined boolean,
CONSTRAINT fk_fossil_creature FOREIGN KEY (creatureID) REFERENCES Creature(creatureID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Crustacean(
creatureID int NOT NULL,
speed enum("1", "2", "3", "4", "5"),
CONSTRAINT fk_crustacean_creature FOREIGN KEY (creatureID) REFERENCES Creature(creatureID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Wallpaper(
itemID int NOT NULL,
color enum ("red", "blue", "green", "yellow"),
isRare boolean,
CONSTRAINT fk_wallpaper_item FOREIGN KEY (itemID) REFERENCES Item(itemID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Flooring(
itemID int NOT NULL,
color enum("red", "blue", "green", "yellow"),
isRare boolean,
CONSTRAINT fk_flooring_item FOREIGN KEY (itemID) REFERENCES Item(itemID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Furniture(
itemID int NOT NULL,
color enum("red", "blue", "green", "yellow"),
materialColor enum("red", "blue", "green", "yellow"),
space enum("1", "2", "3", "4", "5", "6", "7", "8", "9"),
isCraftable boolean,
CONSTRAINT fk_furniture_item FOREIGN KEY (itemID) REFERENCES Item(itemID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Music(
itemID int NOT NULL,
length varchar(4),
isSecret boolean,
CONSTRAINT fk_music_item FOREIGN KEY (itemID) REFERENCES Item(itemID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Tool(
itemID int NOT NULL,
durability int,
type enum("axe", "pole", "ladder", "wand", "fishingRod", "shovel", "net", "wateringCan", "ballon", "sparkler", "umbrella", "fan"),
color enum( "red", "blue", "green", "yellow"),
isBreakable boolean,
CONSTRAINT fk_tool_item FOREIGN KEY (itemID) REFERENCES Item(itemID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Fruit(
itemID int NOT NULL,
fruitType enum("apple", "peach", "cherry", "orange", "coconut" ),
CONSTRAINT fk_fruit_item FOREIGN KEY (itemID) REFERENCES Item(itemID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS LivesOn(
playerID int NOT NULL,
worldID int NOT NULL,
CONSTRAINT fk_liveson_player FOREIGN KEY (playerID) REFERENCES Player(playerID),
CONSTRAINT fk_liveson_world FOREIGN KEY (worldID) REFERENCES World(worldID)
);

CREATE TABLE IF NOT EXISTS HasVillager(
worldID int NOT NULL,
NPCID int NOT NULL,
CONSTRAINT fk_hasvillager_world FOREIGN KEY (worldID) REFERENCES World(worldID),
CONSTRAINT fk_hasvillager_villager FOREIGN KEY (NPCID) REFERENCES Villager(NPCID)
);

CREATE TABLE IF NOT EXISTS HasStructure(
worldID int NOT NULL,
structureID int NOT NULL,
CONSTRAINT fk_hasstructure_world FOREIGN KEY (worldID) REFERENCES World(worldID),
CONSTRAINT fk_hasstructure_structure FOREIGN KEY (structureID) REFERENCES structure(structureID)
);

CREATE TABLE IF NOT EXISTS HasCaught(
playerID int NOT NULL,
creatureID int NOT NULL,
CONSTRAINT fk_hascaught_player FOREIGN KEY (playerID) REFERENCES Player(playerID),
CONSTRAINT fk_hascaught_creature FOREIGN KEY (creatureID) REFERENCES Creature(creatureID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS IsHolding(
playerID int NOT NULL,
itemID int NOT NULL,
CONSTRAINT fk_isholding_player FOREIGN KEY (playerID) REFERENCES Player(playerID),
CONSTRAINT fk_isholding_item FOREIGN KEY (itemID) REFERENCES Item(itemID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS IsFriendsWith(
playerID int NOT NULL,
NPCID int NOT NULL,
CONSTRAINT fk_isfriendswith_player FOREIGN KEY (playerID) REFERENCES Player(playerID),
CONSTRAINT fk_isfriendswith_villager FOREIGN KEY (NPCID) REFERENCES Villager(NPCID)
);

CREATE TABLE IF NOT EXISTS HasDonated(
creatureID int NOT NULL,
worldID int NOT NULL,
CONSTRAINT fk_hasdonated_creature FOREIGN KEY (creatureID) REFERENCES Creature(creatureID) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT fk_hasdonated_world FOREIGN KEY (worldID) REFERENCES World(worldID)
);