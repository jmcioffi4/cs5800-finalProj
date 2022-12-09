-- Functional Requirements:

-- Game Player
-- The Game Player must be able to see their player’s inventory
SELECT *
FROM IsHolding
WHERE playerID = 1;

-- The Game Player must be able to see a list of villagers that live in the player’s world
SELECT v.*
FROM Villager v
JOIN HasVillager h ON h.NPCID = v.NPCID
WHERE h.worldID = 2;

-- The Game Player must be able to see a list of creatures that they have caught
SELECT Creature.*
FROM HasCaught, Creature
WHERE HasCaught.playerId = 2
AND HasCaught.creatureID = Creature.creatureID;

-- The Game Player must be able to see a list of creatures that have been donated to their world
SELECT Creature.*
FROM Creature, Player, HasDonated, LivesOn
WHERE Player.playerID = 1
AND Player.playerID = LivesOn.playerID
AND LivesOn.WorldID = HasDonated.WorldId
AND Creature.CreatureID = HasDonated.creatureId;

-- The Game Player must be able to see details of their world
SELECT world.*
FROM World, LivesOn
WHERE LivesOn.playerId = 2
AND LivesOn.worldId = world.worldId;

-- The Game Player must be able to get a list of players that live on their world
SELECT playerID
FROM LivesOn
WHERE LivesOn.worldId = (SELECT worldId 
                         FROM LivesOn 
                         WHERE playerId = 2) 

-- Game Developer
-- The Game Developer must be able to see a list of any player’s inventory
SELECT *
FROM IsHolding
WHERE playerID = 2;

-- The Game Developer must be able to see a list of all villagers
SELECT *
FROM Villager;

-- The Game Developer must be able to see a full list of creatures
SELECT *
FROM Creature;

-- The Game Developer must be able to see a full list of fish
SELECT * 
FROM Fish;

-- The Game Developer must be able to see a full list of bugs
SELECT * 
FROM Bug;

-- The Game Developer must be able to see a full list of fossils
SELECT * 
FROM Fossil;

-- The Game Developer must be able to see a full list of crustaceans
SELECT * 
FROM Crustacean;

-- The Game Developer must be able to see details of any world
SELECT *
FROM World
WHERE worldID = 2;

-- The Game Developer must be able to get a full list of players
SELECT * 
FROM Player;

-- The Game Developer must be able to get a list of players that live on a specific world
SELECT playerID
FROM LivesOn
WHERE LivesOn.worldID = 2;