//■D002:数の比較
object Main extends App{
    val sc = new java.util.Scanner(System.in)
    val m,n = sc.nextInt

    if (m == n)
    	println("eq")
    else if (m < n)
    	println(n)
    else
    	println(m)
}

//■D003:掛け算のリスト
object Main extends App{
    val sc = new java.util.Scanner(System.in)
    val n = sc.nextInt

    var ans: String = ""
    for (i <- 1 to 9) {
    	ans += (n * i).toString + " "
    }
    println(ans.trim)
}

//■D003:掛け算のリスト その2
object Main extends App{
    val sc = new java.util.Scanner(System.in)
    val n = sc.nextInt

    var ans: String = ""
    (1 to 9).foreach(ans += n * _ + " ")
    println(ans.trim)

}

//D004:文字列の結合
object Main extends App{
    val sc = new java.util.Scanner(System.in)
    val n = sc.nextInt
    var list = List.fill(n)(sc.next)

    println("Hello " + list.mkString(",") + ".")
}