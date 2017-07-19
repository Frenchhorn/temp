/*
 * 拓展模块，添加使用GET/POST下载资源的方法
 */
exports.create = function create(page) {
    return new this.Casper(page);
}

exports.Casper = function Casper(page) {
    this.page = page;
    this.fs = require('fs');
    //client.js模块所在路径
    this.clientPath = this.fs.absolute(require('system').args[0]) + 'client.js';
    this.client = require(this.clientPath).create();

    this.get = function get(url, targetPath) {
        this.injectClientJs();  //注入client.js
        var content = this.page.evaluate(function(url) {
            return __utils__.sendAJAX(url);
        }, url);
        this.fs.write(targetPath, this.client.decode(content), 'wb');
    }

    this.post = function post(url, data, targetPath) {
        this.injectClientJs();  //注入client.js
        var content = this.page.evaluate(function(url, data) {
            return __utils__.sendAJAX(url, 'POST', data);
        }, url, data);
        this.fs.write(targetPath, this.client.decode(content), 'wb');
    }

    this.injectClientJs = function injectClientJs() {
        "use strict";
        //避免重复注入
        var isJsInjected = this.page.evaluate(function() {
            return typeof __utils__ === 'object';
        });
        if (true === isJsInjected) {
            return ;
        }
        if (true !== this.page.injectJs(this.clientPath)) {
            console.log('WARNING: Failed to inject client module!');
        }
        this.page.evaluate(function() {
            window.__utils__ = new window.Client(); //新建Client对象
        });
    };
};