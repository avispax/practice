// todo-item というコンポーネントを生み出している。
// propsはカスタムプロパティで、1アイテムずつって感じ。
Vue.component('todo-item', {
    props: ['todo'],
    template: '<li> {{ todo.text }} -- {{ todo.id }}</li>'
})

// 今回のこのクラスは、どうやらコンポーネントの適用範囲を示すもの？ htmlのl6タグの範囲内でテンプレートが有効になるんだよね。
// htmlを改造してdivを消し去るとtodo-itemは機能しなくなるんだわ。
var l4 = new Vue({
    el: '#l4',
    data: {
        groceryList: [
            { id: 0, text: 'Vegetables' },
            { id: 1, text: 'Cheese' },
            { id: 2, text: 'Whatever else humans are supposed to eat' }
        ]
    }
})