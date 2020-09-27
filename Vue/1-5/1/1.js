var app = new Vue({ 
    el: '#l1',
    data: {
        isRed: 'true',

        classObject: {
            fontBlue: 'true',   //この場合は1.cssにあるclass名を書け。
            'font-italic': 'true',  //「-」（ハイフン）付きのものは「'」（シングルクォーテーション）で囲む。
        },

        isGreenYellow: 'true',
        isUnderline: 'true',
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
