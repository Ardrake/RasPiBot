#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import wx
#import RasPiBot

### Test servo screen
servo_list = [["Head", 90], ["Neck", 90], ["Left shoulder", 90], ["Left bicep", 90],
              ["Left hand", 90], ["Left hip", 90], ["Left knee", 90], ["Left ankle", 90],
              ["Right shoulder", 90], ["Right bicep", 90], ["Right hand", 90], ["Right hip", 90],
              ["Right knee", 90]]

change_value = 1

class ServoButton(wx.Button):
    def __init__(self, servo_id, servo_pos, logger, change, *args, **kwargs):
        wx.Button.__init__(self, *args, **kwargs)
        self.servo_id = servo_id
        self.servo_pos = servo_pos
        self.logger = logger
        self.change = change_value

    def OnButton(self, e):
        print("Clicked '%s'" % self.servo_id)

        def get_index(list, searchstr):
            return [y[0] for y in list].index(searchstr)

        if self.servo_id[-2:] == "up":
            print("UP")
            servo_name = self.servo_id[:(len(self.servo_id) - 3)]
            myindex = get_index(servo_list, servo_name)
            servo_list[myindex][1] += self.change
            direction = '+'

        else:
            print("DOWN")
            servo_name = self.servo_id[:(len(self.servo_id) - 5)]
            myindex = get_index(servo_list, servo_name)
            servo_list[myindex][1] -= self.change
            direction = '-'

        self.logger.AppendText(" Click on {} - pos = {} {} {} = {}\n".format(self.servo_id, str(self.servo_pos), direction, self.change, servo_list[myindex][1]))


class MyRobotUi(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(700, 800))

        BUTTON_SIZE = (120, 30); X1_POS = 50; X2_POS = 180; Y_POS = 40

        self.panel = wx.Panel(self, pos=(X1_POS, Y_POS))
        self.panel2 = wx.Panel(self, pos=(X2_POS, Y_POS))
        self.radiopanel = wx.Panel(self, pos=(50, 05), size=(250, 30))

        self.rb1 = wx.RadioButton(self.radiopanel, -1, '1 degré', (10, 7), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(self.radiopanel, -1, '5 degré', (90, 7))
        self.rb3 = wx.RadioButton(self.radiopanel, -1, '10 degré', (170, 7))

        self.buttons = []

        self.logger = wx.TextCtrl(self, pos=(370, 20), size=(300, 600), style=wx.TE_MULTILINE | wx.TE_READONLY)

        for servo in servo_list:
            mybutton = ServoButton(servo_id=str(servo[0]) + " up", servo_pos=servo[1], change=1, parent=self.panel, label=str(servo[0])+" up", size=BUTTON_SIZE, logger=self.logger)
            mybutton.Bind(wx.EVT_BUTTON, mybutton.OnButton)
            self.buttons.append(mybutton)

        self.sizer_ver = wx.BoxSizer(wx.VERTICAL)
        for button in self.buttons:
            self.sizer_ver.Add(button)
        self.panel.SetSizerAndFit(self.sizer_ver)

        self.buttons = []
        for servo in servo_list:
            mybutton = ServoButton(servo_id=str(servo[0]) + " down", servo_pos=servo[1], change=1, parent=self.panel2, label=str(servo[0]) + " down", size=BUTTON_SIZE, logger=self.logger)
            mybutton.Bind(wx.EVT_BUTTON, mybutton.OnButton)
            self.buttons.append(mybutton)

        self.sizer_ver_02 = wx.BoxSizer(wx.VERTICAL)
        for button in self.buttons:
            self.sizer_ver_02.Add(button)
        self.panel2.SetSizerAndFit(self.sizer_ver_02)

        self.CreateStatusBar()  # A Statusbar in the bottom of the window

        # Setting up the menu
        filemenu = wx.Menu()

        menu_item_about = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.AppendSeparator()
        menu_item_exit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)

        # set events
        self.Bind(wx.EVT_MENU, self.on_about, menu_item_about)
        self.Bind(wx.EVT_MENU, self.on_exit, menu_item_exit)

        self.Show(True)

    def on_about(self, e):
        print("On about clicked")
        dlg = wx.MessageDialog(self, "About RasPiBot was clicked", "About", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    def on_exit(self, e):
        self.Close(True)  # Close the frame.

    def click_on(self, event):
        name = event.GetEventObject().bname
        self.logger.AppendText(" Click on object with Id {} {} \n".format(event.GetId(), name))


app = wx.App(False)
frame = MyRobotUi(None, 'Robot UI')
app.MainLoop()
