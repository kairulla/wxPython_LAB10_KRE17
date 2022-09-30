#!/usr/bin/env python3
# coding=utf-8

import random

import wx
import wx.xrc
from guiController import MyFrame


class Launcher(MyFrame):
    array_global = []

    def myFrameOnActivate(self, event):
        self.wxGridMyArray.SetRowLabelSize(0)
        self.wxGridMyArray.SetColLabelSize(0)
        ico = wx.Icon('_MY_PICTURES/logo.png', wx.BITMAP_TYPE_PNG)
        self.SetIcon(ico)

    def myFrameOnClose(self, event):
        self.Destroy()

    def wxButtonRandomOnButtonClick(self, event):
        n = 4
        m = 5
        max_value = 20

        array = []
        for i in range(0, n):
            sub_array = []
            for j in range(m):
                number = random.randint(0, max_value)
                sub_array.append(number)
            array.append(sub_array)

        for row, i in enumerate(array):
            for col, j in enumerate(i):
                self.wxGridMyArray.SetCellValue(row, col, "%d" % j)

        self.array_global = array.copy()
        self.wxStaticTextMaxItem.SetLabelText("Максимальный элемент =")


    def wxButtonSolverOnButtonClick(self, event):
        array = self.array_global.copy()
        i = 0
        max_value = array[1][i]
        max_i = i
        for i, j in enumerate(array[1]):
            # print("i=", i)
            if j > max_value:
                max_value = j
                max_i = i
        self.wxStaticTextMaxItem.SetLabelText("Максимальный элемент = %d" % max_value)
        print("max_value=", max_value)
        print("max_i=", max_i)

        if (max_value > array[2][0]):
            temp = array[2][0]
            array[2][0] = max_value
            array[1][max_i] = temp

            for row, i in enumerate(array):
                for col, j in enumerate(i):
                    self.wxGridMyArray.SetCellValue(row, col, "%d" % j)


def main():
    app = wx.App(False)
    frame = Launcher(None)
    frame.Show(True)
    app.MainLoop()

    # дописать в __init__
    # self.wxGridMyArray.SetRowLabelSize(0)
    # self.wxGridMyArray.SetColLabelSize(0)


if __name__ == '__main__':
    main()



# def main():
#     array = random_array(4, 5)
#     print_array(array)
#
#     i = 0
#     max_value = array[1][i]
#     max_i = i
#     for i, j in enumerate(array[1]):
#         # print("i=", i)
#         if j > max_value:
#             max_value = j
#             max_i = i
#     print("max_value=", max_value)
#     print("max_i=", max_i)
#
#     if (max_value > array[2][0]):
#         temp = array[2][0]
#         array[2][0] = max_value
#         array[1][max_i] = temp
#
#     print_array(array)


