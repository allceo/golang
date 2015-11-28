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