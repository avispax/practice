package com.ibis.mura;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import com.ibis.mura.controller.MyController;

import static org.assertj.core.api.Assertions.assertThat;

// https://spring.io/guides/gs/testing-web/

@WebMvcTest(MyController.class)
public class MyControllerTests {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private ProductInfo productInfo;

    @Test
    public void myTest() throws Exception {
        // when(productInfo.getName()).thenReturn("maguro");
        MvcResult ret = this.mockMvc.perform(get("/product-info?name=maguro&price=100&date_str=2021-01-01"))
                .andExpect(status().isOk())
                .andReturn();

        String body = ret.getResponse().getContentAsString();

        assertThat(body).isEqualTo("aaa");
    }
}