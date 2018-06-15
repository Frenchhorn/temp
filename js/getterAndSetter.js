var bindObj = function(object) {
    if (typeof object !== 'object') {
        return;
    }
    var obj = object.obj;
    var attr = object.attr;
    var setter = object.setter;
    var getter = object.getter;
    if (!obj || !attr) {
        return;
    }
    if (!obj.hasOwnProperty('_')) {
        obj['_'] = {};
    }
    if (!obj['_'].hasOwnProperty('_')) {
        obj['_']['_'] = {
            'getter': [],
            'setter': []
        };
    }
    getter ? obj['_']['_']['getter'].push(getter) : '';
    setter ? obj['_']['_']['setter'].push(setter) : '';

    if (!obj['_'].hasOwnProperty(attr)) {
        obj['_'][attr] = obj[attr];
        Object.defineProperty(obj, attr, {
            get: function() {
                obj['_']['_']['getter'].forEach(function(func) {
                    func();
                });
                return obj['_'][attr];
            },
            set: function(val) {
                obj['_']['_']['setter'].forEach(function(func) {
                    func(val);
                });
                obj['_'][attr] = val;
            }
        });
    }


}
a = {'z':2, }
bindObj({
    obj: a,
    attr: 'b',
    setter: function(val){console.log('setter', val)},
    getter: function(){console.log('getter')}
})
bindObj({
    obj: a,
    attr: 'b',
    setter: function(val){console.log('setter2', val)},
    getter: function(){console.log('getter2')}
})