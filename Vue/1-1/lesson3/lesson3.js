var l3 = new Vue({
    el: '#l3',
    data: {
        message: 'Hello Vue.js!',
        message2:''
    },
    methods: {
        reverseMessage: function() {
            this.message2 = this.message.split('').reverse().join('')
        }
    }
})
