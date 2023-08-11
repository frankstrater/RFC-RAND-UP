# Rhye's and Fall of Civilization RAND

```
Updated to v1.27
```
Rhye's and Fall RAND is a project that tries to offer something halfway between RFC and
standard Civ. All the great additions of RFC, such as stability, historical spawn dates, congresses,
victory conditions and the UPs are in. However, certain adjustments were necessary, and the
terrain generated is very different from the standard one, and is limited by some constraints.

## Installation

- Extract the files contained in the zip
- Copy and paste the Rhye’s and Fall RAND folder in ...your Civ4 folder...\BTS\Mods\
- Start Civilization, go to ADVANCED , then LOAD A MOD , select Rhye’s and Fall RAND
- After the mod loads, choose PLAY NOW!, Rhyes_Terra, and then you can set your preferences
- WARNING: if you want to use CUSTOM GAME, please read carefully the "Custom Game" paragraph at the bottom of this document.
- Map generation takes a while, so be patient

## World size

There are three world sizes. They can hold 15, 21 and 27 civs (plus minor civs). Your civ will always be present in a game with a smaller world size; the others are picked semi-randomly.

## Terrrain generator enhancements

Rhyes_Terra is based on other generators such as Terra.py. Its enhancements include:

- The addition of marshes
- Extended areas of the same terrain type, rather than the usual pattern of mixed terrains
- Adjusted latitude of terrain types (still retaining the climate type options)
- Mountain chains that act as barriers
- Very high landmass/ocean ratio (which allows smaller maps supporting many civs at the same time)
- Variable equator position (to allow a more comfortable northern or southern hemisphere)
- Presence of a minimum distance of 5-6 plots from different groups of continents, which is enough to make communications impossible until Renaissance

## Earth likeness

This parameter of the world setup sets how much the world generated is similar to the Earth.

### Very High likeness:

- Earth-like shape and disposition of continents.
- Wrapping is only allowed in horizontal (cylindrical world).
- The equator is horizontal and is placed 18% lower than half map, in order to match Central Africa and Brazil.
- Terrain is adjusted in certain cold areas (North-West, Siberia, Northern Europe) to better represent real unhabitated lands.
- America is stripped bare of all the unhistorical resources. The old world hasn’t got maize instead. Wheat is more common in the west of Eurasia and rice in the east.
- Independent and Barbarian cities spawn within historical coordinates
- Mercenaries that need Old World resources can’t be built in the New World.
- All civs are placed in their real regions (if it’s not completely covered by other civs).
- Starting locations and AI settlers are strongly influenced by neighbouring civs (Asian civs tend to spawn close to other Asian civs, etc.)
- Civ spawn dates are the same as in classic RFC.
- Unique Historical Victories are enabled and should usually be all possible.

### High likeness:

- Earth-like disposition of continents (America at west, a kind of Eurasia at north and east, possible presence of two main islands at the left and right edge of Eurasia, Africa at south).
- Wrapping is only allowed in horizontal (cylindrical world).
- The equator is horizontal and is placed around 15% lower than half map, in order to match the continents that resemble Africa and South America.
- Terrain is adjusted in certain cold areas (North-West, Siberia, Northern Europe) to better represent real unhabitated lands.
- America is stripped bare of all the unhistorical resources. The old world hasn’t got maize instead. Wheat is more common in the west of Eurasia and rice in the east.
- Independent and Barbarian cities spawn close to historically related civs
- Mercenaries that need Old World resources can’t be built in the New World.
- Old world civs are placed in a way that they look like the Earth (Euros at west, Asians at east; same for north/south divide).
- Starting locations and AI settlers are strongly influenced by neighbouring civs (Asian civs tend to spawn close to other Asian civs, etc.)
- Civ spawn dates (excluded the player’s civ and the turn 0 starters) may vary of a few turns.
- Unique Historical Victories are enabled and should usually be all possible.

### Medium likeness:

- Earth-like continents, but they may vary more in the shape and be flipped on the horizontal and/or the vertical axis.
- Wrapping set randomly: flat world, toroidal world or vertical wrapping are possible.
- The equator is usually horizontal and is placed around 15% lower or higher than half map, depending on the placement of the biggest landmass, but can vary its orientation.
- No terrain adjustment is made.
- America is stripped bare of the most important unhistorical resources, such as elephants and horses.
- Independent and Barbarian cities spawn close to historically related civs
- Mercenaries that need Old World resources can’t be built in the New World.
- Old world civs are placed may be placed with some constrains like in high likeness, or may not be. The only certain constraint is the old/new world civs divide.
- Starting locations and AI settlers are strongly influenced by neighbouring civs (Asian civs tend to spawn close to other Asian civs, etc.)
- Civ spawn dates (excluded the player’s civ and the turn 0 starters) may vary of more than 10 turns.
- Unique Historical Victories are enabled, but sometimes they may be impossible.

### Low likeness:

- Continents may have different shape and position, but still retain a margin that divides groups of continents
- Wrapping set randomly: flat world, toroidal world or vertical wrapping are quite common.
- The equator can be horizontal, vertical or be set at the edges or at the centre of the map.
- No terrain adjustment is made.
- No resource adjustment is made.
- Independent and Barbarian cities spawn close to historically related civs, at random dates
- Mercenaries don’t have any lock.
- There are no constraints on starting locations: a new/old world civs divide is likely, but you might see them mix up as well.
- Starting locations and AI settlers are quite influenced by neighbouring civs (Asian civs tend to spawn close to other Asian civs, etc.)
- Civ spawn dates are partially random. Starting units, technologies and hidden modifiers are rescaled to the new date as well.
- Unique Historical Victories are still enabled, but sometimes they may be impossible.

### Very Low likeness:

- Not only continents: archipelago, panagaea and inner sea in various combinations may be generated
- Wrapping set randomly: flat world, toroidal world or vertical wrapping are common.
- The equator can be horizontal, vertical or be set at the edges or at the centre of the map.
- No terrain adjustment is made.
- No resource adjustment is made.
- Independent and Barbarian cities spawn randomly, at random dates
- Mercenaries don’t have any lock.
- There are no constraints on starting locations.
- Starting locations and AI settlers are slightly influenced by neighbouring civs (Asian civs tend to spawn close to other Asian civs, etc.)
- Civ spawn dates are totally random. Starting units, technologies and hidden modifiers are rescaled to the new date as well.
- Unique Historical Victories are disabled.

## Starting locations

While we have fixed starting locations in RFC and totally random locations in standard Civ, RFC RAND features some additional code that makes certain terrain types more important than others, depending on the civ. The Egyptians have high modifiers for desert, rivers and a certain range of latitude (those latitudes are shifted when climate is different than temperate).

There are many other parameters, like the distance from the coast, which all influence not only the starting location placement, but the settlers as well. These modifiers alone, in fact, will form the new settlers maps, which will influence stability. As the Vikings, settling near the equator is a good way to have a low expansion stability rating.

Starting locations are also guided by a system of "attraction and repulsion". As Japan, plots close to China are more highly valued, while plots close to Rome or Egypt, for instance, have its value
decreased.

This means that when you're playing, you don't know WHERE a new civ will spawn. As Rome, Germany may spawn next to you, and flip some of your cities, or next to France or Spain, and not
affect you at all. America is a special case, since it is supposed to spawn in America, and close to some European
city. Of course, even less is known in very low likeness, as spawn dates are totally random.

## City names management

Obviously, there can't be names assigned to plot coordinates, but still it doesn't mean that we should rely on completely random names.

So, each civ will have 4 city names lists:

1. for non-coastal cities in the continent
2. for coastal cities in the continent
3. for non-coastal cities in another continent
4. for coastal cities in another continent

The capital is always at the top of 1 or 2.
This picture shows cities picked from lists 3 and 4:


## Historical goals

Some historical goals had to be readapted. Check Civilopedia for details.All you need to know that’s not written in the pedia is the meaning of "new world", as mentioned in Spanish and French goals.

With high or medium Earth likeness, it’s the group of landmasses in the zone of the world corresponding to North and South America, where Aztecs, Maya and Inca always spawn.

With low likeness, it depends on the position of the continents: when there’s a biggest world, and two other small continents, these two are considered "new world"; when there’s a biggest world, a medium-sized world and a small continent, it’s the medium-sized world; when there are three continents of the same size, it’s one of the three (usually the one where there’s at least one native American civ, but it may be more crowded: you can tell it by checking if the conquerors event was triggered). You can always press SHIFT+ALT+W once you have researched Compass if you are unsure about which continents are the new world.

However, due to the randomness of the world generation, it may happen that some goals, in some maps, are materially impossible. For this fact, Historical Victories were disabled on very low.

## Unique powers

Egyptian, Mayan and American Unique Powers have been slightly changed. Please check Civilopedia for details (NOTE: English and Italian text only contain updated descriptions: other languages still contain old text).

## Custom game

If you want to use the CUSTOM GAME option, please don’t touch the list of the civilizations and their team numbers. Just pick your civ, and ignore the rest of the list (however, you may still
enable and disable game options and victory conditions). As RFC uses its own team numbers, changing those slots may cause crashes or weird behaviours.

"Start in 3000 BC" option works only in Low and Very Low likeness.
	
