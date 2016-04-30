## Characters
<hr>

A character is an **animated** object.

- Average body height is **8 heads** for a human(oid) character in this style.
Since the head is 3 pixels high, not including the hair, 24 pixels is the *ideal* height of characters.

- **Character animations** should be no more than **8 frames**. Maintain the correct **proportions**. Use **layers**. The head (face, ear, neck), hair, torso, hip, upper leg, and lower leg (shin,feet) should *ideally* be on their own layers to allow more **flexibility** for edits.

- **The naming convention** for characters is **chr_chrName_version**
	- Examples:
		- chr_male_pale
		- chr_male_fair
		- chr_male_dark
		
- If the file contains more than one character use chrs:
	- Examples:
		- chrs_animals
		- chrs_flowers
		- chrs_people 	

The **characters** were created *roughly* in this order:

1. Face
2. Neck
3. Ear
4. Face highlight
5. Neck shadow
6. Shoulders
7. Torso
8. Hip
9. Legs
10. Torso highlight
11. Torso shadow
12. Arms
13. Hair

Here are the pixel height stats for the base character

- 3 block(s) - face
- 1 blocks(s) - neck
- 5 or 6 blocks(s) - torso
- 2 blocks(s) - hip
- 6 blocks(s) - thigh
- 7 blocks(s) - shin

= approximately **24**

For base character 2 (32 high is ideal)

- 2 x 4 face (not including hair and ear)
- 2 x 1 neck
- 4 x 7 - torso
- 4 x 2 - hip
- 1 x 16 - legs
- 2 x 1 - feet
- 1 x 0 - arms

= **6 x 33**


A few width stats:

- 2 or 3 block(s) - head (3 for wider face)
- 3 block(s) - body
- 1 or 2 block(s) - neck
<hr>

## Props
<hr>
A prop is an **inanimate** object. Things like tables, chairs, and buildings fall under this category. A tree on the other hand would be a character *if it is animated*. 

- If a door is animated, it belongs under the character category

- **The naming convention** for props is **prop_propName_version**
	- Examples:
	 - prop_door_dark
	 - prop_door_maple
	 - prop_door_cherry
<hr>


## Environments
<hr>
An environment is a collection of objects that make a **setting**.

- **The naming convention** for environments is **env_environmentName_version**
	- Examples:
		- env_park_day
		- env_park_night
		- env_park_winter
		- env_park_spring 

## Scenes
<hr>
A scene is a **collection** of props, environments and characters.

- **The naming convention** for scenes is **scn_environmentName_sceneName_version**
	- Examples:
		- scn_park_day_childrenPlaying
		- scn_park_night
		- scn_park_winter
		- scn_park_spring 

- All scenes must use submitted environments. So, when making a scene, submit the environment separately as well.
<hr>

## Palettes
<hr>
- Palettes should have no more than **8 colors**.

- **The naming convention** for characters is **paletteName_version**
	- Examples:
		- skin_light
		- skin_medium
		- skin_dark
		- skin_alien 	
<hr>

## Uploading
<hr>
- Submit all objects as **256px** .png **spritesheets**, along with the **.piskel** file saved in the 32 x 32 or 64 x 64 size.
- Images should be in their respective folders using the following convention:
	- **objectName_size.png**
- Each character should have at least 1 frame for nude, underwear, casual, and formal to start.
<hr>
*Yeah, it's all about 8!*

[@TutorialDoctor](https://twitter.com/TutorialDoctor)
