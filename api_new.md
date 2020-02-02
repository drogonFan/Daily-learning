# 地图api接口

## 腾讯地图（额度50W）

请求接口：

```
https://apis.map.qq.com/ws/geocoder/v1/?
location=39.984154,116.307490
&get_poi=0
&key=ET7BZ-TDHL6-SCKSH-MAIJR-YKTIE-7LFCO
```

返回结果：
```json
{
    "status":0,
    "result":{
        "address_component":{
            "nation":"中国",
            "province":"北京市",
            "city":"北京市",
            "district":"海淀区",
        }
    }
}
```

## 高德地图（额度30万）

请求接口：
```
https://restapi.amap.com/v3/geocode/regeo?
output=JSON
&location=116.310003,39.991957
&key=e55289b149de9ea872bc680caa1c5347
&radius=0
&extensions=base
&batch=false
&roadlevel=0
```

返回结果：
```json
{
    "status" :"1",
    "regeocode" :{
        "addressComponent" :{
            "city" :[ ],
            "province" :"北京市",
            "adcode" :"110105",
            "district" :"朝阳区",
            "towncode" :"110105026000",
            "streetNumber" :{ … },
            "country" :"中国",
            "township" :"望京街道",
            "businessAreas" :[ … ],
            "building" :{ … },
            "neighborhood" :{ … },
            "citycode" :"010"
        },
    },
    "info" :"OK",
    "infocode" :"10000"
}
```

## 百度地图（额度30W）

```
http://api.map.baidu.com/reverse_geocoding/v3/?
ak=40NVD4ntV7xVqDdMifmygyxm0O1B1MM7
&output=json
&coordtype=wgs84ll
&location=31.225696563611,121.49884033194
```

结果：
```json
{
    "status": 0,
    "result": {
        "location": {
            "lng": 121.50989077799084,
            "lat": 31.22932842411674
            },
        "formatted_address": "上海市黄浦区中山南路187",
        "business": "外滩,陆家嘴,董家渡",
        "addressComponent": {
            "country": "中国",
            "province": "上海市",
            "city": "上海市",
        }
    }
}
```
