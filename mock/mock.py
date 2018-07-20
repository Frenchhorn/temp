#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request, response
import json

token = {
    "access_token" : "c76435fb-3a03-41d0-bec4-448202934267",
    "token_type" : "bearer",
    "scope" : "basic",
    "expires_in" : 15
}
@route('/oauth/token', method='post')
def getToken():
    return callback(request, token)

message = {
  "result":{
    "code": "code",
    "message": "message"
  }
}
@route('/SyncCustom', method='post')
def syncCustom():
    return callback(request, message)

message2 = {
  "result": {
    "code": "code",
    "message": "message"
  },
  "pageInfo": {
    "pageNo": 0,
    "pageSize": 6,
    "hasNext": True
  },
  "customInfo": {
    "headImgUrl": "headImgUrl",
    "gender": "gender",
    "openId": "openId",
    "mobileNo": "mobileNo",
    "userName": "userName",
    "customAda": "customAda"
  }
}
@route('/FindCustomInfo', method='post')
def findCustomInfo():
    return callback(request, message2)

message3 = {
  "result": {
    "code": "code",
    "message": "message"
  },
  "products":[
    {"content":"","imageHDUrl":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/at-home/50188_480_480_3.jpg/jcr:content/renditions/cq5dam.thumbnail.640.640.png","imageUrl":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/at-home/50188_480_480_3.jpg/jcr:content/renditions/cq5dam.thumbnail.480.480.png","imageUrl120":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/at-home/50188_480_480_3.jpg/jcr:content/renditions/cq5dam.thumbnail.120.120.png","imageUrl140":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/at-home/50188_480_480_3.jpg/jcr:content/renditions/cq5dam.thumbnail.140.140.png","itemClass":"家居","itemClass2":"益之源净水器","itemClass3":"益之源净水器","itemClass4":"","itemName":"益之源净水器","itemNumber":"50188","price":"6980.0","url":"","weight":"4.95"},
    {"content":"30Ml","imageHDUrl":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/upload/noimage640.png","imageUrl":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/upload/40246_480_480_1.jpg","imageUrl120":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/upload/40246_120_120_1.jpg","imageUrl140":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/upload/40246_140_140_1.jpg","itemClass":"雅姿","itemClass2":"卓效美肌系列","itemClass3":"","itemClass4":"","itemName":"雅姿®抚痕紧致精华乳","itemNumber":"40246","price":"695.0","url":"","weight":"0.058"}
  ]
}
@route('/GetProducts')
def getProducts():
    return callback(request, message3)

message4 = {
  "result": {
    "code":"200",
    "message":"success"
  },
  "product":{"authNo":"","bv":"391.0","component":"","content":"105克（每袋）×2袋","effect":"·具有免疫调节和增加骨密度的保健功能。\n·提供人体必需的8种矿物质和14种维生素，另含6种纽崔莱天然植物提取物。\n·将丰富的维生素和矿物质分开两粒保存，颗粒大小方便吞咽。\n·专利技术*的包装盒设计，真空金属膜包装，良好的密封防潮防紫外线性能，并附有两片隔片，可作为营养片整理盒。\n·不添加人造香料、合成色素或防腐剂。","guarantee":"","healthFunc":"免疫调节、增加骨密度。","honor":"","hotFlag":"0","hygieneNo":"","imageHDUpdateTime":"2016-06-29 05:22:10","imageHDUrl":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/nutrilite/functional-health/aoyunjinianbanlanse288x400.png/jcr:content/renditions/cq5dam.thumbnail.640.640.png","imageUpdateTime":"2016-06-29 05:22:10","imageUrl":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/nutrilite/functional-health/aoyunjinianbanlanse288x400.png/jcr:content/renditions/cq5dam.thumbnail.480.480.png","imageUrl120":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/nutrilite/functional-health/aoyunjinianbanlanse288x400.png/jcr:content/renditions/cq5dam.thumbnail.120.120.png","imageUrl140":"http://qa.amway.com.cn/content/dam/china/accl/amwaychina/product/nutrilite/functional-health/aoyunjinianbanlanse288x400.png/jcr:content/renditions/cq5dam.thumbnail.140.140.png","inclusion":"","itemClass":"纽崔莱","itemClass2":"功能性保健系列","itemClass3":"","itemClass4":"","itemName":"为奥运加油纪念版倍立健片蓝色","itemNumber":"21533","method":"每日2次，每次各1片，以水食用。","newBVProduct":True,"notice":"1、本品不能代替药物。\n2、请放置于儿童触及不到的地方。\n3、本产品应冷藏或贮存于30℃以下阴凉干燥处，并保持盒盖紧闭 。\n \n审批文号：国食健字G20040219","nutrition":"","other":"","price":"460.0","prodDesc":"","prodEndDate":"","prodPubDate":"","pubTime":"","pv":"32.85","range":"","spec":"","standard":"","store":"","suit":"免疫力低下者、中老年人。","summary":"","unsuit":"","volume":"","weight":"0.349"}
}
@route('/GetProduct')
def getProduct():
    return callback(request, message4)

message5 = {
  "result":{
    "code": "code",
    "message": "message"
  }
}
@route('/AddCart', method='post')
def addCart():
    return callback(request, message5)

def callback(request, result):
    if (request.query.callbackparam):
        result = '%s(%s)'%(request.query.callbackparam, json.dumps(result))
    return result

@route('/test')
def test():
    return '{"a":1,"code": "code"}'

run(host='10.143.174.79', port=3000, debug=True)
# run(host='localhost', port=3000, debug=True)
