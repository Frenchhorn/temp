var page = require('webpage').create();
page.open('https://www.baidu.com', function(status) {
  console.log("Status: " + status);
  console.log(require('system').args[0]))
  if(status === "success") {
    page.render('baidu.png');
  }
  phantom.exit();
});