import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Vigilant-DragonWindow(Gtk.Window)
     def _init_(self):
         Gtk.Window._init_(self, title="Vigilant-Dragon v1.0")
         self.set_border_width(10)
         
         hbox = Gtk.Box(spacing=6)
         self.add(hbox)
         
         button = Gtk.Button.new_with_label("Scan")
         button.connect("clicked", self.on_scan_clicked)
         hbox.pack_start(button , True, True, 0)
         
         
        button = Gtk.Button.new_with_mnemonic("Quarantine")
        button.connect("clicked", self.on_quarantine_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Close and quit")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_scan_clicked(self, button):
        print('"SCANNING...." Viruses DETected at .BigBEEFS/tools/metasploit-framework')

    def on_quarantine_clicked(self, button):
        print('"Quarant :"Viruses. etc')

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()


win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
         
         
