# Rhye's and Fall of Civilization guide to stability

## Introduction


### What is stability?

In order to create a true rise and fall of civiliations, Stability has been added to the game. Stability is the most arcane system to be implemented in a Civ4 mod, and here we will attempt to explain it. Stability plays a very important role in RFC. Nearly everthing you do effects the stability of your civilization.

* The number of cities you build, their location and the buildings you construct.
* The mood of your citizens.
* The technologies you research.
* The civics and religions you adopt.
* Your economy, taking into account the population, agriculture, Industry and financial aspects.
* Your relations and contacts with other civs.
* The wars you fight. 

Plus many other factors.


### What impact does this have on the game?

Well a very big one.

You can not play RFC like regular Civ or Warlords. If you do you will soon be seeing you empire collapsing around your feet and your citizens clamouring to join other civilizations.

So what can we do about it?

Well if we know what factors effect stability we can plan our gameplay accordingly. The thing to remember though is that stability improvements occur overtime - not instantaneously. So do not wait until you have stability problems before acting, as you probably will be too late.


### How is stability calculated?

This is the complicated bit.

The game uses two methods to calculate stability, which when added together give your actual total stability.

These two methods are base stability and stability.

Base stability is calculated every turn on certain factors and is the main indicator of your actual stability. This value is not accumulated but is added to the permanent values each turn. The reason for this is that you can change your actions and thus cancel or reverse a previous effect.

Some base stability factors are calculated every 3 turns - so as not to slow down game play.

Stability adds some permanent modifiers, triggered once as certain events happen. These values are applied only once and are accumulated.

Each calculation (of which there are many) can produce either a zero or positive or negative value depending upon what you are doing.

Total stability is what you see in the game. This total stability is the sum of base stability and stability.

So at the start of each turn we have a total stability value which can be either positive or negative.


### What is our total stability and where is it shown?

As these values are not displayed in the game, I shall refrain from using numbers where possible. But there are three ranges for positive values and three ranges for negative values.

Positive values are displayed as: Very solid, Solid and Stable. Negative values are displayed as: Shaky, Unstable and Collapsing.

This stability is displayed in two ways.

On the main screen in the score list, next to each civ you will see one of three icons

* (o) (in a bowl) represents: Very solid and Solid.
* _o_ (flat surface) represents: Stable and Shaky.
* (°) (on top of an upturned bowl) represents: Unstable and Collapsing. 

Do not worry, the actual icons look much better.

examplegd4.png

Press F2 or click on the '$' Icon to enter the renamed Interior Advisor Screen (was Financial Advisor).

stabstars.jpg


Near the bottom of the screen you will see the Stabilty level which will have one of the following descriptions:

* Very solid
* Solid
* Stable
* Shaky
* Unstable
* Collapsing 

Under the description are five categories:

Cities, Civics, Economy, Expansion and Foreign.

Each category has a star rating from one to five. The stars show the stability of your civilization under each category. So at a glance you can see what part of your empire needs attention.

Because some categories have lots more factors influencing stability than others it is not safe to assume that 3 stars in one category equates to the same numeric stability values as the other 3 star entries. THEY DO NOT.

So now we know what our stability rating is and what parts of our civilization are causing it.


### What can happen because of stability?

Well, you or the AI can lose a city or cities or all of your empire (except for one city if the human player).

Stable or above civs are safe. (Note: Not sure what happens when a new Civ is born - e.g. France German etc.)

Shaky civs are only at risk of losing cities when new or resurrecting civs spawn.

Unstable civs are in danger of secessions. From time to time, unhappy cities will declare independence.

Collapsing civs risk to end up in civil war. When this happens, the AI collapses and it is split into independent states and barbarians. Neighbouring civs can absorb some cities.

The human player retains one city, usually the capital, from which he can take the others back.

There is a warning before secessions and resurrection of civs.


## Stability Calculations


Note: When showing stability changes a P indicates permanent change. +/- indicates a value less than 10. ++/-- indicates a value greater than 10.


### Permanent Stability

When you start a new game the permanent stability value is set as follows:

* Viceroy = Solid.
* Monarch = Stable.
* Emperor = Shaky. 

This can be increased or decreased every turn depending upon events that have taken place:

* GNP changes +/- (see Demographics screen)
* high combat loss -
* Anarchy -
* Cities built,occupied, traded,razed or lost +/-
* Granting independence - (BtS only)
* Tech just researched (see below) +/-
* Certain Buildings built +
* Palace moved - -
* Wonders built +
* Projects built (not SS parts) +
* Religion founded -
* Corporation founded - (BtS only)
* At war with rival religous civ. - 

Every so often in the game the permanent stability value is checked and adjusted if too high or too low. This is to stop the runaway or dommino effect. Not just for you, but the AI also.


### Base Stability

This is calculated in two parts - somethings every turn, others every three turns.

Calculated every turn are:

* Great Depression - -
* Techs researched and Civics being used - -
* Number of cities -/- -
* Current combat results -/+ or - -/++ (depending on all the battles)
* Anarchy - -
* Golden Age ++ 

Some additional calculates are performed every third turn:

* Every defensive pact ++
* Every open border +
* Unstable neighbour when your stable -
* Having a vassal +/++
* Historic Civ Size (see below) - -
* Civics selected ++/- - (most are +/-)
* Citizens moods - -
* Foreign Culture -
* Economics, Industry, Agriculture and Population ++/- -
* Happiness ++
* Number of civ contacts +/- 


### Historical civ size

There are also checks based on historic expansion. So a civ that never became large in real life will get penalties if it expands to much. Also a civ that was historicaly large will get penalties if it does not expand enough.

It works counting:

* how many other civ's cities are in your core area
* how many plots you have outside of the area of historical maximum expansion (colonies included) 

These values are used in some formulas to add a negative base modifier to expansion. It balances out the (usually positive) modifiers you get founding and conquering cities.

An important part of keeping stability is taking care not to over-expand. If you try to do a large fast land-grab conquest, or a settler spam, you'll find yourself with an empire larger than your government is capable of handling. You don't want to expand too fast, but you don't want other civs to grab all the good land either, so it's important to find a good balance.


### Final value

At the end of all these calculations, permanent and base stability are added together and normalised. So we now know how stability is calculated. A lot of things as you can see. So do not expect to master stability quickly.

NOTE: All the following factors wont be to detailed (we do not want spoilers ruining the game) and I shall try to refrain from using numbers - just pluses and minuses. Because Rhye is bound to change values as he ruthlessly tracks down human exploits and lays traps for the unwary player.


## The stability categories


We will now look at the 5 stability categories and which of the above actions effects each. Then we will get to the important bit - what can we do to change stability.

Press F2 or click on the '$' Icon to enter the renamed Interior Advisor Screen (was Financial Advisor).

Under the stability description are five categories:

Cities, Civics, Economy, Expansion and Foreign.

Each category has a star rating from one to five. The stars show the stability of your civilization under each category. So at a glance you can see what part of your empire needs attention.

So what effects each category?

Let us look at each in turn. Using the events listed above.

### Categories

Remember: a P indicates permanent change. +/- indicates a value less than 10. ++/-- indicates a value greater than 10.

#### Cities

* Citizens moods - -
* Foreign Culture -
* Happiness ++
* Certain Buildings built + P
* Palace moved - - P
* Wonders built + P
* Projects built (not SS parts) + P
* Religion founded - P
* Corporation founded - P (BtS only)
* At war with rival religous civ. - P 


#### Civics

* Civics selected ++/- - (most are +/-)
* Techs researched and Civics being used --
* Anarchy - P/ - - 


#### Economy

* Economics, Industry, Agriculture and Population ++/- -
* GNP changes +/- P
* Great Depression - -
* Techs researched and Civics being used - -
* Golden Age ++ 


#### Expansion

* Historic Civ Size - -
* Number of cities -/- -
* Current combat results -/+ or - -/++ (depending on all the battles)
* Cities built,occupied, traded,razed or lost +/- P
* Granting independence - P (BtS only) 


#### Foreign

* Every defensive pact ++
* Every open border +
* Unstable neighbour when your stable -
* Having a vassal +/++
* High combat loss - P
* Cities traded +/- P
* Number of civ contacts +/-
* Granting independence - P (BtS only) 


Note: If an event is listed twice, it does not mean it has been calculated twice in the total stability value. It is just that its effects are represented in more than one category.

Well; now that we know most, if not all the stability factors and what they change. We can start to consider what we have to do ingame.



## Cities category

### Citizens moods --

In the city screen, mouse over the unhappy faces to see the citizens moods:

Angry population. - A city religion is the same as your opponents state religion during war. - Hurry (whipping) Anger. - Anger from lack of military units in the city. - War weariness anger. -

These city penalties aren't applied directly, they are accumulated for each city. Each city is checked until a cap is reached - A total value for all cities is also capped. --

Note: The above does not apply if you are at war and have occupied the city and you are running the Occupation civic.

### Foreign Culture -

If there is foreign culture in the city:

Your culture is zero. -

You have culture and any foreign culture that exceeds about 15% of your culture - You have culture and the civic nationhood, any foreign culture that exceeds about 5% of your culture -

Note: The check on their culture is relative to yours, NOT to the total.

Example: You have 16% culture in a city. CivA has 80% total culture and CivB has 4% total culture.

Both trigger a penalty because:

CivA has 500% of your culture. CivB has 25% of your culture.

The percentage is lower for nationhood because of the nationalistic feelings that trigger unrest.

### Happiness

Average happiness from all cities +/-

If your approval rate (from the demographics page) is more than 70, you get a bonus, if less than 60 you get a penalty.

### Buildings +/-- P

Building a courthouse. + Building a jail. + Building an intelligence agency or security bureau. + Building a jail while running the civic police state. + Building a wonder. + Building a great project (other than spaceship parts) + Building another palace (NOT moving palace, you need to build Forbidden Palace or Summer Palace). ++

Corporation founded. - (BtS only)

Moving the original palace. --

### Religion -

If you are using theocracy or organized religion, each religion other than the state religion in a city results in a penalty. -

Founding a religion. - P

If a religion which isn't your state religion spreads to a city and you are at war with a civ whose state religion is that religion. - P


## Civics category

Civics play an important role in the stability of your empire: most of them can cause positive or negative modifiers depending on certain conditions.

Some combinations of civics and events are particularly dangerous, as they may trigger negative modifiers that last more than one turn, such as the Great Depression, a post-communist crisis, or a troubled transition to democracy. All three of them are big hits to your stability.

Fortunately, there’s a brand new civic column “Expansion” that only affects stability. So, you and the AI have a chance to plan the strengthening of the empire by choosing an appropriate civic.

### Civics selected

In this section we shall look at each civic category and its civic choices. I have also included techs researched.

The categories are: Government, Legal, Labor, Economy, Religion and Expansion.


#### Government

##### Despotism

If stability is Collapsing (and below mid range for collapsing) you get a boost, which may move you to just below Unstable ++

* Combined with civic Bureaucracy -
* If you have the tech Democracy -
* If you have the tech democracy and switch to universal suffrage, you suffer for a number of turns - - 

##### Hereditary Rule

* If stability is Collapsing, caps it just below Unstable ++
* Combined with civic Vassalage +
* If you have the tech Democracy -
* If you have the tech democracy, and switch to universal suffrage, you suffer for a number of turns. -- 

##### Representation

* If stability Solid (and in top half of range) +
* Combined with civic Bureaucracy +
* Less than 3 cities (+ per city, capped) +
* More than 3 cities (- per city, capped) -
* If you have the tech Democracy - 

##### Police State

* If stability is Collapsing (and below mid range for collapsing) you get a boost, which may move you to Unstable ++
* Combined with civic Nationhood ++
* For every 5 cities + (capped at 50 cities) ++
* Combined with civic State Property +
* If stability is less than solid and you have a jail the city gets extra stability +
* If you have the tech Democracy -
* Combined with civic Free Speech - -
* If you have the tech democracy, and switch to universal suffrage, you suffer for a number of turns. -- 

##### Universal Suffrage

* If stability Very Solid (and in bottom quarter of the range for Very Solid) ++
* If you have the tech Democracy (no penalty) equivelant to +
* Combined with civic Barbarism -
* If you have the tech democracy, and switch from despotism, hereditary rule, or police state you suffer for a number of turns. - - 

##### Government Notes.

Switching from representation to universal suffrage causes no penalty. If you had enough time and assuming you are stable enough. You could avoid the penalty by switching from one of the despotic civics to representation and then to universal suffrage when you are able to switch again.

Hereditary Rule and Vassalage during the middle age is a good combination. + But they give no bonus in any other era.


#### Legal

##### Barbarism

* Combined with civic Universal Suffrage -
* If you have the tech Liberalism - 

##### Vassalage

* Combined with civic Hereditary Rule +
* Select in Medieval era +
* Select outside Medieval era -
* Combined with civic State Property -
* If you have the tech Liberalism - 

##### Bureaucracy

* Combined with civic Representation +
* 5 or less cities +
* 6 or more cities (- per city, capped) -
* Combined with civic Despotism -
* If you have the tech Liberalism - 

##### Nationhood

* Combined with civic Police State ++
* Combined with civic Mercantilism +
* For each civ you are at war with +
* Combined with civic Pacifism - -
* If you have the tech Liberalism - 

##### Free Speech

* If you have the tech Liberalism (no penalty) equivelant to +
* Combined with civic Police State - - 

##### Legal Notes.

Hereditary Rule and Vassalage during the middle age is a good combination. + But they give no bonus in any other era.


#### Labor

##### Tribalism

* If you have the tech Democracy - 

##### Slavery

* If you have the tech Bronze Working, until you get the tech Constitution +
* If you have the tech Democracy - 

##### Serfdom

* If you have the tech Democracy - 

##### Caste System

* Combined with civic State Property -
* If you have the tech Democracy - 

##### Emancipation

* Combined with civic Free Religion +
* Combined with civic Theocracy -
* If you have the tech Democracy (no penalty) equivelant to + 


#### Economy

##### Decentralization

* If you have the tech Economics - 

##### Mercantilism

* Combined with civic Nationhood + 

##### Free Market

* Free market has the possibility of getting a great depression - - (see below) 

##### State Property

* Combined with civic Police State +
* Combined with civic Caste System -
* Combined with civic Vassalage -
* If you have the tech communism and switch from state property, you suffer for a number of turns. - - 

##### Environmentalism

* No effects on stability. 


#### Religion

##### Paganism

* No effects on stability. 

##### Organized Religion

* With a state religion, every other religion in the city results in a penalty for that city. - 

##### Theocracy

* Combined with civic Emancipation -
* With a state religion, every other religion in the city results in a penalty for that city. - 

##### Pacifism

* Combined with civic Nationhood -- 

##### Free Religion

* Combined with civic Emancipation + 


#### Expansion

This is a brand new civic column that only affects stability.

##### Subjugation

* No effects on stability. 

##### Viceroyalty

* For every Vassal Civ* + 

##### Resettlement

* For every city built 15 or more tiles from the Capitol. + 

##### Occupation

* On capturing a city. +
* If at war no penalty for occupied cities due to citizens anger, religion or foreign culture. Equivalent to +/++ 

##### Commonwealth

* No penalty from low imports/exports. Equivalent to +
* No penalty from low economy/population ratios. Equivalent to + 

##### Expansion Notes.

The commonwealth civic prevents new negative modifiers. It doesn't erase the existing ones.


### Great Depression

It happens if a civilization has excessive production over commerce (which causes deflation), while it's running a free market economy. It's a big hit to a country's stability and can affect all the civs which have an open border agreement with this civilization. Switching away from free market is a solution to quit the depression, but it's dangerous! A period of anarchy is definitely the last step towards civil war. You'd better be careful then, and if your total rating is unstable or worse, it's better to improve stability by other means (such as building wonders) and wait until it's over.

#### Anarchy

Anarchy - P/ - -

When you change civics you get a period of anarchy (except when you have the Unique Power to prevent it).

Your permanent stability is effected by anarchy. -

During the period of anarchy your stability takes large drop. --

##### Anarchy Notes

If your stability is UNSTABLE the period of anarchy will drop you into the COLLAPSING range. Having a golden age raises stability, so changing civics in a golden age may prevent this.


### Technologies

Techs researched and Civics being used - -

These are also covered in the "Civics" section above.

Every new Tech has a + or - stability value based on its historical effect on society.

Basically the '+' techs are those that were historically beneficial in some way: Religion, Rule of Law, Education, Entertainment, Commerce, Production and Food provision amongst others.

The '-' Techs are those that historically had some negative effects on society: military units, new forms of government or polluting Industrial features etc.

Incase anyone noticed - these tech adjustments do not effect the categories shown in the F2 screen.

Some techs have additional effects:

* Democracy unless you switch to Universal Suffrage and Emancipation. -
* Democracy and switching to Universal Suffrage from Despotism, Hereditary Rule or Police State - - (for a number of turns).
* Liberalism unless you switch to Free Speech. -
* Bronze Working (before Constitution is researched) and using civic Slavery. +
* Economics and using civic Decentralization -
* Communism and switching from State Property to a different civic - - (for a number of turns). 


## Economy category

The economy rating, regardless of the type of economy you create, is heavily influenced by growth. The more GNP and production grows, the more stability improves. When you stop or shrink, it decreases.

Economics, Agriculture and Population ++/--

Amount of food per population. +/- The more people you have relative to agriculture the worse the penalty.

Amount of gold (Economy) per population. +/- The more people you have relative to gold the worse the penalty.

Running the Commonwealth civic, No penalty from low gold per population. Equivalent to +. However, agricultural penalties still apply.


### Imports/Exports are your trade with other nations:

* High level of imports/exports. +/++
* Low level imports/exports. -
* No imports/exports. - 

Running the Commonwealth civic, No penalty from low imports/exports. Equivalent to +.

Note. Economy is the GNP(gold) on the demographs page.


### Adjusted GNP changes +/- P

The GNP (Gross National Product) in Civ4 just deals with the commerce side of the game. In RFC commerce, industry and agriculture are taken into account. Each is given a weighting added together then the average value calculated. This is the GNP used for stability purposes. It is checked every 3 turns and capped.

if the GNP drops. - Any GNP loss greater than 20 will get the same penalty.

if the GNP rises above a preset value. + Any GNP gain greater than 35 will get the same bonus.

Note: To balance the gameplay, GNP has to rise above a preset value before gaining any stability bonuses. To avoid these permanent penalties - you need to keep your GNP growing.


### Great Depression --

Running the civic free market can cause a Great Depression in certain situations.

A Great Depression is triggered when industrial output is far greater than your economy and your GNP is increasing. It also takes into account the population size. So the larger the population the larger the differance can be before a depression is triggered.

Example: If a differance of 10 triggered a depression with a population of 1 million. You would need a difference of 20 for 2 million population, but only 5 differance for 1/2 million population. Remember you must be running the free market civic.

A Great Depression can not occur during a golden age.

Suffering a Great Depression. -- (for a number of turns)

You have open borders with a civ suffering from a great depression. -- (that turn only) The penalty is only applied for the first civ and only if you are not in a Great Depression.

After a number of turns you can break out of a great depression, if the industrial difference decreases and your GNP has not increased, or you have switched away from the free market civic.


### Techs researched and Civics being used --

If you have researched the tech communism and switch from state property, you suffer a penalty for a number of turns. --


### Golden Age

Having a Golden Age. ++

Note: A Great Depression can not occur during a golden age.


## Expansion category

You can expand your empire either peacefully, by building cities on unclaimed land or by force of arms. But becareful expand to quickly and you will pay the price.

There is also a brand new civic column Expansion, that only affects stability. A few other civics effect expansion too. So you have a chance to plan the strengthening of your empire by choosing the appropriate civics.


### Historic Civ Size

There are checks based on historic expansion. So a civ that never became large in real life will get penalties if it expands to much. Also a civ that was historicaly large will get penalties if it does not expand enough.

It works by counting:

* how many other civ's cities are in your core area.
* how many plots you have outside of the area of historical maximum expansion (colonies included). 

These values are used in some formulas to add a negative base modifier to expansion. It balances out the (usually positive) modifiers you get founding and conquering cities.

An important part of keeping stability is taking care not to over-expand. If you try to do a large fast land-grab conquest, or a settler spam, you'll find yourself with an empire larger than your government is capable of handling. You don't want to expand too fast, but you don't want other civs to grab all the good land either, so it's important to find a good balance.

Note: This does not stop civ's expanding outside their historic areas - you just have to plan your expansion carefully taking into account your stability. If you are Shaky or worse you are liable to lose some of those cities to secession or a civ re-spawning.

If you want a big empire choose a civ that did: Russia, America, Germany, France, Spain, England, China,...


### Number of cities

The number of cities you own effects your stability rating. The bigger your empire the more unstable it becomes. There is no penalty for the first 7 cities. After that, every additional city has a negative stability impact. This initially only cancels out the bonus for building cities and only becomes a real penalty when you get near 20 cities.

The thing to be careful about is that the stability penalty per city increases when certain limits are reached. These limits are approximately every 10 cities.

Examples of the stability effect that the number of cities have are:

* 7 cities = no impact.
* 10 cities = - small impact.
* 15 cities = - the total effect is equivalent to half a stability level drop.
* 20 cities = -- the total effect is equivalent to one stability level drop.
* 25 cities = -- the total effect is equivalent to two stability level drops.
* 30 cities = -- the total effect is equivalent to three stability level drops.
* 35 cities = -- the total effect is equivalent to four stability level drops.
* 40 cities = -- the total effect is equivalent to six stability level drops. 

The above example just shows the total effect of a lot of cities. It is calculated on the actual number of cities you have.

There is also a research penalty for giga empires. This way there won’t be one leader with 30+ cities and far far ahead in technology.

Some Civics are linked to the number of cities.

* Representation: Less than 3 cities (+ per city, capped) +
* Representation: More than 3 cities (- per city, capped) -
* Bureaucracy: 5 or less cities +
* Bureaucracy: 6 or more cities (- per city, capped) -
* Bureaucracy and Representation combined +
* Police State: For every 5 cities + (capped at 50 cities) ++ 

Note: these civics do not effect the Expansion category.


### Cities built,occupied, traded,razed or lost P

These are permanent modifiers:

* For every city you build +
* With Resettlement civic, for every city built 15 or more tiles from the Capitol. +
* For every city acquired through trade, congress or conquest. +
* With Occupation civic on capturing and not razing a city. +
* On acquiring a Capitol city. + 

For every city lost through a civ birth or reserrection. -

When you lose a city other than through civ birth or reserrection, you get two penalties/bonuses. One based on the number of cities and one on the way it was lost.

If less than 15 cities: (the fewer cities, the higher the penalty) - With a smaller empire the loss of a city is more traumatic to the people.

If more than 15 cities you get a bonus (the more cities the higher the bonus) +/++ The bonus reflects the fact that larger empires are more difficult to control and losing cities is not so traumatic to the population. Some may not even know where that city was located. Also fewer cities over time make administration easier.

The above is then adjusted by:

* For every city lost through trade, or conquest. -
* If city is razed. -
* Granting independence - (BtS only) 

Losing the capitol. --

Note: When you capture a city, you might find that much of the impact on your stability comes from having lots of unhappiness due to citizens anger, religion or foreign culture - except when running the Occupation civic.


### Current combat results

Every victory gives a bonus and every loss twice that as a penalty. These are added together for each turn. The total which is capped, effects the Expansion category. To many losses and your expansion capability is lowered.

Total combat Victory/losses. ++/-- (half is added to next turn)

If the total is more 4 points +/-, it is halved and carried over to the next turn. So losing a lot of units will effect stability for a number of turns. No more mass suicide attacks to take that hill city. Well not if you want to remain stable.

Note: The foreign category also suffers a small permanent penalty due to high combat losses.


## Foreign category

This covers everything regarding foreign affairs..... mainly diplomatic agreements, plus other less important factors.

### Defensive pacts ++

Every defensive pact signed. ++

### Open borders +

Every Open Border agreement. +

### Unstable neighbour when you're stable -

If a neighboring civ's stability is unstable or collapsing and yours is stable or better. -

This penalty will only be applied once regardless of how many neighboring civs are unstable.

### Having a vassal -/+

For each vassal the civ has. +/- The value depends on the Vassal's stability.

The civic viceroyalty gives a bonus for every vassal. +

### Number of civ contacts +/-

When you have gained a high number of contacts, with other civs you start to incur a penalty. - This penalty increases as the number of contacts increase.

Note: This helps East Asian civs, who having less contacts, tend to develop less trade and get a lower Economy rating.

Remember having Embassies allows you to maintain contact. Otherwise over time you will lose contacts with other civs.

### High combat loss - P

Suffering just above negative combat stability this turn. You suffer a small permanent penalty. -

This will happen even if you have lost fewer units than the enemy. Your troops losses are valued twice that of the enemy. So if you kill 8 enemy units, but lose 6 of your own. This is considered high combat loss.

Note: The Expansion category suffers a greater temporary penalty due to combat losses.

### Cities traded - P

If the city is traded away. - Granting independence - (BtS only)


## Final Note

Some penalties or bonuses may seem to be odd choices to the human player. The thing to remember is that some are there to help the AI civs in the game. So that you can play a more realistic and enjoyable game. 
