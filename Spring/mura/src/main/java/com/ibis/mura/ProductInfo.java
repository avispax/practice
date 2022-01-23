package com.ibis.mura;

import java.util.Date;

public class ProductInfo {

    private final String name;
    private final int price;
    private final Date date;

    public ProductInfo(String name, int price, Date date) {

        this.name = name;
        this.price = price;
        this.date = date;

    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

    public Date getDate() {
        return date;
    }
}
