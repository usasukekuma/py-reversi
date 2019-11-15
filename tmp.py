import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Title", size=(300,350))
        self.InitializeComponents()


    def InitializeComponents(self):
        mainPanel = wx.Panel(self)
        mainPanel.SetBackgroundColour("LIGHT BLUE")
        panel1 = wx.Panel(mainPanel, pos=(0,0), size=(150,150))
        panel1.SetBackgroundColour("GREEN")
        panel2 = wx.Panel(mainPanel, pos=(150,0), size=(150,150))
        panel2.SetBackgroundColour("BLUE")
        button_0 = wx.Button(panel1, wx.ID_ANY, '0' )
        button_1 = wx.Button(panel1, wx.ID_ANY, '1' )
        sizer = wx.FlexGridSizer(1,2,0,0)
        sizer.Add(button_1)
        sizer.Add(button_0)
        mainPanel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()