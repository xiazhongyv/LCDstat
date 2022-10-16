# LCDstat
### 让你的旧手机变成自定义PC数据屏
### Make your old phone a status screen ！

## Intorduction

10月14日是第五个国际电子垃圾日。总部设在比利时首都布鲁塞尔的电子电气设备废弃物论坛发布报告，预计今年全球民众持有的160亿部手机中，将有53亿部被废弃或闲置。

October 14 is the fifth International E-Waste Day. Of the 16 billion mobile phones in the hands of the world's citizens, 5.3 billion will be discarded or unused this year, according to a report by the Waste Electrical and Electronic Equipment Forum (WEEE).

这些文件展示了如何使用AIDA64将你的手机变成一个系统状态屏，你不仅可以从上面看到帧数、GPU或CPU状态等，还可以利用爬虫或API获取任何你想要的数据，比如校园卡余额、电量余额、天气等等，并把它们都自动画在屏幕上！

The files show how to convert your phone into a status screen on Windows, how you can use selenium to get data from a web page, or through a web API, and display it on your screen.

请注意我的模板可能只适用于主屏1.5倍缩放下2280x1080的手机屏幕；只是拿selenium登录并爬取北大校园卡余额、以及抓包微信公众号API获取宿舍剩余电量举了个例子；或者你可能不喜欢我的设计。都没有关系，我的本意是向你展示你可以用废旧手机、LCD屏幕或者你正在用的手机，做一个很cool的自定义显示面板，我只是介绍方法与思路，自己动手才是最有乐趣的！

Please note that the template I shared is only suitable for climbing the balance of Peking University campus card and the dormitory electricity of Machikou new campus of Peking University. The panel file is only suitable for a phone with a resolution of 2280x1080 at 1.5x zoom of the main screen. So I'm presenting a design idea, rather than providing a document that works for you. Do It Yourself. That's where the real fun comes in.

## Get Started

Install [AIDA64](https://www.aida64.com/downloads), [DMT](https://dualmonitortool.sourceforge.net/download.html).

Install [spacedesk](https://www.spacedesk.net/) both on your PC and your phone.

### If you need FPS data:

Install [MSI-Afterburner](https://tw.msi.com/Landing/afterburner/graphics-cards) or RTSS.

### If you need a crawler:

Install [Chrome](https://www.google.cn/intl/zh-CN/chrome/) and [chromedriver](http://chromedriver.storage.googleapis.com/index.html)

Put chromedriver.exe under dir root.

pip install selenium, pillow and any other packages you need.

↓

Detailed tutorial: [link](https://space.bilibili.com/99271729)
