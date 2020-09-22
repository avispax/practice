var app = new Vue({ 
    el: '#l1',
    data: {
        titleMsg: "適当titleMsg",
        msg: "",
    },
    methods: {
        doSomething: function(txt) {
            this.msg = txt;
        }
    }
});
