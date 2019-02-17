import wx
import os
import shutil

class ImageWindow(wx.Window):

    def __init__(self, parent, id):
        wx.Window.__init__(self, parent, id)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.image = None

    def SetImage(self, image):
        self.image = image
        self.Refresh(True)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        if self.image:
            dc.DrawBitmap(self.image.ConvertToBitmap(), 0, 0, False)


class AppFrame(wx.Frame):

    def __init__(self, parent, ID, title, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)

        vbox = wx.BoxSizer(wx.VERTICAL)
        topBox = wx.BoxSizer(wx.HORIZONTAL)
        botBox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(topBox, 1, wx.EXPAND)
        vbox.Add(botBox)
        self.filenames = os.listdir('data/')
        self.btnA = wx.Button(self, wx.ID_ANY, 'sellect')
        self.Bind(wx.EVT_BUTTON, self.OnClickSellect, self.btnA)
        self.btnB = wx.Button(self, wx.ID_ANY, 'generate')
        self.Bind(wx.EVT_BUTTON, self.OnClickGEN, self.btnB)

        botBox.Add(self.btnA)
        botBox.Add(self.btnB)

        self.imw = ImageWindow(self, wx.ID_ANY)
        topBox.Add(self.imw, 1, wx.EXPAND)
        self.imw_all = ImageWindow(self, wx.ID_ANY)
        topBox.Add(self.imw_all, 2, wx.EXPAND)

        # self.count = 0
        # self.filename = os.path.join('data', self.filenames[self.count])
        # image = wx.Image(self.filename, wx.BITMAP_TYPE_ANY)
        # # Scale the oiginal to another wx.Image
        # w = image.GetWidth()
        # h = image.GetHeight()
        # img2 = image.Scale(w / 2, h / 2)  # 缩小图像
        #
        # self.imw.SetImage(img2)

        self.SetSizer(vbox)

    def OnClickSellect(self,evt):
        full_path = self.filename.replace('data', 'new')
        shutil.copy(self.filename, full_path)
        self.count += 1
        if self.count >= len(self.filenames):
            self.count -= 1
        self.filename = os.path.join('data', self.filenames[self.count])
        image = wx.Image(self.filename, wx.BITMAP_TYPE_ANY)
        # Scale the oiginal to another wx.Image
        w = image.GetWidth()
        h = image.GetHeight()
        img2 = image.Scale(w / 3, h / 3)  # 缩小图像
        self.imw.SetImage(img2)

    def OnClickGEN(self, evt):
        self.count += 1
        if self.count >= len(self.filenames):
            self.count -= 1
        self.filename = os.path.join('data', self.filenames[self.count])
        image = wx.Image(self.filename, wx.BITMAP_TYPE_ANY)
        # Scale the oiginal to another wx.Image
        w = image.GetWidth()
        h = image.GetHeight()
        img2 = image.Scale(w / 3, h / 3)  # 缩小图像
        self.imw.SetImage(img2)


class MyApplication(wx.App):

    def OnInit(self):
        wnd = AppFrame(None, wx.ID_ANY, "Main Window")
        wnd.Show(True)
        return True


def main():
    app = MyApplication(False)
    app.MainLoop()


if __name__ == "__main__":
    main()