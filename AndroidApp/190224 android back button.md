# 뒤로가기 버튼 변경

처음엔 해당 reference를 참고하여 적용하는 데는 성공했으나, 이는 페이지와 페이지 간의 뒤로가기를 적용하는 데에서만 쓰이는 것이었다.

https://www.gajotres.net/ionic-2-3-how-to-manage-hardware-back-button-event-like-a-pro/

wordpress를 웹 사이트 그대로 가져온 내 앱에서는 페이지가 바뀌지 않으므로 온전하게 작동하지 않는다.(뒤로 가지지는 않고 앱 종료만 가능) 하지만 생각보다 간단하게 하나의 페이지 내에서 뒤로 가는 기능을 적용할 수 있는 방법이 있었다. 좀 더 raw하게 들어가서, angular나 js 단에서 뒤로가기를 어떻게 구현하는지를 찾아보면 될 것 같았고, 당연히 그런 기능이 있을 것 같았고, 실제로 그러했다. ionic이 angular를 베이스로 두는 프레임워크라 위의 reference 코드에 짧게 추가만 해주면 되는 것이었다.

https://stackoverflow.com/questions/38767595/accessing-window-object-in-ionic-2-angular-2-beta-10



### udj_and/src/app/app.component.ts

앱에 대한 중앙통제(?)가 이 파일에서 이루어진다.

```ts
import { Component } from '@angular/core';
import { App, Platform, AlertController } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

import { HomePage } from '../pages/home/home';
@Component({
  templateUrl: 'app.html'
})

export class MyApp {
  rootPage:any = HomePage;

  constructor(public platform: Platform, statusBar: StatusBar, splashScreen: SplashScreen, public app: App, public alertCtrl: AlertController) {
    platform.ready().then(() => {
      // Okay, so the platform is ready and our plugins are available.
      // Here you can do any higher level native things you might need.
      statusBar.styleDefault();
      splashScreen.hide();
      

      // customize back button
      platform.registerBackButtonAction(() => {
 
        let nav = app.getActiveNavs()[0];
        let activeView = nav.getActive();                

        if(activeView.name === "HomePage") {
            window.history.back(); // 여기가 새롭게 적용한 js 코드
          }
      });
      // customize back btn - until this line
    });



  }
}
```

