// 接受漫画网页地址
var system = require('system')
console.log('loaded system');
url = system.args[1];
if (!url){
    url = 'http://www.dm5.com/m5342-p2/'
}
console.log(url);
var page = require('webpage').create();
page.open(url, function(status) {
  console.log('loading page')
  if(status === "success"){
            // 处理页面
          var pic_url = page.evaluate(function() {
            // DOM操作
            return document.getElementById('cp_image').getAttribute('src');
          });
          console.log(pic_url);
  }else{
    console.log('failed');
  }
  phantom.exit();
});