from eye2face_V00 import G
import matplotlib.pyplot as plt
import wx
import wx.xrc

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"eye to face", pos=wx.DefaultPosition,
                          size=wx.Size(810, 400), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(4, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gSizer2 = wx.GridSizer(1, 3, 0, 0)

        self.m_img_eye = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"input.png", wx.BITMAP_TYPE_ANY),
                                         wx.Point(10, 10), wx.Size(256, 256), 0)
        gSizer2.Add(self.m_img_eye, 0, wx.ALL, 5)

        self.m_imgorg = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"target.png", wx.BITMAP_TYPE_ANY),
                                        wx.Point(530, 10), wx.Size(256, 256), 0)
        gSizer2.Add(self.m_imgorg, 0, wx.ALL, 5)

        self.m_imgout = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"output.png", wx.BITMAP_TYPE_ANY),
                                        wx.Point(270, 10), wx.Size(256, 256), 0)
        gSizer2.Add(self.m_imgout, 0, wx.ALL, 5)

        fgSizer1.Add(gSizer2, 1, wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Similarity:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(12, 74, 90, 92, False, wx.EmptyString))

        bSizer2.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"0", wx.Point(100, 0), wx.Size(100, -1), 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(12, 74, 90, 92, False, wx.EmptyString))

        bSizer2.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"path:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(12, 74, 90, 92, False, wx.EmptyString))

        bSizer2.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        bSizer2.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_sellect = wx.Button(self, wx.ID_ANY, u"sellect", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_sellect.SetFont(wx.Font(12, 74, 90, 92, False, wx.EmptyString))
        self.Bind(wx.EVT_BUTTON, self.OnClickSellect, self.m_sellect)
        bSizer3.Add(self.m_sellect, 0, wx.ALL, 5)

        self.m_genarate = wx.Button(self, wx.ID_ANY, u"genarate", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_genarate.SetFont(wx.Font(12, 74, 90, 92, False, wx.EmptyString))
        self.Bind(wx.EVT_BUTTON, self.OnClickGenarate, self.m_genarate)
        bSizer3.Add(self.m_genarate, 0, wx.ALL, 5)

        # self.m_compute = wx.Button(self, wx.ID_ANY, u"compute", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_compute.SetFont(wx.Font(12, 74, 90, 92, False, wx.EmptyString))
        #
        # bSizer3.Add(self.m_compute, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        self.g = G()

    def __del__(self):
        pass

    def OnClickSellect(self, evt):
        filename = '0-input.png'
        image1 = wx.Image(filename, wx.BITMAP_TYPE_ANY).Rescale(256, 256).ConvertToBitmap()
        self.m_img_eye.SetBitmap(wx.BitmapFromImage(image1))
        filename = filename.replace('input', 'targets')
        image2 = wx.Image(filename, wx.BITMAP_TYPE_ANY).Rescale(256, 256).ConvertToBitmap()
        self.m_imgorg.SetBitmap(wx.BitmapFromImage(image2))
        image3 = wx.Image('org.png', wx.BITMAP_TYPE_ANY).Rescale(256, 256).ConvertToBitmap()
        self.m_imgout.SetBitmap(wx.BitmapFromImage(image3))

    def OnClickGenarate(self, evt):
        filename = '0-input.png'
        results = self.g.run(plt.imread(filename)[:, :, :3])
        outpath = filename.replace('input', 'output')
        plt.imsave(outpath, results['outputs'])
        image3 = wx.Image(outpath, wx.BITMAP_TYPE_ANY).Rescale(256, 256).ConvertToBitmap()
        self.m_imgout.SetBitmap(wx.BitmapFromImage(image3))


class MyApplication(wx.App):
    def OnInit(self):
        wnd = MyFrame(None)
        wnd.Show(True)
        return True


def main():
    app = MyApplication(False)
    app.MainLoop()

if __name__ == '__main__':
    main()