package com.ibis.mura.controller;

import com.ibis.mura.ProductInfo;

import java.util.Date;

import java.text.SimpleDateFormat;
import java.text.ParseException;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
public class MyController {

    @GetMapping("/product-info")
    public ProductInfo index(@RequestParam String name, @RequestParam int price, @RequestParam String date_str) {

        ProductInfo productInfo = null;
        Date date = null;

        try {

            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
            date = dateFormat.parse(date_str);

            productInfo = new ProductInfo(name, price, date);

        } catch (ParseException e) {

        }

        return productInfo;
    }

}
