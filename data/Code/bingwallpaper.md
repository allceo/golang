## 微软壁纸API ##

### 获取所有类别信息 ###

 > http://bingclient.chinacloudapp.cn/wallpaperv1/categories

```json
{
    "categories": [
        {
            "name": "精选",
            "filter": "bing",
            "rank": 100,
            "guid": "15296793f5374a49a2965e9f64468225"
        },
        {
            "name": "动物",
            "filter": "animal",
            "rank": 200,
            "guid": "52a615016600444d8236eb3cfb5940b2"
        },
        {
            "name": "风景",
            "filter": "landscape",
            "rank": 300,
            "guid": "5401aed0c9654e3aa1350c90d1f2e4a0"
        },
        {
            "name": "非主流",
            "filter": "other",
            "rank": 400,
            "guid": "7f7d77e6ff7a4a719e8e3f1c97eb52ce"
        },
        {
            "name": "2014年度美图",
            "filter": "2014top",
            "rank": 500,
            "guid": "0cb9c60ead2b4928bde372fea5f5ada3"
        }
    ]
}
```

### 获取类别中的图片信息 ###

 > - http://bingclient.chinacloudapp.cn/wallpaperv1/images?filter=bing&count=16&start=0&1448671451877
 > - filter:类别信息中的filter
 > - count:当前返回的图片条数
 > - start:开始ID
 > - 1448671451877:时间戳，1448671451 877即为2015/11/28 8:44:11.877
 > - 返回一个images的json

```json
	{
    "images": [
        {
            "bot": "1",
            "copyright": "© Zinaida Sopina/Shutterstock",
            "copyrightlink": "http://www.bing.com/search?q=%e5%8f%b2%e6%89%98%e5%85%8b%e9%97%b4%e6%ad%87%e6%b3%89&FORM=hpcapt&mkt=zh-cn",
            "drk": "1",
            "enddate": "20150902",
            "fullstartdate": "201509011600",
            "startdate": "20150901",
            "urlbase": "http://image123.msn.com/wallpaper/i/201509/StrokkurGeyserVideo_ZH-CN13059478273",
            "wp": "false",
            "market": "zh-cn",
            "copyrightquery": "史托克间歇泉",
            "storytitle": "雷克雅未克",
            "storyarrtibute": "冰岛，东雷克雅维克，赫维塔河热地",
            "storypara1": "这座城市接近北极圈，你会被那迷幻的极光、冰川、火山、温泉美景所迷住。城市里街道不宽，住宅小巧精致，整座城给人以古色古香、整洁干净之感。",
            "storypara2": null,
            "rank": 200,
            "filter": "landscape,",
            "relatedquery": "赫维塔河热地",
            "verpquery": "赫维塔河热地",
            "urls1": "-s1.jpg",
            "urls2": "-s2.jpg",
            "urls3": "-s3.jpg",
            "urls4": "-s4.jpg",
            "urls5": "-s5.jpg",
            "guid": "3d81fd3a7e3641038537208d4d531367"
        }
    ]
}
```

### 图片的下载 ###

 > -  图片下载时是使用urlbase + urls[1:5]去生成的。
 > -  s1：213*131
 > -  s2：429*265
 > -  s3：645*399
 > -  s4：1920*1080
 > -  s5：1920*1080  指定了水平/垂直分辨率：96dpi
 > -  s4比s5文件大一些

### 获取每日背景图片 ###

 > - http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1448855230402&pid=hp&video=1
 > 1、format，非必要。我理解为输出格式，不存在或者不等于js，即为xml格式，等于js时，输出json格式；XML，JSON，RSS
 > 2、idx，非必要。不存在或者等于0时，输出当天的图片，-1为已经预备用于明天显示的信息，1则为昨天的图片，idx最多获取到前16天的图片信息；*
 > 3、n，必要。这是输出信息的数量，比如n=1，即为1条，以此类推，至多输出8条；*
*号注释：此处我们要注意的时，是否正常的输出信息，与n和idx有关，通过idx的值，我们就可以获得之前bing所使用的背景图片的信息了。
 > 4、nc，非必要，时间戳

```json
	{
	    "images": [
	        {
	            "startdate": "20151129",
	            "fullstartdate": "201511291600",
	            "enddate": "20151130",
	            "url": "http://s.cn.bing.net/az/hprichbg/rb/Modica_ZH-CN12563546966_1920x1080.jpg",
	            "urlbase": "/az/hprichbg/rb/Modica_ZH-CN12563546966",
	            "copyright": "意大利，西西里岛，莫迪卡 (© Robert Harding World Imagery/Offset)",
	            "copyrightlink": "/search?q=%e8%8e%ab%e8%bf%aa%e5%8d%a1&form=hpcapt&mkt=zh-cn",
	            "wp": true,
	            "hsh": "4ac88736c40219a20b5cab342d33c002",
	            "drk": 1,
	            "top": 1,
	            "bot": 1,
	            "hs": [
	                {
	                    "desc": "当莫迪卡的夜幕下垂，诺托谷地罩上了淡淡的蓝色光晕，",
	                    "link": "/search?q=%e8%8e%ab%e8%bf%aa%e5%8d%a1&FORM=hphot1&mkt=zh-cn",
	                    "query": "这里曾经是一条河流，而如今干涸的河道早已被热闹的街市所填满。",
	                    "locx": 23,
	                    "locy": 38
	                },
	                {
	                    "desc": "而在亚平宁半岛最西南处的小岛之上，曾发生过一些美丽的故事，",
	                    "link": "/search?q=%e8%a5%bf%e8%a5%bf%e9%87%8c%e7%9a%84%e7%be%8e%e4%b8%bd%e4%bc%a0%e8%af%b4&FORM=hphot2&mkt=zh-cn",
	                    "query": "穿过硝烟和战火，穿过热闹和喧嚣，西西里从未像现在这般宁静过……",
	                    "locx": 32,
	                    "locy": 45
	                },
	                {
	                    "desc": "这里是世界著名的巴洛克风格建筑群的中心，巴洛克的原意是畸形的珍珠，",
	                    "link": "/search?q=%e5%b7%b4%e6%b4%9b%e5%85%8b%e5%bb%ba%e7%ad%91&FORM=hphot3&mkt=zh-cn",
	                    "query": "它突破了古典艺术的常规，形成了一种豪华、自由并具有韵律的设计风格……",
	                    "locx": 58,
	                    "locy": 48
	                }
	            ],
	            "msg": [
	                {
	                    "title": "今日图片故事",
	                    "link": "/search?q=%e8%8e%ab%e8%bf%aa%e5%8d%a1&form=pgbar1&mkt=zh-cn",
	                    "text": "莫迪卡"
	                }
	            ]
	        }
	    ],
	    "tooltips": {
	        "loading": "正在加载...",
	        "previous": "上一页",
	        "next": "下一页",
	        "walle": "此图片不能下载用作壁纸。",
	        "walls": "下载今日美图。仅限用作桌面壁纸。",
	        "play": "播放",
	        "pause": "暂停"
	    }
	}
```