package com.google.mlkit.vision.demo.api

import com.google.gson.JsonObject
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path

interface BARDinterface {
    @GET("/api/hello/{question}")
    fun getResponse(@Path("question") question: String): Call<JsonObject>
}