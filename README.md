powered by guanrongjia at 2018/12/12
all rights reserved


here is an demo for wsgiref.simple_server

in the program ,
you can download files from wsgiref.simple_server,
you can render html and link css, js files,
you can get data through ajax.
its a great demo for learning wsgiref.simple_server.

# start 
you can start the demo use command "python server.py",
then a simple server will start on your computer.

# then
you visit localhost:8000 through your browser.
on the page, you give an url ,that you  want to download all images from it.
the click the button,
the images will download by server to your local dir.

# finally 
you will get an return result from the server,
enjoy coding!

tip:
some ability i referred , is in hello.py
you can read the annotate and code to learn.

#####################################################

这是个 wsgiref.simple_server 的教程，
我在学习的时候，发现很多东西，搜索引擎搜不出来，
可能没人深入的用过这个东西吧。

所以我写了这样一个小工程，
里面包括 请求html， 加载css、js文件，以及文件下载（可以设置文件名）等功能
具体的，看 hello.py 的代码就好了，上面有注释。
