-- INSERTIONS --
INSERT IGNORE INTO World VALUES
(00001, "potatoes", "red", "1", "apple", "spring", "rainy", "2020-02-06 12:12:12"),
(00002, "wheresmycursor", "red", "1", "apple", "spring", "rainy", "2020-06-03 12:12:12"),
(00003, "hi vinny", "red", "1", "apple", "spring", "rainy", "2020-04-08 12:12:12"),
(00004, "Shhhhhhhh", "red", "1", "apple", "spring", "rainy", "2020-11-12 12:12:12"),
(00005, "hullo", "red", "1", "apple", "spring", "rainy", "2020-12-01 12:12:12");

INSERT IGNORE INTO Structure VALUES
(00001, "1"),
(00002, "1"),
(00003, "1"),
(00004, "2"),
(00005, "2"),
(00006, "2"),
(00007, "3"),
(00008, "3"),
(00009, "3");

INSERT IGNORE INTO Creature VALUES
(00001, "ABBA", true, "1", "2020-02-06 12:12:12", "winter"),
(00002, "spoop", false, "2", "2020-02-06 12:12:12", "spring"),
(00003, "mcflurdle", true, "3", "2020-02-06 12:12:12", "summer"),
(00004, "jaberwalk", false, "4", "2020-02-06 12:12:12", "fall"),
(00005, "slenderman", true, "5", "2020-02-06 12:12:12", "winter"),
(00006, "slenderman", true, "5", "2020-02-06 12:12:12", "spring"),
(00007, "slenderwoman", true, "5", "2020-02-06 12:12:12", "summer"),
(00008, "slenderchild", true, "5", "2020-02-06 12:12:12", "fall"),
(00009, "aliteralbean", true, "5", "2020-02-06 12:12:12", "winter"),
(00010, "extendedwarranty", true, "5", "2020-02-06 12:12:12", "spring"),
(00011, "skittle", true, "5", "2020-02-06 12:12:12", "summer"),
(00012, "johncena", true, "5", "2020-02-06 12:12:12", "fall");

INSERT IGNORE INTO Player VALUES
(00001, "meep", "2000-01-01", "brown", "brown", true),
(00002, "king arthur", "2017-08-01", "white", "blue", true),
(00003, "queen anne", "1999-12-12", "purple", "yellow", false),
(00004, "neil armstrong", "1969-07-21", "brown", "blue", true),
(00005, "bob", "2017-08-01", "green", "blue", false);

INSERT IGNORE INTO NPC VALUES
(00001, "jaxton"),
(00002, "patrick"),
(00003, "vinny"),
(00004, "becca"),
(00005, "jenna"),
(00006, "karen"),
(00007, "monique"),
(00008, "thomas"),
(00009, "peter"),
(00010, "james"),
(00011, "binary"),
(00012, "twee"),
(00013, "hash"),
(00014, "taybul"),
(00015, "link"),
(00016, "lizst");

INSERT IGNORE INTO Item VALUES
(00001, "frogchair", 200, 150),
(00002, "fancyfridge", 20, 10),
(00003, "bleakwall", 2020, 1010),
(00004, "playroomwall", 20005, 145),
(00005, "gardenwall", 20003, 150),
(00006, "classicfloor", 206, 150),
(00007, "slatetile", 564, 133),
(00008, "trashedfloor", 36346, 1334),
(00009, "heartcouch", 24643578, 178),
(00010, "violin", 667, 198),
(00011, "piano", 95, 14),
(00012, "shovel", 6757, 155),
(00013, "axe", 956, 190),
(00014, "net", 665, 190),
(00015, "orange", 97, 155),
(00016, "apple", 20, 188),
(00017, "cherry", 20, 17),
(00018, "classiclamp", 3633, 167),
(00019, "trashedlamp", 867, 177),
(00020, "gardenbench", 900, 199),
(00021, "townlamp", 245, 190),
(00022, "lawnmower", 278, 190),
(00023, "royalcrown", 47456, 190),
(00024, "jinglebells", 678, 190),
(00025, "believin", 879, 1),
(00026, "avengerstheme", 900, 123),
(00027, "dogobreakingmyheart", 450, 156);

INSERT IGNORE INTO Villager VALUES
(00001, "itsamemario", "jock", "male", "1968-10-11", "horse"),
(00002, "raymond", "snooty", "male", "2000-04-04", "cat"),
(00003, "jaxton", "normal", "male", "1998-04-04", "octopus"),
(00004, "kevin", "peppy", "male", "2000-04-04", "dog"),
(00005, "itsameluigi", "jock", "male", "1968-10-11", "horse"),
(00006, "prosten", "smug", "male", "2000-01-01", "bird"),
(00007, "halley", "peppy", "female", "2002-07-07", "octopus"),
(00008, "makus", "normal", "male", "2001-06-06", "cat");

INSERT IGNORE INTO Fish VALUES
(00001, 4.5, "2", "5", "pier"),
(00002, 7, "3", "2", "ocean"),
(00003, 2.5, "2", "5", "pier");

INSERT IGNORE INTO Bug VALUES
(00004, "2", "tree"),
(00005, "3", "treeStump"),
(00006, "5", "air");

INSERT IGNORE INTO Fossil VALUES
(00007, true),
(00008, false),
(00009, true);

INSERT IGNORE INTO Crustacean VALUES
(00010, "4"),
(00011, "2"),
(00012, "3");

INSERT IGNORE INTO Wallpaper VALUES
(00003, "red", false),
(00004, "blue", true),
(00005, "green", true);

INSERT IGNORE INTO Flooring VALUES
(00006, "red", false),
(00007, "blue", true),
(00008, "yellow", true);

INSERT IGNORE INTO Furniture VALUES
(00001, "red", "blue", "6", false),
(00002, "blue", "green", "4", true),
(00009, "yellow", "yellow", "2", true),
(00010, "red", "green", "6", false),
(00011, "blue", "red", "8", true),
(00018, "yellow", "red", "5", true),
(00019, "red", "green", "4", false),
(00020, "blue", "blue", "7", true),
(00021, "green", "blue", "5", true),
(00022, "blue", "blue", "7", true),
(00023, "yellow", "red", "9", true);

INSERT IGNORE INTO Music VALUES
(00024, "2:34", false),
(00025, "4:32", true),
(00026, "0:30", false),
(00027, "0:45", true);

INSERT IGNORE INTO Tool VALUES
(00012, 4, "shovel", "green", true),
(00013, 10, "axe", "red", false),
(00014, 25, "net", "blue", true);

INSERT IGNORE INTO Fruit VALUES
(00015, "orange"),
(00016, "apple"),
(00017, "cherry");

INSERT IGNORE INTO LivesOn VALUES
(00001, 00001),
(00002, 00002),
(00003, 00003),
(00004, 00004),
(00005, 00005);

INSERT IGNORE INTO HasVillager VALUES
(00001, 00001),
(00001, 00002),
(00001, 00008),
(00001, 00007),
(00002, 00002),
(00002, 00001),
(00002, 00006),
(00003, 00003),
(00003, 00005),
(00003, 00004),
(00004, 00004),
(00004, 00001),
(00004, 00002),
(00005, 00005),
(00005, 00008),
(00005, 00007);

INSERT IGNORE INTO HasStructure VALUES
(00001, 00004),
(00001, 00002),
(00001, 00008),
(00001, 00007),
(00002, 00002),
(00002, 00001),
(00002, 00006),
(00003, 00003),
(00003, 00005),
(00003, 00009),
(00004, 00009),
(00004, 00001),
(00004, 00002),
(00005, 00005),
(00005, 00008),
(00005, 00007);

INSERT IGNORE INTO HasCaught VALUES
(00001, 00004),
(00001, 00002),
(00001, 00008),
(00001, 00007),
(00002, 00002),
(00002, 00001),
(00002, 00006),
(00003, 00003),
(00003, 00005),
(00003, 00009),
(00004, 00009),
(00004, 00001),
(00004, 00002),
(00005, 00005),
(00005, 00008),
(00005, 00007),
(00001, 00012),
(00003, 00010),
(00002, 00011);

INSERT IGNORE INTO IsHolding VALUES
(00001, 00001),
(00002, 00002),
(00003, 00003),
(00004, 00004),
(00005, 00005),
(00001, 00006),
(00002, 00007),
(00003, 00008),
(00004, 00009),
(00005, 00010);

INSERT IGNORE INTO IsFriendsWith VALUES
(00001, 00001),
(00001, 00002),
(00001, 00008),
(00001, 00007),
(00002, 00002),
(00002, 00001),
(00002, 00006),
(00003, 00003),
(00003, 00005),
(00003, 00004),
(00004, 00004),
(00004, 00001),
(00004, 00002),
(00005, 00005),
(00005, 00008),
(00005, 00007);

INSERT IGNORE INTO HasDonated VALUES
(00001, 00001),
(00002, 00002),
(00003, 00003),
(00004, 00004),
(00005, 00005);