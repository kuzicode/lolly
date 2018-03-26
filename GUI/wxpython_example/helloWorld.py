import wx

#创建一个应用对象
app=wx.App()

#创建框架
frm=wx.Frame(None,title='Hello,World!')

#显示
frm.Show()

#开始事件循环
app.MainLoop()

