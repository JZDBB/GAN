import wx
import os
import shutil

from eye2face_V00 import G
import matplotlib.pyplot as plt

class ImageWindow(wx.Window):

    def __init__(self, parent, id):
        wx.Window.__init__(self, parent, id)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.image = None

    def SetImage(self, image):
        self.image = image
        self.Refresh(True)

    def ClearImage(self):
        self.image = None
        self.Refresh(True)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        if self.image:
            dc.DrawBitmap(self.image.ConvertToBitmap(), 0, 0, False)


class AppFrame(wx.Frame):

    def __init__(self, parent, ID, title, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, (0, 0), (700, 400), style)

        self.panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        topBox = wx.BoxSizer(wx.HORIZONTAL)
        botBox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(topBox, 1, wx.EXPAND)
        vbox.Add(botBox)
        # self.filenames = os.listdir('data/')
        simbox = wx.BoxSizer(wx.HORIZONTAL)
        pathbox = wx.BoxSizer(wx.HORIZONTAL)
        bottombox = wx.BoxSizer(wx.HORIZONTAL)
        self.simStatic = wx.StaticText(self, label='Similarity:', size=(80, 30))
        self.simNum = wx.StaticText(self, label='0', size=(60, 30))
        self.Static = wx.StaticText(self, label='path:', size=(40, 30))
        self.text = wx.TextCtrl(self, wx.ID_ANY, size=(400, 30))
        self.btnA = wx.Button(self, wx.ID_ANY, 'sellect')
        self.Bind(wx.EVT_BUTTON, self.OnClickSellect, self.btnA)
        self.btnB = wx.Button(self, wx.ID_ANY, 'generate')
        self.Bind(wx.EVT_BUTTON, self.OnClickGEN, self.btnB)
        simbox.Add(self.simStatic)
        simbox.Add(self.simNum)
        pathbox.Add(self.Static)
        pathbox.Add(self.text)
        bottombox.Add(self.btnA)
        bottombox.Add(self.btnB)
        botBox.Add(simbox)
        botBox.Add(pathbox)
        botBox.Add(bottombox)

        # self.imw_eye = wx.Image(self, wx.ID_ANY)
        image = wx.Image('0-input.png', wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        # size = (256, 256)
        self.imw_eye = wx.StaticBitmap(self.panel, -1, pos=(10, 10), size=size)
        topBox.Add(self.imw_eye, 1, wx.EXPAND)
        # self.imw_org = wx.StaticBitmap(self.panel, -1, pos=(270, 10), size=size)
        # topBox.Add(self.imw_org, 2, wx.EXPAND)
        # self.imw_all = wx.StaticBitmap(self.panel, -1, pos=(530, 10), size=size)
        # topBox.Add(self.imw_all, 3, wx.EXPAND)

        # image = wx.Image('out.jpg', wx.BITMAP_TYPE_JPEG)
        # temp = image.ConvertToBitmap()
        # size = temp.GetWidth(), temp.GetHeight()
        # self.bmp = wx.StaticBitmap(self.panel, -1, temp, pos=(500, 20), size=size)

        filename = 'C:\\Users\\yn\\Desktop\\完整代码整理2018-12-17\\0.jpg'
        self.text.SetValue(filename)
        self.SetSizer(vbox)
        self.g = G()

    def OnClickSellect(self, evt):
        filenames = self.text.GetValue()
        image = wx.Image(filenames, wx.BITMAP_TYPE_ANY)
        w = image.GetWidth()
        h = image.GetHeight()
        scale = h / 256
        img2 = image.Scale(w / scale, h / scale)  # 缩小图像
        temp = img2.ConvertToBitmap()
        self.imw_eye.SetBitmap(temp)

        # filenames = filenames.replace('input', 'outputs')
        # image = wx.Image(filenames, wx.BITMAP_TYPE_ANY)
        # w = image.GetWidth()
        # h = image.GetHeight()
        # scale = h / 256
        # img2 = image.Scale(w / scale, h / scale)  # 缩小图像
        # self.imw_org.SetImage(img2)

    def OnClickGEN(self, evt):
        filenames = self.text.GetValue()
        # self.filename = os.path.join('data', self.filenames[self.count])

        # Scale the oiginal to another wx.Image
        results = self.g.run(plt.imread(filenames))
        plt.imsave('result.jpg', results['outputs'])
        image = wx.Image('result.jpg', wx.BITMAP_TYPE_ANY)
        w = image.GetWidth()
        h = image.GetHeight()
        scale = h / 256
        img2 = image.Scale(w / scale, h / scale)  # 缩小图像
        temp = img2.ConvertToBitmap()
        self.imw_eye.SetBitmap(temp)


class MyApplication(wx.App):
    def OnInit(self):
        wnd = AppFrame(None, wx.ID_ANY, "eye to face")
        wnd.Show(True)
        return True


def main():
    app = MyApplication(False)
    app.MainLoop()


if __name__ == "__main__":
    main()