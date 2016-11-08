# RFC-RAND-UP
Unofficial Patch for the Civilization IV: RFC RAND mod

### Python bug fixes

Changed CityNameManager.py to the cleaned version from RFC RAND Plus to prevent Python error messages with non-ascii characters in some city names.

### Logical bug fixes

The most important one was the fix of the bug with non-spawning of coastal starting units. I changed the tile search from 1 to 2 and made sure the tile found was coastal. This is to prevent the situation where you spawn 1 tile inland with no open water in a 1 tile radius around you starting point. When that happened you didn't get all the coastal starting units. This was happening quite a lot with Rome and Greece.
I fixed it in RiseandFall.py in several places.

See post: http://forums.civfanatics.com/showpost.php?p=9264065&postcount=6

I fixed all the barbarian sea spawn bugs. In an earlier version of RFC RAND there was a bug with barbarian ships spawning on random water tiles with seaice on it.
The check for this seaice feature was implemented in 1.27, but created a new bug where barbarian ships could only spawn on seaice.
I fixed it in RFCUtils.py in the OuterSeaSpawn function.

I also changed the ships spawning for the celtic norse in North Europe and the barbarian pirates in the mediterrenean by changing them to OuterCoastSpawn to prevent triremes and galleys spawning on ocean tiles.

### Additions

Added missing CIVIC_SUBJUGATION for all the civs in Civ4CivilizationInfos.xml

http://forums.civfanatics.com/showthread.php?t=348436

Added Wide Citybar by asioasioasio in Art/Interface/citybar/*.*

http://forums.civfanatics.com/showthread.php?t=239221

### Typos

Civ4GameText_UP.xml - "Burocracy" changed to "Bureacracy"

CvRandomEventInterface.py - "getHelpThGoths1" changed to "getHelpTheGoths1"

### Tweaked

Tweaked RFCEventhandler.py because Resources.py is not used

### Other changes

Removed the no-Jerusalem-flip on spawn.
With hindsight it was a bad idea to use this as a way to nerf Greece and the implementation led to other problems.
I changed it in RiseandFall.py.

See post: http://forums.civfanatics.com/showpost.php?p=9579381&postcount=44

Revisited the "Supergreece" problem.
Returned Hunting and The Wheel as starting techs, but removed the attacking Greek Phalanx to prevent it from taking Jerusalem too early.

Less barb camel archers in Africa (same number for as for low likeness maps).

Removed plains requirement for silk to wine swap in Europe (suggestion by ImNotHere).
