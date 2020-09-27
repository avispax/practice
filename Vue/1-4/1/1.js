var app = new Vue({ 
    el: '#l1',
    data: {
        msg: 'abcdefg',

        firstName: 'Foo',
        lastName: 'Bar',

        f: 'F',
        l: 'B',

    },
    computed: {
        // 算出関数
        reverseMsg: function() {
            return this.msg.split('').reverse().join('')
        },

        //name
        fullName: function () {
            return this.firstName + ' ' + this.lastName

        },

        // getter & setter
        // app.fName で set が呼ばれて、変数が変わって、getが呼ばれる。そんな感じ。
        fName: {
            get: function() {
                console.log('fName.get')
                return this.f + ' ' + this.l
            },
            set: function(newValue) {
                console.log('fName.set')
                var names = newValue.split(' ')
                this.f = names[0]
                this.l = names[names.length - 1]

            }
        }
    }
});
