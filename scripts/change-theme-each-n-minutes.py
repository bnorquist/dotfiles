#!/usr/bin/env python3.7

import asyncio
import datetime
import random
import iterm2

# How often you want the theme to change
UPDATE_CADENCE = datetime.timedelta(minutes=45)

# Profiles to update
PROFILES=["Default"]

# Themes you would like to cycle through, make sure they match the names in iTerm color presets
THEMES = [
	'Belafonte Day', 
	'Belafonte Night', 
	'BirdsOfParadise', 
	'Desert', 
	'Espresso', 
	'LiquidCarbon', 
	'Purple Rain', 
	'Solarized Darcula', 
	'SpaceGray Eighties Dull', 
	'SpaceGray'
	]


def get_random_theme():
	return random.choice(THEMES)

async def set_colors(connection, preset_name):
    print("Changed to preset {}".format(preset_name))
    preset = await iterm2.ColorPreset.async_get(connection, preset_name)
    for partial in (await iterm2.PartialProfile.async_query(connection)):
        if partial.name in PROFILES:
            await partial.async_set_color_preset(preset)

async def main(connection):
    while True:
        new_preset = get_random_theme()
        print(f"Updating theme in {UPDATE_CADENCE.seconds/60} minutes")
        await asyncio.sleep(UPDATE_CADENCE.seconds)
        await set_colors(connection, new_preset)
        await asyncio.sleep(1)

iterm2.run_forever(main)
