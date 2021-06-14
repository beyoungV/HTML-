//Golang+React Native做APP的好处
      1.学好Golang就是真正的跨平台（PC端、服务器、移动端、WEB端）
      2.不用学java kotlin swift oc等语言
      3.一套代码双端运行（Golang和React Native都只需要编写一套代码就足够）
      4.可以实现对应平台只有原生才能实现的功能（React Native真的只适合做界面，做其他的真是只能靠原生或者用类似Golang等语言来实现）
      5.需要什么功能，编写一次就够了、改bug也极其方便
不过话说回来，如果你要做的APP仅仅是用来展示数据，那么React Native就能满足你的需求了，不过一旦你需要完成一些比较复杂的事情，那么就必须需要用到原生才行。

//一个小说APP为例
  需要实现的功能
      1.在线搜索小说
      2.小说搜索失败时自动切换数据源重试
      3.解析小说章节列表并提取小说信息
      4.解析小说章节内容并去除文字广告
      5.小说章节内容根据屏幕尺寸、字体大小、字体间距、字体行高等条件自动分页
      6.小说章节列表内容自动缓存下载
      7.小说指定章节更换数据来源
      8.章节内容下载失败后自动更换数据源重试
      
      
      
      
      不依赖服务器提供的接口，就必须使用Golang。Golang实现上面的功能实在是不要太简单，做好之后只需要通过gomobile命令直接打包成对应的包提供给React Native调用就行。


//RN依赖的环境配置
        Android SDK
          Android 10 (Q)

        Android SDK Platform
          Android SDK Platform 29
          Intel x86 Atom_64 System Image or Google APIs Intel x86 Atom System Image
            Android SDK Build-Tools 29.0.2

        Android Virtual Device

        ANDROID_HOME environment variable
        ANDROID_HOME
        %LOCALAPPDATA%\Android\Sdk

        powershell
        Get-ChildItem -Path Env:\

        %LOCALAPPDATA%\Android\Sdk\platform-tools

npx react-native init AwesomeProject //generate a new project.创建新项目
npx react-native init AwesomeProject --version X.XX.X //使用react-native特定版本
npx react-native init AwesomeTSProject --template react-native-template-typescript //using typescript.使用Typescipt

adb devices //检测手机连接
