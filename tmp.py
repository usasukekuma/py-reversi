import wx

class reversiGUI(wx.Frame):
    def __init__(self):
        super(reversiGUI,self).__init__()
        self.first_ui()


    def first_ui(self):
        frame = wx.Frame(None, -1, 'Hello,World!',size=(1500,800))
        frame.SetTitle('オセロ')
        frame.Show()


app = wx.App
reversiGUI()
app.MainLoop()