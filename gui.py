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
        self.gui_turn = 0
        self.vs = self.for_ch

        self.for_convert = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
                            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                            (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
                            (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                            (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                            (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Reversi', size=(1500, 700))
        icon = wx.Icon('img/icon.ico', wx.BITMAP_TYPE_ICO)
        wx.Frame.SetIcon(self, icon)
        self.board_Panel = wx.Panel(self, wx.ID_ANY, pos=(0, 0), size=(560, 560))
        self.layout_board = wx.FlexGridSizer(8, 8, 0, 0)
        self.board_make()

        self.board_Panel.SetSizer(self.layout_board)
        self.othello = game_master()
        self.board_color_update()
        self.button_enable(BLACK)
        if self.vs == self.for_random:
            px, py = random_action(self.othello.can_put_list(BLACK), 0, 0)
            self.othello.put_stone(px, py, BLACK)
            self.board_color_update()
            self.button_enable(WHITE)
            self.gui_turn += 1
        elif self.vs == self.for_ch:
            px, py = ch_multi_player(self.othello.can_put_list(BLACK), [self.othello.board], 'LOSER')
            self.othello.put_stone(px, py, BLACK)
            self.board_color_update()
            self.button_enable(WHITE)
            self.gui_turn += 1

    def board_make(self):
        self.board_Panel.SetBackgroundColour('#191970')
        self.button_0 = wx.Button(self.board_Panel, wx.ID_ANY, '0', size=(70, 70))
        self.button_1 = wx.Button(self.board_Panel, wx.ID_ANY, '1', size=(70, 70))
        self.button_2 = wx.Button(self.board_Panel, wx.ID_ANY, '2', size=(70, 70))
        self.button_3 = wx.Button(self.board_Panel, wx.ID_ANY, '3', size=(70, 70))
        self.button_4 = wx.Button(self.board_Panel, wx.ID_ANY, '4', size=(70, 70))
        self.button_5 = wx.Button(self.board_Panel, wx.ID_ANY, '5', size=(70, 70))
        self.button_6 = wx.Button(self.board_Panel, wx.ID_ANY, '6', size=(70, 70))
        self.button_7 = wx.Button(self.board_Panel, wx.ID_ANY, '7', size=(70, 70))
        self.button_8 = wx.Button(self.board_Panel, wx.ID_ANY, '8', size=(70, 70))
        self.button_9 = wx.Button(self.board_Panel, wx.ID_ANY, '9', size=(70, 70))
        self.button_10 = wx.Button(self.board_Panel, wx.ID_ANY, '10', size=(70, 70))
        self.button_11 = wx.Button(self.board_Panel, wx.ID_ANY, '11', size=(70, 70))
        self.button_12 = wx.Button(self.board_Panel, wx.ID_ANY, '12', size=(70, 70))
        self.button_13 = wx.Button(self.board_Panel, wx.ID_ANY, '13', size=(70, 70))
        self.button_14 = wx.Button(self.board_Panel, wx.ID_ANY, '14', size=(70, 70))
        self.button_15 = wx.Button(self.board_Panel, wx.ID_ANY, '15', size=(70, 70))
        self.button_16 = wx.Button(self.board_Panel, wx.ID_ANY, '16', size=(70, 70))
        self.button_17 = wx.Button(self.board_Panel, wx.ID_ANY, '17', size=(70, 70))
        self.button_18 = wx.Button(self.board_Panel, wx.ID_ANY, '18', size=(70, 70))
        self.button_19 = wx.Button(self.board_Panel, wx.ID_ANY, '19', size=(70, 70))
        self.button_20 = wx.Button(self.board_Panel, wx.ID_ANY, '20', size=(70, 70))
        self.button_21 = wx.Button(self.board_Panel, wx.ID_ANY, '21', size=(70, 70))
        self.button_22 = wx.Button(self.board_Panel, wx.ID_ANY, '22', size=(70, 70))
        self.button_23 = wx.Button(self.board_Panel, wx.ID_ANY, '23', size=(70, 70))
        self.button_24 = wx.Button(self.board_Panel, wx.ID_ANY, '24', size=(70, 70))
        self.button_25 = wx.Button(self.board_Panel, wx.ID_ANY, '25', size=(70, 70))
        self.button_26 = wx.Button(self.board_Panel, wx.ID_ANY, '26', size=(70, 70))
        self.button_27 = wx.Button(self.board_Panel, wx.ID_ANY, '27', size=(70, 70))
        self.button_28 = wx.Button(self.board_Panel, wx.ID_ANY, '28', size=(70, 70))
        self.button_29 = wx.Button(self.board_Panel, wx.ID_ANY, '29', size=(70, 70))
        self.button_30 = wx.Button(self.board_Panel, wx.ID_ANY, '30', size=(70, 70))
        self.button_31 = wx.Button(self.board_Panel, wx.ID_ANY, '31', size=(70, 70))
        self.button_32 = wx.Button(self.board_Panel, wx.ID_ANY, '32', size=(70, 70))
        self.button_33 = wx.Button(self.board_Panel, wx.ID_ANY, '33', size=(70, 70))
        self.button_34 = wx.Button(self.board_Panel, wx.ID_ANY, '34', size=(70, 70))
        self.button_35 = wx.Button(self.board_Panel, wx.ID_ANY, '35', size=(70, 70))
        self.button_36 = wx.Button(self.board_Panel, wx.ID_ANY, '36', size=(70, 70))
        self.button_37 = wx.Button(self.board_Panel, wx.ID_ANY, '37', size=(70, 70))
        self.button_38 = wx.Button(self.board_Panel, wx.ID_ANY, '38', size=(70, 70))
        self.button_39 = wx.Button(self.board_Panel, wx.ID_ANY, '39', size=(70, 70))
        self.button_40 = wx.Button(self.board_Panel, wx.ID_ANY, '40', size=(70, 70))
        self.button_41 = wx.Button(self.board_Panel, wx.ID_ANY, '41', size=(70, 70))
        self.button_42 = wx.Button(self.board_Panel, wx.ID_ANY, '42', size=(70, 70))
        self.button_43 = wx.Button(self.board_Panel, wx.ID_ANY, '43', size=(70, 70))
        self.button_44 = wx.Button(self.board_Panel, wx.ID_ANY, '44', size=(70, 70))
        self.button_45 = wx.Button(self.board_Panel, wx.ID_ANY, '45', size=(70, 70))
        self.button_46 = wx.Button(self.board_Panel, wx.ID_ANY, '46', size=(70, 70))
        self.button_47 = wx.Button(self.board_Panel, wx.ID_ANY, '47', size=(70, 70))
        self.button_48 = wx.Button(self.board_Panel, wx.ID_ANY, '48', size=(70, 70))
        self.button_49 = wx.Button(self.board_Panel, wx.ID_ANY, '49', size=(70, 70))
        self.button_50 = wx.Button(self.board_Panel, wx.ID_ANY, '50', size=(70, 70))
        self.button_51 = wx.Button(self.board_Panel, wx.ID_ANY, '51', size=(70, 70))
        self.button_52 = wx.Button(self.board_Panel, wx.ID_ANY, '52', size=(70, 70))
        self.button_53 = wx.Button(self.board_Panel, wx.ID_ANY, '53', size=(70, 70))
        self.button_54 = wx.Button(self.board_Panel, wx.ID_ANY, '54', size=(70, 70))
        self.button_55 = wx.Button(self.board_Panel, wx.ID_ANY, '55', size=(70, 70))
        self.button_56 = wx.Button(self.board_Panel, wx.ID_ANY, '56', size=(70, 70))
        self.button_57 = wx.Button(self.board_Panel, wx.ID_ANY, '57', size=(70, 70))
        self.button_58 = wx.Button(self.board_Panel, wx.ID_ANY, '58', size=(70, 70))
        self.button_59 = wx.Button(self.board_Panel, wx.ID_ANY, '59', size=(70, 70))
        self.button_60 = wx.Button(self.board_Panel, wx.ID_ANY, '60', size=(70, 70))
        self.button_61 = wx.Button(self.board_Panel, wx.ID_ANY, '61', size=(70, 70))
        self.button_62 = wx.Button(self.board_Panel, wx.ID_ANY, '62', size=(70, 70))
        self.button_63 = wx.Button(self.board_Panel, wx.ID_ANY, '63', size=(70, 70))

        self.board_name = [self.button_0, self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7,
                           self.button_8, self.button_9, self.button_10, self.button_11, self.button_12, self.button_13, self.button_14,self.button_15,
                           self.button_16, self.button_17, self.button_18, self.button_19, self.button_20,self.button_21, self.button_22, self.button_23,
                           self.button_24, self.button_25, self.button_26, self.button_27, self.button_28, self.button_29, self.button_30, self.button_31,
                           self.button_32, self.button_33, self.button_34, self.button_35, self.button_36, self.button_37, self.button_38, self.button_39,
                           self.button_40, self.button_41, self.button_42, self.button_43,self. button_44, self.button_45, self.button_46, self.button_47,
                           self.button_48, self.button_49, self.button_50, self.button_51, self.button_52, self.button_53, self.button_54, self.button_55,
                           self.button_56, self.button_57, self.button_58, self.button_59, self.button_60, self.button_61, self.button_62, self.button_63,
                           ]

        self.board_dict = {}
        dict_reg = 0
        for button_name in self.board_name:
            button_name.SetBackgroundColour('#228b22')
            button_name.SetForegroundColour('#bc8f8f')
            button_name.Bind(wx.EVT_BUTTON, self.vs)
            button_name.Disable()
            self.layout_board.Add(button_name)
            self.board_dict[str(dict_reg)] = button_name
            dict_reg += 1

    def board_color_update(self):
        for bx in range(BOARD_SIZE):
            for by in range(BOARD_SIZE):
                if self.othello.board[by][bx] == 0:
                    button_idx = bx + by * 8
                    self.board_name[button_idx].SetBackgroundColour('#228b22')
                elif self.othello.board[by][bx] == 1:
                    button_idx = bx + by * 8
                    self.board_name[button_idx].SetBackgroundColour('#000000')
                else:
                    button_idx = bx + by * 8
                    self.board_name[button_idx].SetBackgroundColour('#ffffff')

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
            tmp_w, score_B, score_W = self.othello.end()
            print(str(tmp_w) + 'です.黒' + str(score_B) + '石,白' + str(score_W) + '石です.')
            sys.exit()

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
        self.othello.view()
        self.board_color_update()


reversi = wx.App()
Main_Frame = Main_Frame()
Main_Frame.Show()
reversi.MainLoop()
