# TOTAL_CHARACTERS: How many total Characters are there?
total_characters = """ SELECT COUNT(DISTINCT name) 
                           FROM charactercreator_character; """

# TOTAL_SUBCLASS: How many of each specific subclass?
total_subclass = """ SELECT 
                     (SELECT COUNT(DISTINCT character_ptr_id) 
                         FROM charactercreator_cleric) AS clerics,
                     (SELECT COUNT(DISTINCT character_ptr_id) 
                         FROM charactercreator_fighter) AS fighters,
                     (SELECT COUNT(DISTINCT character_ptr_id) 
                         FROM charactercreator_mage) AS mages,
                     (SELECT COUNT(DISTINCT character_ptr_id) 
                         FROM charactercreator_thief) AS thieves,
                     (SELECT COUNT(DISTINCT mage_ptr_id) 
                         FROM charactercreator_necromancer) AS necromancers; """

# TOTAL_ITEMS: How many total Items?
total_items = """ SELECT COUNT(DISTINCT name)
                      FROM armory_item; """

# WEAPONS: How many of the Items are weapons?
weapons = """ SELECT COUNT(DISTINCT item_ptr_id)
                  FROM armory_weapon; """

# NON_WEAPONS: How many of the items are not weapons?
non_weapons = """ SELECT COUNT(DISTINCT item_id) FROM armory_item
                      WHERE item_id NOT IN (SELECT item_ptr_id 
                          FROM armory_weapon);"""

# CHARACTER_ITEMS: How many Items does each character have? 
#                  (Return first 20 rows)
character_items = """ SELECT character_id, 
                          COUNT(DISTINCT item_id) AS total_items
                      FROM charactercreator_character_inventory
                      GROUP BY character_id
                      ORDER BY character_id
                      LIMIT 20; """

# CHARACTER_WEAPONS: How many Weapons does each character have? 
#                  (Return first 20 rows)
character_weapons = """ SELECT character_id, 
                            COUNT(DISTINCT item_id) AS total_weapons
                        FROM charactercreator_character_inventory
                        WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
                        GROUP BY character_id
                        ORDER BY character_id
                        LIMIT 20; """

# AVG_CHARACTER_ITEMS: On average, how many Items does each Character have?
AVG_CHARACTER_ITEMS = """ SELECT avg(total_items)
                          FROM (SELECT character_id, COUNT(DISTINCT item_id) 
                                    AS total_items
                                FROM charactercreator_character_inventory
                                GROUP BY character_id); """

# AVG_CHARACTER_WEAPONS: On average, how many Weapons does each character have?
AVG_CHARACTER_WEAPONS = """ SELECT avg(total_weapons)
                            FROM (SELECT character_id, COUNT(DISTINCT item_id)
                                      AS total_weapons
                                  FROM charactercreator_character_inventory
                                  WHERE item_id IN (SELECT item_ptr_id 
                                      FROM armory_weapon)
                                  GROUP BY character_id); """ 