#!/usr/bin/env python

import gtk
import pygtk
import eiscp
pygtk.require('2.0')


class Receiver():

    def callback(self, widget, data):
        self.receiver.writeCommandFromName(data)
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

        box_volume = gtk.HBox(True, 0)
        vol_up = gtk.Button("Volume Up")
        vol_up.connect("clicked", self.callback, "Volume Up")
        box_volume.pack_start(vol_up, True, True, 0)
        vol_up.show()
        vol_down = gtk.Button("Volume Down")
        vol_down.connect("clicked", self.callback, "Volume Down")
        box_volume.pack_start(vol_down, True, True, 0)
        vol_down.show()
        box_volume.show()

        box_power = gtk.HBox(True, 0)
        vol_up = gtk.Button("Power ON")
        vol_up.connect("clicked", self.callback, "Power ON")
        box_power.pack_start(vol_up, True, True, 0)
        vol_up.show()
        vol_down = gtk.Button("Power OFF")
        vol_down.connect("clicked", self.callback, "Power OFF")
        box_power.pack_start(vol_down, True, True, 0)
        vol_down.show()
        box_power.show()

        box_mute = gtk.HBox(True, 0)
        vol_up = gtk.Button("Mute")
        vol_up.connect("clicked", self.callback, "Mute")
        box_mute.pack_start(vol_up, True, True, 0)
        vol_up.show()
        vol_down = gtk.Button("UnMute")
        vol_down.connect("clicked", self.callback, "UnMute")
        box_mute.pack_start(vol_down, True, True, 0)
        vol_down.show()
        box_mute.show()

        box.pack_start(box_power, True, True, 0)
        box.pack_start(box_volume, True, True, 0)
        box.pack_start(box_mute, True, True, 0)

        self.window.add(box)
        box.show()
        self.window.show()


def main():
    receiver = eiscp.eISCP('192.168.1.68')
    Receiver(receiver)
    gtk.main()

if __name__ == "__main__":
    main()
