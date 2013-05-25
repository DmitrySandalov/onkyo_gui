onkyo_gui
=========

PyGTK GUI for Onkyo AV receivers

![alt tag](https://raw.github.com/DmitrySandalov/onkyo_gui/master/screenshots/scr1.png)

* Launch the tool with `python main.py` (change IP in main function)

* This gui can be easily modified :)
    * Open the comprehensive list of commands in onkyo_gui/util
    * Add commands to onkyo_gui/eiscp/onkyo_raw_commands.txt
    * Generate py file with `python raw_commands_massager.py onkyo_raw_commands.txt > commands.py`
    * Modify the main.py file

* Tested on Ubuntu 13.04 with Onkyo TX-NR515 receiver (but should work with other receivers)

* Based on https://github.com/compbrain/Onkyo-TX-NR708-Control/ 
