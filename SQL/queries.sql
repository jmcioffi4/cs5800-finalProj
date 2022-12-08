-- Functional Requirements:

-- Game Player
-- The Game Player must be able to see their player’s inventory
SELECT *
FROM IsHolding
WHERE playerID = {playerID}

-- The Game Player must be able to see a list of villagers that live in the player’s world
SELECT v.*
FROM Villager v
JOIN hasVillager h ON h.NPCID = v.NPCID
WHERE h.worldID = {worldID};

-- The Game Player must be able to see a list of creatures that they have caught
SELECT creature.*
FROM hasCaught, creature
WHERE hasCaught.playerId = {playerID}
AND hasCaught.creatureID = creature.creatureID;

-- The Game Player must be able to see a list of creatures that have been donated to their world

SELECT creature.*
FROM creature, player, hasDonated, livesOn
WHERE player.playerID = {playerID}
AND player.playerID = livesOn.playerID
AND livesOn.WorldID = hasDonated.WorldId
AND creature.CreatureID = HasDonated.creatureId;


-- The Game Player must be able to see details of their world
SELECT world.*
FROM world, livesOn
WHERE livesOn.playerId = {playerID}
AND livesOn.worldId = world.worldId;

-- The Game Player must be able to get a list of players that live on their world
SELECT playerID
FROM livesOn
WHERE livesOn.worldId = (SELECT worldId 
                         FROM livesOn 
                         WHERE playerId = CURRENTPLAYERID) 

-- Game Developer
-- The Game Developer must be able to see a list of any player’s inventory
SELECT *
FROM IsHolding
WHERE playerID = {playerID}

-- The Game Developer must be able to see a list of all villagers
SELECT *
FROM villager;

-- The Game Developer must be able to see a full list of creatures
SELECT *
FROM creature;

-- The Game Developer must be able to see a full list of fish
SELECT * 
FROM fish;

-- The Game Developer must be able to see a full list of bugs
SELECT * 
FROM Bug;

-- The Game Developer must be able to see a full list of fossils
SELECT * 
FROM fossil;

-- The Game Developer must be able to see a full list of crustaceans
SELECT * 
FROM Crustacean;

-- The Game Developer must be able to see details of any world
SELECT *
FROM world
WHERE worldID = {worldID};

-- The Game Developer must be able to get a full list of players
SELECT * 
FROM player;

-- The Game Developer must be able to get a list of players that live on a specific world
SELECT playerID
FROM livesOn
WHERE liveson.worldID = {worldID};