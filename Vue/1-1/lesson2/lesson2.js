var l2 = new Vue({
    el: '#lesson2',
    data: {
        seen: false,
        todos: [
            { text: 'Learn JavaScript'},
            { text: 'Learn Vue'},
            { text: 'Build something awesome'}
        ]
    }
});

l2.seen=true;
l2.todos.push( {text: 'New item'})
