# searchPanel
Use Surfraw by highlighting your word(s) and pressing a hotkey to type in the Elvis you want to search with

## Usage
- Download the `searchPanel` file and store it somewhere that makes sense for you.
- Download [surfraw](https://gitlab.com/surfraw/Surfraw) or download the updated version that I've included (you'll need to place these files in `/usr/lib/surfraw` or update the location in the script (should be line 3).
- Download [dmenu](https://github.com/stilvoid/dmenu) (fair warning, I don't remember if I downloaded this from here. You may need to play with it if it doesn't work.)
- Pending your OS find out how to assign a hotkey to run a script. [For Ubuntu:](https://techwiser.com/custom-keyboard-shortcuts-ubuntu/)
- Consume massive amounts of knowledge at UNPARALLED SPEEDS.
- Note: I've made my own elvi which I store and then symlink to be read by surfraw. If you'd like to do the same, all you need to do is add the custom elvi to the elvi folder and then create the link with `ln -s /path/to/where/you/downloaded/ ~/.config/surfraw/`. 
    - You can confirm your custom elvi are being recognized by typing `sr -elvi` which will display your customs at the very bottom.
