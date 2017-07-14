#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import wx
#import RasPiBot

### Test servo screen
servo_list = [["Head", 90], ["Neck", 90], ["Left shoulder", 90], ["Left bicep", 90],
              ["Left hand", 90], ["Left hip", 90], ["Left knee", 90], ["Left ankle", 90],
              ["Right shoulder", 90], ["Right bicep", 90], ["Right hand", 90], ["Right hip", 90],
              ["Right knee", 90]]


class ServoButton(wx.Button):
    def __init__(self, servo_id, servo_pos, myframe, *args, **kwargs):
        wx.Button.__init__(self, *args, **kwargs)
        self.servo_id = servo_id
        self.servo_pos = servo_pos
        self.frame = myframe
        self.logger = myframe.logger
        self.change = myframe.my_change_val

    def OnButton(self, e):
        def get_index(list, searchstr):
            return [y[0] for y in list].index(searchstr)

        def update_val(index):
            if index == 0:
                frame.servo_val_0.SetValue(str(servo_list[0][1]))
            if index == 1:
                frame.servo_val_1.SetValue(str(servo_list[1][1]))
            if index == 2:
                frame.servo_val_2.SetValue(str(servo_list[2][1]))
            if index == 3:
                frame.servo_val_3.SetValue(str(servo_list[3][1]))
            if index == 4:
                frame.servo_val_4.SetValue(str(servo_list[4][1]))
            if index == 5:
                frame.servo_val_5.SetValue(str(servo_list[5][1]))
            if index == 6:
                frame.servo_val_6.SetValue(str(servo_list[6][1]))
            if index == 7:
                frame.servo_val_7.SetValue(str(servo_list[7][1]))
            if index == 8:
                frame.servo_val_8.SetValue(str(servo_list[8][1]))
            if index == 9:
                frame.servo_val_9.SetValue(str(servo_list[9][1]))
            if index == 10:
                frame.servo_val_10.SetValue(str(servo_list[10][1]))
            if index == 11:
                frame.servo_val_11.SetValue(str(servo_list[11][1]))
            if index == 12:
                frame.servo_val_12.SetValue(str(servo_list[12][1]))

        if self.servo_id[-2:] == "up":
            servo_name = self.servo_id[:(len(self.servo_id) - 3)]
            myindex = get_index(servo_list, servo_name)
            servo_list[myindex][1] += frame.my_change_val
            direction = '+'
            update_val(myindex)

        else:
            servo_name = self.servo_id[:(len(self.servo_id) - 5)]
            myindex = get_index(servo_list, servo_name)
            servo_list[myindex][1] -= frame.my_change_val
            direction = '-'
            update_val(myindex)

        self.logger.AppendText(" Click on {} - pos = {} {} {} = {}\n".format(self.servo_id, str(self.servo_pos), direction, frame.my_change_val, servo_list[myindex][1]))


class MyRobotUi(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(700, 800))

        BUTTON_SIZE = (120, 30); X1_POS = 50; X2_POS = 180; Y_POS = 40

        self.panel = wx.Panel(self, pos=(X1_POS, Y_POS)) # up button panel
        self.panel2 = wx.Panel(self, pos=(X2_POS, Y_POS)) # down button panel
        self.panel3 = wx.Panel(self, pos=(310, 40)) # serva value panel
        self.panel3.SetBackgroundColour('LIGHT GREY')
        self.radiopanel = wx.Panel(self, pos=(50, 05), size=(250, 30))

        self.rb1 = wx.RadioButton(self.radiopanel, -1, '1 degré', (10, 7), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(self.radiopanel, -1, '5 degré', (90, 7))
        self.rb3 = wx.RadioButton(self.radiopanel, -1, '10 degré', (170, 7))

        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)

        my_input_size = (50, 24)
        self.servo_val_0 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[0][1]))
        self.servo_val_1 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[1][1]))
        self.servo_val_2 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[2][1]))
        self.servo_val_3 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[3][1]))
        self.servo_val_4 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[4][1]))
        self.servo_val_5 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[5][1]))
        self.servo_val_6 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[6][1]))
        self.servo_val_7 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[7][1]))
        self.servo_val_8 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[8][1]))
        self.servo_val_9 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                       value=str(servo_list[9][1]))
        self.servo_val_10 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                        value=str(servo_list[10][1]))
        self.servo_val_11 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                        value=str(servo_list[11][1]))
        self.servo_val_12 = wx.TextCtrl(self.panel3, size=my_input_size, style=wx.TE_READONLY,
                                        value=str(servo_list[12][1]))

        self.sizer_ver_03 = wx.BoxSizer(wx.VERTICAL)
        myborder = 3.2
        self.sizer_ver_03.Add(self.servo_val_0, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_1, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_2, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_3, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_4, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_5, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_6, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_7, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_8, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_9, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_10, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_11, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.sizer_ver_03.Add(self.servo_val_12, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=myborder)
        self.panel3.SetSizerAndFit(self.sizer_ver_03)

        self.logger = wx.TextCtrl(self, pos=(370, 20), size=(300, 600), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.my_change_val = 1

        self.buttons = []

        for servo in servo_list:
            mybutton = ServoButton(servo_id=str(servo[0]) + " up", servo_pos=servo[1], parent=self.panel,
                                   label=str(servo[0])+" up", size=BUTTON_SIZE, myframe=self)
            mybutton.Bind(wx.EVT_BUTTON, mybutton.OnButton)
            self.buttons.append(mybutton)

        self.sizer_ver = wx.BoxSizer(wx.VERTICAL)

        for button in self.buttons:
            self.sizer_ver.Add(button)
        self.panel.SetSizerAndFit(self.sizer_ver)

        self.buttons = []
        for servo in servo_list:
            mybutton = ServoButton(servo_id=str(servo[0]) + " down", servo_pos=servo[1], parent=self.panel2,
                                   label=str(servo[0]) + " down", size=BUTTON_SIZE, myframe=self)
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

    def OnRadiogroup(self, e):
        rb = e.GetEventObject()
        myval = int(rb.GetLabel()[:2].strip())
        self.my_change_val = myval
        self.logger.AppendText(" changé valeur a {} \n".format(myval))


app = wx.App(False)
frame = MyRobotUi(None, 'Robot UI')
app.MainLoop()
