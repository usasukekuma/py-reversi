import wx
from game_master import *


class Main_Frame(wx.Frame):

    def __init__(self):
        self.gui_turn = 0
        self.vs = self.for_ch
        self.selection = ('model','random')

        self.for_convert = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
                            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                            (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
                            (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                            (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                            (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

        wx.Frame.__init__(self, None, wx.ID_ANY, 'Reversi', size=(728, 700))
        icon = wx.Icon('img/icon.ico', wx.BITMAP_TYPE_ICO)
        wx.Frame.SetIcon(self, icon)
        self.main_Panel = wx.Panel(self)
        self.board_Panel = wx.Panel(self.main_Panel, pos=(0, 0), size=(560, 560))
        self.control_Panel = wx.Panel(self.main_Panel, pos=(560, 0), size=(560, 700))
        self.control_Panel.SetBackgroundColour('#7fbfff')
        self.status_Panel = wx.Panel(self.main_Panel, pos=(0, 560), size=(560, 140))
        self.status_Panel.SetBackgroundColour('#8484ff')
        self.othello = game_master()
        self.board_make()
        self.make_status()
        self.make_control()

        main_layout = wx.GridBagSizer()
        main_layout.Add(self.board_Panel, (0, 0), (1, 1))
        main_layout.Add(self.control_Panel, (0, 1), (2, 1))
        main_layout.Add(self.status_Panel, (1, 0), (1, 1))
        main_layout.AddGrowableRow(0)
        main_layout.AddGrowableRow(1)
        main_layout.AddGrowableCol(0)
        main_layout.AddGrowableCol(1)
        self.main_Panel.SetSizer(main_layout)

        self.board_color_update()


    def board_make(self):
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
        self.board_name = [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7,
                           button_8, button_9, button_10, button_11, button_12, button_13, button_14,button_15,
                           button_16, button_17, button_18, button_19, button_20,button_21, button_22, button_23,
                           button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31,
                           button_32, button_33, button_34, button_35, button_36, button_37, button_38, button_39,
                           button_40, button_41, button_42, button_43,button_44, button_45, button_46, button_47,
                           button_48, button_49, button_50, button_51, button_52, button_53, button_54, button_55,
                           button_56, button_57, button_58, button_59, button_60, button_61, button_62, button_63,
                           ]
        dict_reg = 0
        layout_board = wx.FlexGridSizer(8, 8, 0, 0)
        for button_name in self.board_name:
            button_name.SetBackgroundColour('#228b22')
            button_name.SetForegroundColour('#bc8f8f')
            button_name.Bind(wx.EVT_BUTTON, self.vs)
            button_name.Disable()
            layout_board.Add(button_name)
            dict_reg += 1
        self.board_Panel.SetSizer(layout_board)

    def make_control(self):
        control_layout = wx.BoxSizer(wx.VERTICAL)
        text1 = wx.StaticText(self.control_Panel, wx.ID_ANY, '戦う相手', size=(150, 30))
        text1.SetFont(wx.Font(20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.button_start = wx.Button(self.control_Panel, wx.ID_ANY, 'START', size=(150, 70))
        self.button_start.SetBackgroundColour('#ffe4b5')
        self.button_start.Bind(wx.EVT_BUTTON, self.click_start)
        self.selectin_box = wx.ComboBox(self.control_Panel, wx.ID_ANY, '選択してください',
                                   choices=self.selection, style=wx.CB_READONLY, size=(150, 30))
        self.selectin_box.SetFont(wx.Font(20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.selectin_box.SetSelection(0)
        self.WINNER = wx.StaticText(self.control_Panel, wx.ID_ANY, '', size=(150, 70), style=wx.TE_CENTER)
        self.WINNER.SetBackgroundColour('#20b2aa')
        self.WINNER.SetFont(wx.Font(28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        control_layout.Add(text1)
        control_layout.Add(self.selectin_box)
        control_layout.Add(self.button_start)
        control_layout.Add(self.WINNER)
        self.control_Panel.SetSizer(control_layout)

    def click_start(self, a):
        self.button_start.Disable()
        self.button_enable(BLACK)
        select_p = self.selectin_box.GetStringSelection()
        if select_p == 'model':
            px, py = ch_multi_player(self.othello.can_put_list(BLACK), [self.othello.board], 'LOSER')
            self.othello.put_stone(px, py, BLACK)
            self.board_color_update()
            self.button_enable(WHITE)
            self.gui_turn += 1

        elif select_p == 'random':
            px, py = random_action(self.othello.can_put_list(BLACK), 0, 0)
            self.othello.put_stone(px, py, BLACK)
            self.board_color_update()
            self.button_enable(WHITE)
            self.gui_turn += 1

        else:
            sys.exit()

    def make_status(self):
        layout_status = wx.BoxSizer(wx.HORIZONTAL)
        status_font = wx.Font(50, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        color_b = wx.StaticText(self.status_Panel, wx.ID_ANY, 'BLACK ')
        color_w = wx.StaticText(self.status_Panel, wx.ID_ANY, 'WHITE ')
        self.sc_b = wx.StaticText(self.status_Panel, wx.ID_ANY, '0')
        self.sc_w = wx.StaticText(self.status_Panel, wx.ID_ANY, '0')
        color_b.SetFont(status_font)
        self.sc_b.SetFont(status_font)
        self.sc_w.SetFont(status_font)
        color_w.SetFont(status_font)
        self.sc_w.SetForegroundColour('WHITE')
        color_w.SetForegroundColour('WHITE')

        layout_status.Add(color_b, proportion=1)
        layout_status.Add(self.sc_b, proportion=1)
        layout_status.Add(color_w, proportion=1)
        layout_status.Add(self.sc_w, proportion=1)
        self.status_Panel.SetSizer(layout_status)

    def board_color_update(self):
        self.count_b = 0
        self.count_w = 0
        for bx in range(BOARD_SIZE):
            for by in range(BOARD_SIZE):
                if self.othello.board[by][bx] == 0:
                    button_idx = bx + by * 8
                    self.board_name[button_idx].SetBackgroundColour('#228b22')
                elif self.othello.board[by][bx] == 1:
                    button_idx = bx + by * 8
                    self.board_name[button_idx].SetBackgroundColour('#000000')
                    self.count_b += 1
                else:
                    button_idx = bx + by * 8
                    self.board_name[button_idx].SetBackgroundColour('#ffffff')
                    self.count_w += 1
        self.sc_b.SetLabel(str(self.count_b))
        self.sc_w.SetLabel(str(self.count_w))


    def click_action(self, a, g_p):
        b = a.GetId()
        b_idx = 0
        for button_put in self.board_name:
            c = button_put.GetId()
            if b == c:
                self.put_button(b_idx, g_p)
            else:
                b_idx += 1

    def for_human(self, a):
        g_p = self.turn_check()
        self.click_action(a, g_p)
        if g_p == BLACK:
            self.button_enable(WHITE)
        else:
            self.button_enable(BLACK)
        self.end_check()
        self.gui_turn += 1

    def end_check(self):
        kop = 0
        if self.othello.can_put_list(BLACK) == []:
            kop += 50
        if self.othello.can_put_list(WHITE) == []:
            kop += 50
        if kop == 100:
            judge, sb, sw = self.othello.end()
            self.WINNER.SetLabel(judge)

    def for_random(self, a):
        self.end_check()
        self.click_action(a, WHITE)
        self.board_color_update()
        self.end_check()
        while(True):
            if not self.othello.can_put_list(BLACK) == []:
                px, py = random_action(self.othello.can_put_list(BLACK), 0, 0)
                self.othello.put_stone(px, py, BLACK)
                self.board_color_update()
                self.gui_turn += 1
                self.end_check()
                if not self.othello.can_put_list(WHITE) == []:
                    self.button_enable(WHITE)
                    break
                else:
                    continue
            else:
                self.button_enable(WHITE)
                break
        self.gui_turn += 1

    def for_ch(self, a):
        self.end_check()
        self.click_action(a, WHITE)
        self.board_color_update()
        self.end_check()
        while (True):
            if not self.othello.can_put_list(BLACK) == []:
                px, py = ch_multi_player(self.othello.can_put_list(BLACK), [self.othello.board], 'LOSER')
                self.othello.put_stone(px, py, BLACK)
                self.board_color_update()
                self.gui_turn += 1
                self.end_check()
                if not self.othello.can_put_list(WHITE) == []:
                    self.button_enable(WHITE)
                    break
                else:
                    continue
            else:
                self.button_enable(WHITE)
                break
        self.gui_turn += 1

    def button_enable(self, player):
        for button_name in self.board_name:
            button_name.Disable()
        for bxy in self.othello.can_put_list(player):
            bx, by = bxy
            button_idx = bx + by * 8
            self.board_name[button_idx].Enable()

    def turn_check(self):
        print(self.gui_turn)
        if self.gui_turn == 0:
            print('f b')
            print(self.gui_turn)
            return BLACK
        elif self.gui_turn % 2 == 0:
            if not self.othello.can_put_list(BLACK) == []:
                print('b')
                return BLACK
            else:
                print('pass w')
                self.gui_turn += 1
                return WHITE
        else:
            if not self.othello.can_put_list(WHITE) == []:
                print('w')
                return WHITE
            else:
                print('pass b')
                self.gui_turn += 1
                return BLACK

    def put_button(self, b_idx, g_p):
        px, py = self.for_convert[b_idx]
        self.othello.put_stone(px, py, g_p)
        self.board_color_update()


reversi = wx.App()
Main_Frame = Main_Frame()
Main_Frame.Show()
reversi.MainLoop()
