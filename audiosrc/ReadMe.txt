http://www.dspalgorithms.com/products/echo.html

1.回声消除前.wav
  是一个16K，双声道的语音文件，左声道为近端语音、右声道为远端语音
2.aecOut.wav
  这个是上面网站上的回声消除效果
3.icmOut.wav icoolmedia改speex的效果
  收敛速度不够快，但双端语音时效果很好
  out.pcm  16K，单声道，新的效果
  收敛问题解决的比较好，但双端语音时效果差
  目前正在做这两个效果的融合
  
4.left.wav，right.wav是回声消除前.wav左右声道拆分后生成的两个文件，对于做对比