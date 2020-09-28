Vue.component('my-comp', {
    template: '<p class="static">この場合、static（背景青） + 文字色赤</p>'
})

var v1 = new Vue({ 
    el: '#el1',
    data: {
        isRed: true,

        classObject: {
            fontBlue: true,   //この場合は1.cssにあるclass名を書け。
            'font-italic': true,  //「-」（ハイフン）付きのものは「'」（シングルクォーテーション）で囲む。
        },

        isGreenYellow: true,
        isUnderline: true,

        // ここから配列構文
        array1Class: 'fontRed',
        array2Class: 'fontUnderline',

        isFontColor: true,

    },

    computed: {
        classObject2: function() {
            return {
                fontGreenYellow: this.isGreenYellow,    //これもclass名を書く。
                fontUnderline: this.isUnderline,
            }
        }
    }


});

