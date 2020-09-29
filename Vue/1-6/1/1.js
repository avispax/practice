Vue.component('my-comp', {
    template: '<p class="static">この場合、static（背景青） + 文字色赤</p>'
})

var v1 = new Vue({ 
    el: '#el1',
    data: {
        isAAA: false,
        isOK: true,

        selected:'a',
        ops: [
            { text: 'AAAAA', value:'a'},
            { text: 'BBBBB', value:'b'},
            { text: 'CCCCC', value:'c'},
        ],

        loginType: true,

        //ここからv-show
        isBBB: true,
    },
});

