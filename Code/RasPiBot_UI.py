import wx
import RasPiBot


class ServoButton(wx.Button):
    def __init__(self, servo_id, logger, *args, **kwargs):
        wx.Button.__init__(self, *args, **kwargs)
        self.servo_id = servo_id
        self.logger = logger

    def OnButton(self, e):
        print("Clicked '%s'" % self.servo_id)
        self.logger.AppendText(" Click on {} \n".format(self.servo_id))


class MyRobotUi(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 800))

        BUTTON_SIZE = (120, 30); X1_POS = 50; X2_POS = 180; Y_POS = 40

        self.panel = wx.Panel(self, pos=(X1_POS, Y_POS))
        self.panel2 = wx.Panel(self, pos=(X2_POS, Y_POS))
        self.buttons = []

        self.logger = wx.TextCtrl(self, pos=(370, 20), size=(200, 600), style=wx.TE_MULTILINE | wx.TE_READONLY)

        servo_list = ("Head", "Neck", "Left shoulder", "Left bicep", "Left hand", "Left hip", "Left knee", "Left ankle",
                      "Right shoulder", "Right bicep", "Right hand", "Right hip", "Right knee", "Right ankle")

        for servo in servo_list:
            mybutton = ServoButton(servo_id=str(servo) + " up", parent=self.panel, label=str(servo)+" up", size=BUTTON_SIZE, logger=self.logger)
            mybutton.Bind(wx.EVT_BUTTON, mybutton.OnButton)
            self.buttons.append(mybutton)

        self.sizer_ver = wx.BoxSizer(wx.VERTICAL)
        for button in self.buttons:
            self.sizer_ver.Add(button)
        self.panel.SetSizerAndFit(self.sizer_ver)

        self.buttons = []
        for servo in servo_list:
            mybutton = ServoButton(servo_id=str(servo) + " down", parent=self.panel2, label=str(servo) + " down", size=BUTTON_SIZE, logger=self.logger)
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
