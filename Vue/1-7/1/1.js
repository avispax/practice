Vue.component('my-comp', {
    template: '<p class="static">この場合、static（背景青） + 文字色赤</p>'
})

var v1 = new Vue({ 
    el: '#el1',
    data: {
        items: [
            { message: 'AAAAA' },
            { message: 'BBBBB' },
            { message: 'CCCCC' },
        ],

        obj: {
            d1: 'その1',
            d2: 'その2',
            d3: 'その3',
        }
    },
});

