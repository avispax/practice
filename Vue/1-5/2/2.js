Vue.component('my-comp', {
    template: '<p class="static">この場合、static（背景青） + 文字色赤</p>'
})

var v1 = new Vue({ 
    el: '#el2',
    data: {
        myColor: 'red',
        styleObject: {
            color:'blue',
            fontSize: '13px',
        },
        so2: {
            color:'green',
            border: '1px solid red',
        }
    },

});

