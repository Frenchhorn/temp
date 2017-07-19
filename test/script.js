var fs = require('fs');
//切换至当前脚本路径下，方便引入自定义模块
var isChangeDirSuccees = fs.changeWorkingDirectory(fs.absolute(require('system').args[0]) + '/../');
if (!isChangeDirSuccees) {
    console.log('ERROR: Failed to change working directory!');
    phantom.exit();
}

var page = require('webpage').create();
page.open('http://www.w3school.com.cn/', function(status) {
    var download = require('download').create(page);
    download.get('http://www.w3school.com.cn/i/site_photoref.jpg', 'photo.jpg');
    console.log('LOG: Download Completed!');
    phantom.exit();
});