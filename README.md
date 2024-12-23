# fpww_roster_builder
Use python to create a simple static webpage in html for your e-fed.\
To see an example: https://leenoah390.github.io/roster.html

## Pre-steps:
1. Must have Python installed (at the very least, version 3.8) along with an IDE
   1. *I used Anaconda Spyder*
3. Have a folder containing images of your wrestlers
4. Download `file_names.py` and `roster_creator.py`, then move both files into your image folder described in (2)
5. Knowledge of html is helpful
---
## How to use:
1. Open `file_names.py`.
2. Update the **path** variable.
3. **irr** is a list that is to contain all non-wrestler images in your path's folder. For example, in my path, I had to ignore:
    1. Other `.html` files used for my main website
    2. `.png` files for my belt graphics
    3. `.py` files used for creating the final roster
    4. Basically, it there is anything in your path/folder that is not a wrestler's image file, then list it inside the **irr** list.
4. Save the changes, then open `roster_creator.py`.
5. Edit line 60 to a header of your choosing.
6. **[OPTIONAL]** Edit any other changes.
    1. I have my current website set up to have rows of *10* wrestler images per row, with a a total width of *1440* units.
    2. To change how many wrestlers per row, change the `n` value (line 19)
    3. Remember to edit the `<td width="10%"...` if you want to make any changes look better (line 32)
    4. Might have to change the `WIDTH=...` as well (line 25)
    5. All my images are set to 128*128 pixels
    6. Other website stuff like background, text color / size, etc.
7. Run `roster_creator.py`, and an html file titled *`roster.html`* should pop up.
