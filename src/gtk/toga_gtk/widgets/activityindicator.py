from ..libs import Gtk
from .base import Widget


class ActivityIndicator(Widget):

    def create(self):
        self.native = Gtk.Spinner()
        self.native.interface = self.interface

    def set_hide_when_stopped(self, value):
        self.interface.factory.not_implemented('ActivityIndicator.set_hide_when_stopped()')

    def start(self):
        self.native.start()

    def stop(self):
        self.native.stop()
