#!/usr/bin/env python

import gtk
import pygtk
import eiscp
pygtk.require('2.0')


class Receiver():

    def callback(self, widget, data):
        self.receiver.writeCommand(data)
        print "%s" % data

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self, receiver):
        self.receiver = receiver

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Onkyo Control")
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(10)

        box = gtk.VBox(False, 0)
        box_1 = gtk.HBox(True, 0)
        box_2 = gtk.HBox(True, 0)
        box_3 = gtk.HBox(True, 0)
        box_4 = gtk.HBox(True, 0)
        box_5 = gtk.HBox(True, 0)

        # box_1
        pow_on = gtk.Button("Power ON")
        pow_on.connect("clicked", self.callback, "PWR01")
        box_1.pack_start(pow_on, True, True, 0)
        pow_on.show()

        mute = gtk.Button("Mute")
        mute.connect("clicked", self.callback, "AMT01")
        box_1.pack_start(mute, True, True, 0)
        mute.show()

        vol_up = gtk.Button("Volume Up")
        vol_up.connect("clicked", self.callback, "MVLUP")
        box_1.pack_start(vol_up, True, True, 0)
        vol_up.show()

        src_pc = gtk.Button("PC")
        src_pc.connect("clicked", self.callback, "SLI05")
        box_1.pack_start(src_pc, True, True, 0)
        src_pc.show()

        # box_2
        pow_on = gtk.Button("Power OFF")
        pow_on.connect("clicked", self.callback, "PWR00")
        box_2.pack_start(pow_on, True, True, 0)
        pow_on.show()

        mute = gtk.Button("UnMute")
        mute.connect("clicked", self.callback, "AMT00")
        box_2.pack_start(mute, True, True, 0)
        mute.show()

        vol_up = gtk.Button("Volume Down")
        vol_up.connect("clicked", self.callback, "MVLDOWN")
        box_2.pack_start(vol_up, True, True, 0)
        vol_up.show()

        src_pc = gtk.Button("FM")
        src_pc.connect("clicked", self.callback, "SLI24")
        box_2.pack_start(src_pc, True, True, 0)
        src_pc.show()

        # box_3
        pow_on = gtk.Button("Display")
        pow_on.connect("clicked", self.callback, "DIFTG")
        box_3.pack_start(pow_on, True, True, 0)
        pow_on.show()

        mute = gtk.Button("Up")
        mute.connect("clicked", self.callback, "OSDUP")
        box_3.pack_start(mute, True, True, 0)
        mute.show()

        vol_up = gtk.Button("Menu")
        vol_up.connect("clicked", self.callback, "OSDMENU")
        box_3.pack_start(vol_up, True, True, 0)
        vol_up.show()

        src_pc = gtk.Button("Internet Radio")
        src_pc.connect("clicked", self.callback, "SLI28")
        box_3.pack_start(src_pc, True, True, 0)
        src_pc.show()

        # box_4
        pow_on = gtk.Button("Left")
        pow_on.connect("clicked", self.callback, "ODFLEFT")
        box_4.pack_start(pow_on, True, True, 0)
        pow_on.show()

        mute = gtk.Button("Enter")
        mute.connect("clicked", self.callback, "OSDENTER")
        box_4.pack_start(mute, True, True, 0)
        mute.show()

        vol_up = gtk.Button("Right")
        vol_up.connect("clicked", self.callback, "OSDRIGHT")
        box_4.pack_start(vol_up, True, True, 0)
        vol_up.show()

        src_pc = gtk.Button("Next Source")
        src_pc.connect("clicked", self.callback, "SLIUP")
        box_4.pack_start(src_pc, True, True, 0)
        src_pc.show()

        # box_5
        pow_on = gtk.Button("Home")
        pow_on.connect("clicked", self.callback, "OSDHOME")
        box_5.pack_start(pow_on, True, True, 0)
        pow_on.show()

        mute = gtk.Button("Down")
        mute.connect("clicked", self.callback, "OSDDOWN")
        box_5.pack_start(mute, True, True, 0)
        mute.show()

        vol_up = gtk.Button("Exit")
        vol_up.connect("clicked", self.callback, "OSDEXIT")
        box_5.pack_start(vol_up, True, True, 0)
        vol_up.show()

        src_pc = gtk.Button("Previous Source")
        src_pc.connect("clicked", self.callback, "SLIDOWN")
        box_5.pack_start(src_pc, True, True, 0)
        src_pc.show()

        box.pack_start(box_1, True, True, 0)
        box.pack_start(box_2, True, True, 0)
        box.pack_start(box_3, True, True, 0)
        box.pack_start(box_4, True, True, 0)
        box.pack_start(box_5, True, True, 0)
        box_1.show()
        box_2.show()
        box_3.show()
        box_4.show()
        box_5.show()

        self.window.add(box)
        box.show()
        self.window.show()


def main():
    receiver = eiscp.eISCP('192.168.1.68')
    Receiver(receiver)
    gtk.main()

if __name__ == "__main__":
    main()
