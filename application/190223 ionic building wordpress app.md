# building wordpress android app in ionic

reference from: https://www.youtube.com/watch?v=z4qp7AuqN68

`$ sudo ionic start project_name blank`

Install the free Ionic Appflow SDK and connect your app? `Y`

`$ cd project_name`

`$ code .`

It seems that the directory structure has changed in ionic version 4. So you have to go to different directory to make changes in your source.

`/src/app/home/home.page.html`

```html
<ion-content>
  <iframe src="<wordpress_page_url>" style="width:100%;height:100%"></iframe>
</ion-content>
```



Test your source

: `$ sudo ionic serve -l`	