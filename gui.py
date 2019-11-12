import wx
from game_master import *


board_name = ['button_0', 'button_1', 'button_2', 'button_3', 'button_4', 'button_5', 'button_6', 'button_7',
              'button_8', 'button_9', 'button_10', 'button_11', 'button_12', 'button_13', 'button_14', 'button_15',
              'button_16', 'button_17', 'button_18', 'button_19', 'button_20', 'button_21', 'button_22', 'button_23',
              'button_24', 'button_25', 'button_26', 'button_27', 'button_28', 'button_29', 'button_30', 'button_31',
              'button_32', 'button_33', 'button_34', 'button_35', 'button_36', 'button_37', 'button_38', 'button_39',
              'button_40', 'button_41', 'button_42', 'button_43', 'button_44', 'button_45', 'button_46', 'button_47',
              'button_48', 'button_49', 'button_50', 'button_51', 'button_52', 'button_53', 'button_54', 'button_55',
              'button_56', 'button_57', 'button_58', 'button_59', 'button_60', 'button_61', 'button_62', 'button_63',
              ]

class Main_Frame(wx.Frame):

    def __init__(self):
        super().__init__(None, wx.ID_ANY, 'reversi', size=(1500, 700))
        self.board_Panel = wx.Panel(self, wx.ID_ANY, pos=(0, 0), size=(560, 560))
        self.board_Panel.SetBackgroundColour('#191970')
        self.control_Panel = wx.Panel(self, wx.ID_ANY, pos=(560, 0))
        self.control_Panel.SetBackgroundColour('#ffff00')

        layout_board = wx.FlexGridSizer(rows=8, cols=8, gap=(0, 0))

        button_0 = wx.Button(self.board_Panel, wx.ID_ANY, '0', size=(70, 70))
        button_1 = wx.Button(self.board_Panel, wx.ID_ANY, '1', size=(70, 70))
        button_2 = wx.Button(self.board_Panel, wx.ID_ANY, '2', size=(70, 70))
        button_3 = wx.Button(self.board_Panel, wx.ID_ANY, '3', size=(70, 70))
        button_4 = wx.Button(self.board_Panel, wx.ID_ANY, '4', size=(70, 70))
        button_5 = wx.Button(self.board_Panel, wx.ID_ANY, '5', size=(70, 70))
        button_6 = wx.Button(self.board_Panel, wx.ID_ANY, '6', size=(70, 70))
        button_7 = wx.Button(self.board_Panel, wx.ID_ANY, '7', size=(70, 70))
        button_8 = wx.Button(self.board_Panel, wx.ID_ANY, '8', size=(70, 70))
        button_9 = wx.Button(self.board_Panel, wx.ID_ANY, '9', size=(70, 70))
        button_10 = wx.Button(self.board_Panel, wx.ID_ANY, '10', size=(70, 70))
        button_11 = wx.Button(self.board_Panel, wx.ID_ANY, '11', size=(70, 70))
        button_12 = wx.Button(self.board_Panel, wx.ID_ANY, '12', size=(70, 70))
        button_13 = wx.Button(self.board_Panel, wx.ID_ANY, '13', size=(70, 70))
        button_14 = wx.Button(self.board_Panel, wx.ID_ANY, '14', size=(70, 70))
        button_15 = wx.Button(self.board_Panel, wx.ID_ANY, '15', size=(70, 70))
        button_16 = wx.Button(self.board_Panel, wx.ID_ANY, '16', size=(70, 70))
        button_17 = wx.Button(self.board_Panel, wx.ID_ANY, '17', size=(70, 70))
        button_18 = wx.Button(self.board_Panel, wx.ID_ANY, '18', size=(70, 70))
        button_19 = wx.Button(self.board_Panel, wx.ID_ANY, '19', size=(70, 70))
        button_20 = wx.Button(self.board_Panel, wx.ID_ANY, '20', size=(70, 70))
        button_21 = wx.Button(self.board_Panel, wx.ID_ANY, '21', size=(70, 70))
        button_22 = wx.Button(self.board_Panel, wx.ID_ANY, '22', size=(70, 70))
        button_23 = wx.Button(self.board_Panel, wx.ID_ANY, '23', size=(70, 70))
        button_24 = wx.Button(self.board_Panel, wx.ID_ANY, '24', size=(70, 70))
        button_25 = wx.Button(self.board_Panel, wx.ID_ANY, '25', size=(70, 70))
        button_26 = wx.Button(self.board_Panel, wx.ID_ANY, '26', size=(70, 70))
        button_27 = wx.Button(self.board_Panel, wx.ID_ANY, '27', size=(70, 70))
        button_28 = wx.Button(self.board_Panel, wx.ID_ANY, '28', size=(70, 70))
        button_29 = wx.Button(self.board_Panel, wx.ID_ANY, '29', size=(70, 70))
        button_30 = wx.Button(self.board_Panel, wx.ID_ANY, '30', size=(70, 70))
        button_31 = wx.Button(self.board_Panel, wx.ID_ANY, '31', size=(70, 70))
        button_32 = wx.Button(self.board_Panel, wx.ID_ANY, '32', size=(70, 70))
        button_33 = wx.Button(self.board_Panel, wx.ID_ANY, '33', size=(70, 70))
        button_34 = wx.Button(self.board_Panel, wx.ID_ANY, '34', size=(70, 70))
        button_35 = wx.Button(self.board_Panel, wx.ID_ANY, '35', size=(70, 70))
        button_36 = wx.Button(self.board_Panel, wx.ID_ANY, '36', size=(70, 70))
        button_37 = wx.Button(self.board_Panel, wx.ID_ANY, '37', size=(70, 70))
        button_38 = wx.Button(self.board_Panel, wx.ID_ANY, '38', size=(70, 70))
        button_39 = wx.Button(self.board_Panel, wx.ID_ANY, '39', size=(70, 70))
        button_40 = wx.Button(self.board_Panel, wx.ID_ANY, '40', size=(70, 70))
        button_41 = wx.Button(self.board_Panel, wx.ID_ANY, '41', size=(70, 70))
        button_42 = wx.Button(self.board_Panel, wx.ID_ANY, '42', size=(70, 70))
        button_43 = wx.Button(self.board_Panel, wx.ID_ANY, '43', size=(70, 70))
        button_44 = wx.Button(self.board_Panel, wx.ID_ANY, '44', size=(70, 70))
        button_45 = wx.Button(self.board_Panel, wx.ID_ANY, '45', size=(70, 70))
        button_46 = wx.Button(self.board_Panel, wx.ID_ANY, '46', size=(70, 70))
        button_47 = wx.Button(self.board_Panel, wx.ID_ANY, '47', size=(70, 70))
        button_48 = wx.Button(self.board_Panel, wx.ID_ANY, '48', size=(70, 70))
        button_49 = wx.Button(self.board_Panel, wx.ID_ANY, '49', size=(70, 70))
        button_50 = wx.Button(self.board_Panel, wx.ID_ANY, '50', size=(70, 70))
        button_51 = wx.Button(self.board_Panel, wx.ID_ANY, '51', size=(70, 70))
        button_52 = wx.Button(self.board_Panel, wx.ID_ANY, '52', size=(70, 70))
        button_53 = wx.Button(self.board_Panel, wx.ID_ANY, '53', size=(70, 70))
        button_54 = wx.Button(self.board_Panel, wx.ID_ANY, '54', size=(70, 70))
        button_55 = wx.Button(self.board_Panel, wx.ID_ANY, '55', size=(70, 70))
        button_56 = wx.Button(self.board_Panel, wx.ID_ANY, '56', size=(70, 70))
        button_57 = wx.Button(self.board_Panel, wx.ID_ANY, '57', size=(70, 70))
        button_58 = wx.Button(self.board_Panel, wx.ID_ANY, '58', size=(70, 70))
        button_59 = wx.Button(self.board_Panel, wx.ID_ANY, '59', size=(70, 70))
        button_60 = wx.Button(self.board_Panel, wx.ID_ANY, '60', size=(70, 70))
        button_61 = wx.Button(self.board_Panel, wx.ID_ANY, '61', size=(70, 70))
        button_62 = wx.Button(self.board_Panel, wx.ID_ANY, '62', size=(70, 70))
        button_63 = wx.Button(self.board_Panel, wx.ID_ANY, '63', size=(70, 70))

        button_start = wx.Button(self.control_Panel, wx.ID_ANY, 'START', size=(150, 30))

        board_name = [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7,
                      button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15,
                      button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23,
                      button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31,
                      button_32, button_33, button_34, button_35, button_36, button_37, button_38, button_39,
                      button_40, button_41, button_42, button_43, button_44, button_45, button_46, button_47,
                      button_48, button_49, button_50, button_51, button_52, button_53, button_54, button_55,
                      button_56, button_57, button_58, button_59, button_60, button_61, button_62,  button_63,
                      ]
        for button_name in board_name:
            button_name.SetBackgroundColour('#228b22')
            layout_board.Add(button_name)
        self.board_Panel.SetSizer(layout_board)


reversi = wx.App()
Main_Frame = Main_Frame()
Main_Frame.Show()
reversi.MainLoop()