#!/usr/bin/env python
# coding: UTF-8

CronJob = require('cron').CronJob

module.exports = (robot) ->
  # 投稿する時間のデフォルトを定義
  # sendTime = '0 0 10 * * 1-5'
  
  #テスト用
  sendTime = '0 * * * * *'

  # 投稿する部屋のデフォルトを定義
  Room = 'random'
  # 画像のベースURL
  ImageBaseURL = 'http://hoge.com/zoi%s.png'
  # 画像の最終番号
  ImageLastNumber = 22

  # ランダムで投稿する内容
  messages = []
  for(i in range(1, ImageLastNumber + 1))
  {
    messages.append(ImageBaseURL % i)
  }

  # 投稿
  messageFunc = () ->
      # 画像をランダム選択
      message = messages[Math.floor(Math.random() * messages.length)]
      robot.send {Room: "#" + room}, message

  # 投稿のcron設定
  new CronJob sendTime, messageFunc, null, true, 'Asia/Tokyo'
