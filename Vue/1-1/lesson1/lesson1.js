var app = new Vue({ 
    el: '#lesson1', //element : lesson1 これは html で id="lesson1" と使用する。
    data: {
        message: 'Hello Vue!',
        testTitle: 'test title desu.'
    }
});

//ここはインスタンス名の「app」で書く。
app.message = "I have changed the data!";