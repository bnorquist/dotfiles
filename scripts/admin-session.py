#!~/Envs/dev/bin/python

import iterm2


async def main(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    change = iterm2.LocalWriteOnlyProfile()
    tab_color = iterm2.Color(255, 153, 51)
    background_color = iterm2.Color(100, 0, 0)
    change.set_tab_color(tab_color)
    change.set_use_tab_color(True)
    change.set_background_color(background_color)
    await session.async_set_profile_properties(change)

iterm2.run_until_complete(main)
